#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

import math
from rclpy.executors import MultiThreadedExecutor

from phidget_stepper_controllers_msgs.action import SpeedController
from phidget_stepper_controllers.speed_controller_server import SpeedControllerServer

from geometry_msgs.msg import Twist, Pose
from tf2_ros import TransformBroadcaster

from navigation_utils.utils import *

class CmdVelSubscriber(Node):

    def __init__(self):
        super().__init__('simple_cmdvel_sub')

        assert self.declare_parameter('left_wheel_stepper', 0)
        assert self.declare_parameter('right_wheel_stepper', 1)
        assert self.declare_parameter('entraxe', 18.44)
        assert self.declare_parameter('wheel_radius', 4.06)
        assert self.declare_parameter('step_count', 200)
        assert self.declare_parameter('encoder_tics_count', 1200)
        assert self.declare_parameter('left_wheel_encoder', 2)
        assert self.declare_parameter('right_wheel_encoder', 3)
        assert self.declare_parameter('navigation_hub', 723793)
        assert self.declare_parameter('odom_period', 0.5)
        assert self.declare_parameter('stop_topic', "stop")
        assert self.declare_parameter('speed_factor',"speed_factor")
        assert self.declare_parameter('tics_per_step', 32)

        # ===== get the param and compute all the values needed

        hub_serial = self.get_parameter('navigation_hub').get_parameter_value().integer_value

        # for steppers
        stop_topic = self.get_parameter('stop_topic').get_parameter_value().string_value
        speed_factor = self.get_parameter('speed_factor').get_parameter_value().string_value
        tics_per_step = self.get_parameter('tics_per_step').get_parameter_value().integer_value
        step_count = self.get_parameter('step_count').get_parameter_value().integer_value # steps per rotation

        # geometry constraints
        self.entraxe = self.get_parameter('entraxe').get_parameter_value().double_value / 100  # meters
        self.wheel_radius = self.get_parameter('wheel_radius').get_parameter_value().double_value / 100  # meters
        self.step_per_meter = 1 / (2 * math.pi * self.wheel_radius) * step_count

        self.get_logger().info(f"[cmd_callback Lib][{self.wheel_radius}] Initialization complete")
        self.get_logger().info(f"[cmd_callback Lib][{step_count}] Initialization complete")
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
        odom_period = self.get_parameter('odom_period').get_parameter_value().double_value

        self.get_logger().info(f"[cmd_vel] All params init")

        # ==== init steppers and associated action server

        self.left_stepper_obj = SpeedControllerServer(self, hub_serial,
                                                 self.get_parameter('left_wheel_stepper').get_parameter_value().integer_value,
                                                 "left_wheel",
                                                 1 / tics_per_step,
                                                 stop_topic,
                                                 speed_factor)
        
        self.left_stepper_as = ActionClient(self, SpeedController, 'left_wheel')

        self.right_stepper_obj = SpeedControllerServer(self, hub_serial,
                                                 self.get_parameter('right_wheel_stepper').get_parameter_value().integer_value,
                                                 "right_wheel",
                                                 1 / tics_per_step,
                                                 stop_topic,
                                                 speed_factor)

        self.right_stepper_as = ActionClient(self, SpeedController, 'right_wheel')
        

        if self.odom_activate:
            # init the odom publisher
            self.odom_pub = self.create_publisher(Odometry, "/odom", 1)

            # init encoders
            self.left_encoder = init_encoder(hub_serial,
                                             self.get_parameter('left_wheel_encoder').get_parameter_value().integer_value,
                                             int(odom_period*1000/5))
            

            self.right_encoder = init_encoder(hub_serial,
                                              self.get_parameter('right_wheel_encoder').get_parameter_value().integer_value,
                                              int(odom_period*1000/5))

            # the initial position and speed
            self.wheels_pos = (-self.left_encoder.getPosition(), self.right_encoder.getPosition())
            
            # the position (0, 0)
            self.pos = Pose()

            #self.timer = self.create_timer(odom_period, self.timer_callback)

            self.get_logger().info('[cmd_vel] All encoders started')

        self.last_cmd_vel = None
        self.cmd_vel_canceled = False
        self._cmd_vel = self.create_subscription(Twist, "cmd_vel", self.cmd_callback, 1)

        self.br = TransformBroadcaster(self)

        self.get_logger().info('[cmd_vel] Ready')

    def cmd_callback(self, msg):
        self.last_cmd_vel = msg  # update the last cmd_vel received

        if not self.cmd_vel_canceled:  # if the action server weren't canceled
            self.cmd_vel_canceled = True  # cancel the stepper action

            self.get_logger().info(f"[cmd_callback Lib][{msg}] Initialization complete")
            self.get_logger().info(f"[cmd_callback Lib][{self.step_per_meter}] Initialization complete")

            right_goal = SpeedController.Goal()
            right_goal.velocity_limit = (self.last_cmd_vel.linear.x + self.last_cmd_vel.angular.z
                                            * self.get_parameter('entraxe').get_parameter_value().double_value/2) * self.step_per_meter
            left_goal = SpeedController.Goal()
            left_goal.velocity_limit = -(self.last_cmd_vel.linear.x - self.last_cmd_vel.angular.z
                                            * self.get_parameter('entraxe').get_parameter_value().double_value/2) * self.step_per_meter

            self.right_stepper_as.wait_for_server()
            self.left_stepper_as.wait_for_server()

            self.right_stepper_as.send_goal_async(right_goal)
            self.left_stepper_as.send_goal_async(left_goal)

            self.cmd_vel_canceled = False

    def timer_callback(self):
        prev_wheels_pos = self.wheels_pos
        self.wheels_pos = (-self.left_encoder.getPosition(), self.right_encoder.getPosition())

        dx, dy, dtheta = odom_position_calculation(self.wheels_pos, prev_wheels_pos,
                                                self.pos.orientation.z,
                                                self.wheel_radius, self.entraxe,
                                                self.encoder_tics_count)
        self.pos.position.x += dx
        self.pos.position.y += dy
        self.pos.orientation.z += dtheta

        broadcast_associated_tf(self, self.br, self.pos)

        self.odom_pub.publish(get_odom_msg(self, self.pos))

def main(args=None):
    rclpy.init(args=args)  # Initialize the ROS 2 Python client library

    # Create an instance of your custom node
    cmd_vel_subscriber = CmdVelSubscriber()

    # Spin the node so its callbacks can be called
    executor = MultiThreadedExecutor()
    executor.add_node(cmd_vel_subscriber)
    executor.spin()

    # Shutdown the ROS 2 Python client library
    cmd_vel_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()