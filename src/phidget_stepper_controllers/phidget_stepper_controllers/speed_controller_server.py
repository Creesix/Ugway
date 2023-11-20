#!/usr/bin/env python3

import rclpy
from rclpy.action import ActionServer
from rclpy.action import CancelResponse
from rclpy.action import GoalResponse

from Phidget22.Phidget import *
from Phidget22.Devices.Stepper import *

from phidget_stepper_controllers_msgs.action import SpeedController
from std_msgs.msg import Float64, Bool

def init_stepper(hub_serial, hub_port, rescale_factor):
    """
    Init the stepper at the hub_port

    @param rescale_factor: the factor to rescale the unit to a step
    @param hub_serial: the serial of the hub
    @param hub_port: the port on which the stepper is
    @return: the Stepper()
    """
    stepper = Stepper()
    stepper.setHubPort(hub_port)
    stepper.setDeviceSerialNumber(hub_serial)
    stepper.openWaitForAttachment(500)
    stepper.setControlMode(StepperControlMode.CONTROL_MODE_RUN)
    stepper.setRescaleFactor(rescale_factor)
    stepper.setEngaged(True)

    return stepper

class SpeedControllerServer:

    def __init__(self, node, hub_serial, hub_port, action_server_name, rescale_factor=1/32, stop_topic=None, speed_factor_topic=None):
        """
        Create an action server controlling the stepper with speed (step/s)
				
        @param node: the ROS2 node
        @param hub_serial: the serial of the hub
        @param hub_port: the port on which the stepper is
        @param action_server_name: the name of the action server to create
        @param stop_topic: (optional) the name of the stop topic
        @param speed_factor_topic: (optional) the name of the speed factor topic
        """
        # default values
        self.speed_factor = 1
        self.speed = 0
        self.stopped = False

        # listen to topics
        if stop_topic is not None:
            self.stop_topic  = node.create_subscription(Bool, 'stop_topic', self.stop_callback, 1)
        if speed_factor_topic is not None:
            self.speed_factor_topic  = node.create_subscription(Float64, 'speed_factor_topic', self.speed_callback, 1)

        # init stepper
        self.stepper = init_stepper(hub_serial, hub_port, rescale_factor)

        # make sure the stepper is stopped
        self.stepper.setVelocityLimit(0)

        # launch the action server
        self._as = ActionServer(node,
                                SpeedController,
                                action_server_name,
                                execute_callback=self.execute_callback,
                                goal_callback=self.goal_callback,
                                cancel_callback=self.cancel_callback)

        node.get_logger().info(f"[Stepper Lib][{action_server_name}] Initialization complete")
		
    def goal_callback(self, goal_request):
        return GoalResponse.ACCEPT if not self.stopped else GoalResponse.REJECT

    def cancel_callback(self, goal_handle):
        return CancelResponse.ACCEPT

    async def execute_callback(self, goal_handle):
        self.speed = goal_handle.velocity_limit
        self.stepper.setVelocityLimit(self.speed * self.speed_factor)

        while abs(self.speed * self.speed_factor - self.stepper.getVelocity()) > 0.5:
            feedback = SpeedController.Feedback()

            # check that preempt has not been requested by the client
            if goal_handle.is_cancel_requested() or self.stopped:
                break

            # publish the feedback
            feedback.observed_velocity = self.stepper.getVelocity()
            feedback.theoretical_velocity = self.stepper.getVelocity() / self.speed_factor
            goal_handle.publish_feedback(feedback)

            node.create_rate(0.1).sleep()

        # publish result
        result = SpeedController.Result()
        result.done = False
        if abs(self.speed * self.speed_factor - self.stepper.getVelocity()) <= 0.5:
            result.done = True
				
        if goal_handle.is_cancel_requested() or self.stopped:
            goal_handle.canceled()
        else:
            goal_handle.succeed()
               
        return result

    def speed_callback(self, msg):
        self.speed_factor = msg.data

        if not self.stopped:
            self.stepper.setVelocityLimit(int(self.speed * self.speed_factor))

    def stop_callback(self, msg):
        self.stopped = msg.data

        if self.stopped:
            self.stepper.setVelocityLimit(0)

