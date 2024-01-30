#!/usr/bin/env python3
import rclpy
import time

from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.action import CancelResponse
from rclpy.action import GoalResponse

from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *

from Phidget22.Phidget import *
from Phidget22.Devices.Stepper import *

from phidget_stepper_controllers_msgs.action import StepController

from std_msgs.msg import Float64, Bool


def init_stepper(hub_serial, hub_port, rescale_factor):
    """
    Je suis un joyeux commentaire
    Init the stepper at the hub_port

    @param rescale_factor: the factor to rescale the unit to a step
    @param hub_serial: the serial of the hub
    @param hub_port: the port on which the stepper is
    @return: the Stepper()
    """

    Log.enable(LogLevel.PHIDGET_LOG_INFO, "phidgetlog.log")

    stepper = Stepper()
    stepper.setHubPort(hub_port)
    stepper.setDeviceSerialNumber(hub_serial)
    stepper.openWaitForAttachment(500)
    stepper.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
    stepper.setRescaleFactor(rescale_factor)
    stepper.setEngaged(True)

    return stepper

class StepControllerServer:

    def __init__(self, node, hub_serial, hub_port, action_server_name, rescale_factor=1/32, stop_topic=None, speed_factor_topic=None):
        """
        Create an action server controlling the stepper step by step

        @param hub_serial: the serial of the hub
        @param hub_port: the port on which the stepper is
        @param action_server_name: the name of the action server to create
        @param rescale_factor: (default: 1/32) the factor to rescale position/velocity/acceleration output
        @param stop_topic: (optional) the name of the stop topic
        @param speed_factor_topic: (optional) the name of the speed factor topic
        """
        # default values
        self.speed_factor = 1
        self.speed = 0
        self.stopped = False

        self.node = node

        # listen to topics
        if stop_topic is not None:
            self.stop_topic  = node.create_subscription(Bool, 'stop', self.stop_callback, 1)
        if speed_factor_topic is not None:
            self.speed_factor_topic  = node.create_subscription(Float64, 'speed_factor', self.speed_callback, 1)

        # init stepper
        self.stepper = init_stepper(hub_serial, hub_port, rescale_factor)

        # make sure the stepper is stopped
        self.stepper.setVelocityLimit(0)
        self.stepper.setTargetPosition(self.stepper.getPosition())

        # launch the action server
        self._as = ActionServer(node,
                                StepController,
                                action_server_name,
                                execute_callback=self.execute_callback,
                                goal_callback=self.goal_callback,
                                cancel_callback=self.cancel_callback)

        node.get_logger().info(f"[Stepper Lib][{action_server_name}] Initialization complete")

    def goal_callback(self, goal_request):
        return GoalResponse.ACCEPT if not self.stopped else GoalResponse.REJECT

    def cancel_callback(self, goal_handle):
        return CancelResponse.ACCEPT

    def execute_callback(self, goal_handle):
        result = StepController.Result()

        if self.stopped:
            self.stepper.setVelocityLimit(0)
            self.stepper.setTargetPosition(self.stepper.getPosition())

            result.steps_done = 0
            result.done = False
            self._as.set_aborted(result)
            return

        origin = self.stepper.getPosition()
        current = origin
        target = origin + goal_handle.request.steps_goal

        self.speed = goal_handle.request.velocity_limit

        self.stepper.setVelocityLimit(int(self.speed * self.speed_factor))
        self.stepper.setTargetPosition(target)


        while abs(current - target) > 1:
            feedback = StepController.Feedback()

            current = self.stepper.getPosition()

            # check that preempt has not been requested by the client
            if goal_handle.is_cancel_requested() or self.stopped:
                break

            # publish the feedback
            feedback.steps_from_start = int(target - current)
            goal_handle.publish_feedback(feedback)

            time.sleep(0.1)

        # publish result
        result = StepController.Result()
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

def main(args=None):
    rclpy.init(args=args)

    step_control_server = StepControllerServer()

    rclpy.spin(step_control_server)


if __name__ == '__main__':
    main()