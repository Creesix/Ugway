#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient
from rclpy.action import CancelResponse
from rclpy.action import GoalResponse

import tf2_ros
from tf2_ros import LookupException, ConnectivityException, ExtrapolationException
import tf_transformations

from math import sqrt, atan2, pi
import numpy as np
from tf_transformations import euler_from_quaternion

from phidget_stepper_controllers_msgs.action import Trajectoire, WheelsDistance

class TrajectoryActionServer(Node):
    def __init__(self):
        super().__init__('trajectory_server')
        self._action_server = ActionServer(
            self,
            Trajectoire, 
            'trajectory_action',
            execute_callback=self.execute_cb,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )

        # ROS 2 action client
        self._action_client = ActionClient(
            self,
            WheelsDistance, 
            'DistanceMainWheelsController'
        )

        # TF listener setup
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        assert self.declare_parameter('use_odom', False)
        assert self.declare_parameter('entraxe', 0.0)
        assert self.declare_parameter('trajectory_goal_error', 0.0)
        assert self.declare_parameter('is_left_side', True)
        assert self.declare_parameter('y_depart', 0.0)
        assert self.declare_parameter('x_depart', 0.0)
        assert self.declare_parameter('angle_depart', 0.0)

        self.use_odom = self.get_parameter('use_odom').get_parameter_value().bool_value
        self.entraxe = self.get_parameter('entraxe').get_parameter_value().double_value / 100
        self.trajectory_goal_error = self.get_parameter('trajectory_goal_error').get_parameter_value().double_value

        self.is_left_side = self.get_parameter('is_left_side').get_parameter_value().bool_value
        self.y_depart = self.get_parameter('y_depart').get_parameter_value().double_value
        self.x_depart = -self.get_parameter('x_depart').get_parameter_value().double_value if not self.is_left_side else self.get_parameter('x_depart').get_parameter_value().double_value
        self.angle_depart = np.pi - self.get_parameter('angle_depart').get_parameter_value().double_value if not self.is_left_side else self.get_parameter('angle_depart').get_parameter_value().double_value

        self.get_logger().info('[Trajectory Server] Ready')

    def goal_callback(self, goal_request):
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        return CancelResponse.ACCEPT

    def __set_starting_pos__(self, with_odom=False):
        """
        Set self.x1, self.y1, self.angle1 using either the odom or the last point of the trajectory

        @param with_odom: if odom should be used
        @return:
        """
        if with_odom:  # if using the odom then get the current pos
            try:
                trans = self.tf_buffer.lookup_transform('map', 'base_footprint', rclpy.time.Time())
                self.x1 = trans.transform.translation.x
                self.y1 = trans.transform.translation.y
                quat = trans.transform.rotation

                # Convert quaternion to Euler angles
                euler = tf_transformations.euler_from_quaternion([quat.x, quat.y, quat.z, quat.w])
                self.angle1 = euler[2]
            except (LookupException, ConnectivityException, ExtrapolationException) as e:
                self.get_logger().error(f'Failed to get transform: {e}')
                # Handle the failure to obtain a transform, possibly by retrying or setting default values
        else:
            # Otherwise, the current pos is the last position that should have been reached
            self.x1 = self.x2
            self.y1 = self.y2
            self.angle1 = self.angle2

    def __calculate_dist_and_angle__(self, traj_dir=1):
        """
        Calculate the distance and angle to the next point in the trajectory

        @param traj_dir: the direction use by the robot (> 0 => forward, < 0 => backward)
        @return:
        """

        # calculate path
        dist = sqrt((self.x1 - self.x2) * (self.x1 - self.x2) + (self.y1 - self.y2) * (self.y1 - self.y2))
        self.angle2 = atan2(self.y2 - self.y1, self.x2 - self.x1)

        if traj_dir < 0:
            self.angle2 += pi
            dist = -dist
        angle = self.angle2 - self.angle1

        # make sure - pi <= angle <= pi
        angle -= ((angle + pi) // (2 * pi)) * 2 * pi

        return dist, angle

    def __move__(self, dist, angle, traj_dir):
        goal_msg = WheelsDistance.Goal()
        goal_msg.velocity_limit = 0.1 * abs(traj_dir)

        # First rotate the robot
        if angle != 0:
            goal_msg.distance_left = -angle * self.entraxe / 2
            goal_msg.distance_right = angle * self.entraxe / 2

            # Sending goal and waiting for result
            send_goal_future = self.action_client.send_goal_async(goal_msg)
            rclpy.spin_until_future_complete(self.node, send_goal_future)
            goal_handle = send_goal_future.result()

            if not goal_handle.accepted:
                self.get_logger().info('Goal rejected :(')
                return

            self.get_logger().info('Goal accepted :)')

            result_future = goal_handle.get_result_async()
            rclpy.spin_until_future_complete(self.node, result_future)
            result = result_future.result()
            self.get_logger().info('Result received')

        # Then move
        if dist != 0:
            goal_msg.distance_left = dist
            goal_msg.distance_right = dist

            # Sending goal and waiting for result
            send_goal_future = self.action_client.send_goal_async(goal_msg)
            rclpy.spin_until_future_complete(self.node, send_goal_future)
            goal_handle = send_goal_future.result()

            if not goal_handle.accepted:
                self.get_logger().info('Goal rejected :(')
                return

            self.get_logger().info('Goal accepted :)')

            result_future = goal_handle.get_result_async()
            rclpy.spin_until_future_complete(self.node, result_future)
            result = result_future.result()
            self.get_logger().info('Result received')

    def execute_cb(self, trajectory):
        success = True

        goal_trajX = trajectory.request.traj_x
        goal_trajY = trajectory.request.traj_y
        goal_trajDir = trajectory.request.traj_dir
        
        n = len(goal_trajX)

        # take symmetrical traj if necessary
        goal_trajX = [trajX if self.is_left_side else - trajX for trajX in goal_trajX]

        self.get_logger().info(f"[Trajectory Server] New trajectory received ({n} points)")
        for i in range(n):

            # get the starting position of the trajectory
            self.__set_starting_pos__(self.use_odom)

            # the next pos to go
            self.x2 = goal_trajX[i]
            self.y2 = goal_trajY[i]
            traj_dir = goal_trajDir[i] # forward/backward

            # calculate dist and angle to (x2, y2)
            dist, angle = self.__calculate_dist_and_angle__(traj_dir)

            # move (first rotate and move linearly)
            self.__move__(dist, angle, traj_dir)

            self._feedback.percentage = (i+1)/n if self.use_odom else i/n # if the odom is activated there one more correction point
            self.server.publish_feedback(self._feedback)

        # get the starting position of the trajectory
        self.__set_starting_pos__(True)
        dist, angle = self.__calculate_dist_and_angle__()
        self.get_logger().info(f"[Trajectory Server] Distance from objective {dist} m {angle/pi*180} °")

        if self.use_odom and dist > self.trajectory_goal_error:
            self.get_logger().info(f"[Trajectory Server] The error is too important ! Using odom to correct")
            self.__move__(dist, angle, 1)

            self._feedback.percentage = 1
            self.server.publish_feedback(self._feedback)

        self.get_logger().info("[Trajectory Server] Trajectory finished")
        
        if success:
            self._result.done = True
            self.server.set_succeeded(self._result)
        else:
            self._result.done = False
            self.server.set_aborted(self._result)

def main(args=None):
    rclpy.init(args=args)

    trajectory_action_server = TrajectoryActionServer()
    
    rclpy.spin(trajectory_action_server)

    trajectory_action_server.destroy()
    rclpy.shutdown()

if __name__ == '__main__':
    main()