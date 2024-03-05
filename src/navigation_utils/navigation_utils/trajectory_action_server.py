#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, ActionClient

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
            self.execute_cb
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

        # Parameters
        self.declare_parameters(namespace='',
                                parameters=[
                                    ('use_odom', False),
                                    ('entraxe', 0.0),
                                    ('trajectory_goal_error', 0.0),
                                    ('is_left_side', True),
                                    ('y_depart', 0.0),
                                    ('x_depart', 0.0),
                                    ('angle_depart', 0.0)
                                ])

        self.use_odom = self.get_parameter('use_odom').value
        self.entraxe = self.get_parameter('entraxe').value / 100
        self.trajectory_goal_error = self.get_parameter('trajectory_goal_error').value

        self.is_left_side = self.get_parameter('is_left_side').value
        self.y_depart = self.get_parameter('y_depart').value
        self.x_depart = -self.get_parameter('x_depart').value if not self.is_left_side else self.get_parameter('x_depart').value
        self.angle_depart = np.pi - self.get_parameter('angle_depart').value if not self.is_left_side else self.get_parameter('angle_depart').value

        self.get_logger().info('[Trajectory Server] Ready')


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

def main(args=None):
    rclpy.init(args=args)

    trajectory_action_server = TrajectoryActionServer()
    
    rclpy.spin(trajectory_action_server)

    trajectory_action_server.destroy()
    rclpy.shutdown()

if __name__ == '__main__':
    main()