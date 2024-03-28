#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionClient
from rclpy.action import ActionServer
from rclpy.action import CancelResponse
from rclpy.action import GoalResponse
from rclpy.node import Node

import math

from phidget_stepper_controllers_msgs.action import StepController, WheelsDistance
from phidget_stepper_controllers.step_controller_server import StepControllerServer

from geometry_msgs.msg import Twist, Pose

from navigation_utils.utils import *

class DistanceWheelsController(Node):

    def __init__(self):
        super().__init__('simple_stepController')

        assert self.declare_parameter('navigation_hub', 723793)
        assert self.declare_parameter('left_wheel_stepper', 0)
        assert self.declare_parameter('right_wheel_stepper', 1)
        assert self.declare_parameter('entraxe', 0.0)
        assert self.declare_parameter('wheel_radius', 0.0)
        assert self.declare_parameter('step_count', 200)
        assert self.declare_parameter('stop_topic', "stop_all")
        assert self.declare_parameter('speed_factor', "speed_factor")
        assert self.declare_parameter('tics_per_step', 32)
        assert self.declare_parameter('encoder_tics_count', 1200)
        assert self.declare_parameter('left_wheel_encoder', 2)
        assert self.declare_parameter('right_wheel_encoder', 3)
        assert self.declare_parameter('odom_period', 0.25)

        # ===== get the param and compute all the values needed

        hub_serial = self.get_parameter("navigation_hub").get_parameter_value().integer_value

        # for steppers
        stop_topic = self.get_parameter("stop_topic").get_parameter_value().string_value
        speed_factor = self.get_parameter("speed_factor").get_parameter_value().string_value
        tics_per_step = self.get_parameter("tics_per_step").get_parameter_value().integer_value
        step_count = self.get_parameter('step_count').get_parameter_value().integer_value # steps per rotation

        # geometry constraints
        self.entraxe = self.get_parameter('entraxe').get_parameter_value().double_value / 100  # meters
        self.wheel_radius = self.get_parameter('wheel_radius').get_parameter_value().double_value / 100  # meters
        self.step_per_meter = 1 / (2 * math.pi * self.wheel_radius) * step_count

        # for encoders
        self.odom_activate = self.get_parameter('encoder_tics_count').get_parameter_value().integer_value\
                        or self.get_parameter('left_wheel_encoder').get_parameter_value().integer_value\
                        or self.get_parameter('right_wheel_encoder').get_parameter_value().integer_value
        
        self.odom_activate = False

        if self.odom_activate:
            assert self.get_parameter('encoder_tics_count').get_parameter_value().integer_value
            assert self.get_parameter('left_wheel_encoder').get_parameter_value().integer_value
            assert self.get_parameter('right_wheel_encoder').get_parameter_value().integer_value

        self.encoder_tics_count = self.get_parameter('encoder_tics_count').get_parameter_value().integer_value
        odom_period = self.get_parameter("odom_period").get_parameter_value().double_value

        self.get_logger().info(f"[main wheels] All params init")

        # ==== init steppers and associated action server


        self.left_stepper_obj = StepControllerServer(self, hub_serial,
                                                 self.get_parameter('left_wheel_stepper').get_parameter_value().integer_value,
                                                 "left_wheel",
                                                 1 / tics_per_step,
                                                 stop_topic,
                                                 speed_factor)
        
        self.left_stepper_as = ActionClient(self, StepController, 'left_wheel')

        self.right_stepper_obj = StepControllerServer(self, hub_serial,
                                                 self.get_parameter('right_wheel_stepper').get_parameter_value().integer_value,
                                                 "right_wheel",
                                                 1 / tics_per_step,
                                                 stop_topic,
                                                 speed_factor)
        
        self.right_stepper_as = ActionClient(self, StepController, 'right_wheel')

        self.get_logger().info(f"[main wheels] All steppers started")

        if self.odom_activate:
            # init the odom publisher
            self.odom_pub = self.create_publisher(Odometry, "/odom", 1)

            # init encoders
            self.left_encoder = init_encoder(hub_serial,
                                             self.get_parameter('left_wheel_encoder').get_parameter_value().integer_value,
                                             odom_period*1000/5)
            self.right_encoder = init_encoder(hub_serial,
                                             self.get_parameter('right_wheel_encoder').get_parameter_value().integer_value,
                                             odom_period*1000/5)

            # the initial position and speed
            self.wheels_pos = (-self.left_encoder.getPosition(), self.right_encoder.getPosition())
            #self.timer = self.create_timer(odom_period, self.timer_callback)

            # the position (0, 0)
            self.pos = Pose()

            self.get_logger().info("[main wheels] All encoders started")

        self._feedback = WheelsDistance.Feedback()

        self._as = ActionServer(self, WheelsDistance,'WheelsDistance',                                 
                                execute_callback=self.execute_cb,
                                goal_callback=self.goal_callback,
                                cancel_callback=self.cancel_callback)

        self.get_logger().info("[main wheels] Ready")

    def goal_callback(self, goal_request):
        return GoalResponse.ACCEPT if not self.stopped else GoalResponse.REJECT

    def cancel_callback(self, goal_handle):
        return CancelResponse.ACCEPT

    def execute_cb(self, msg):
        result = WheelsDistance.Result()

        left_goal = StepController.Goal()
        right_goal = StepController.Goal()

        right_goal.steps_goal = int(msg.distance_right * self.step_per_meter)
        left_goal.steps_goal = - int(msg.distance_left * self.step_per_meter)

        right_goal.velocity_limit = int(msg.velocity_limit * self.step_per_meter)
        left_goal.velocity_limit = int(msg.velocity_limit * self.step_per_meter)

        self.right_stepper_as.wait_for_server()
        self.left_stepper_as.wait_for_server()      

        right_send_goal_future = self.right_stepper_as.send_goal_async(right_goal, feedback_cb=self.feedback_right)
        left_send_goal_future = self.left_stepper_as.send_goal_async(left_goal, feedback_cb=self.feedback_left)

        # Attendre que les resultats soient obtenus
        right_result = self.right_stepper_as.get_result()
        left_result = self.right_stepper_as.get_result()

        result.done = True
        result.done_distance_right = right_result.steps_done / self.step_per_meter
        result.done_distance_left = - left_result.steps_done / self.step_per_meter
        self._as.set_succeeded(result)

    def feedback_right(self, msg):
        self._feedback.distance_right_from_start = msg.steps_from_start / self.step_per_meter

    def feedback_left(self, msg):
        self._feedback.distance_left_from_start = - msg.steps_from_start / self.step_per_meter

    def timer_callback(self, _):
        prev_wheels_pos = self.wheels_pos
        self.wheels_pos = (-self.left_encoder.getPosition(), self.right_encoder.getPosition())

        dx, dy, dtheta = odom_position_calculation(self.wheels_pos, prev_wheels_pos,
                                                   self.pos.orientation.z,
                                                   self.wheel_radius, self.entraxe,
                                                   self.encoder_tics_count)
        self.pos.position.x += dx
        self.pos.position.y += dy
        self.pos.orientation.z += dtheta

        broadcast_associated_tf(self.pos)
        self.odom_pub.publish(get_odom_msg(self.pos))


def main(args=None):
    rclpy.init(args=args)

    dist_sub = DistanceWheelsController()

    # Spin the node so its callbacks can be called
    rclpy.spin(dist_sub)

    # Shutdown the ROS 2 Python client library
    dist_sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()