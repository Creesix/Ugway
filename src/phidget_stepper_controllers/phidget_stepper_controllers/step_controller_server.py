#!/usr/bin/env python3

# A remplacer par rcllpy import rospy

from Phidget22.Phidget import *
from Phidget22.Devices.Stepper import *

import actionlib
from phidget_stepper_controllers.msg import StepControllerAction, StepControllerResult, StepControllerFeedback
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
    stepper.setControlMode(StepperControlMode.CONTROL_MODE_STEP)
    stepper.setRescaleFactor(rescale_factor)
    stepper.setEngaged(True)

    return stepper

class StepControllerServer:

    def __init__(self, hub_serial, hub_port, action_server_name, rescale_factor=1/32, stop_topic=None, speed_factor_topic=None):
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

        # listen to topics
        if stop_topic is not None:
            self.stop_topic = rospy.Subscriber(stop_topic, Bool, self.stop_callback, queue_size=1)
        if speed_factor_topic is not None:
            self.speed_factor_topic = rospy.Subscriber(speed_factor_topic, Float64, self.speed_callback, queue_size=1)

        # init stepper
        self.stepper = init_stepper(hub_serial, hub_port, rescale_factor)

        # make sure the stepper is stopped
        self.stepper.setVelocityLimit(0)
        self.stepper.setTargetPosition(self.stepper.getPosition())

        # launch the action server
        self._as = actionlib.SimpleActionServer(action_server_name, StepControllerAction,
                                                execute_cb=self.execute_cb, auto_start=False)
        self._as.start()

        rospy.loginfo(f"[Stepper Lib][{action_server_name}] Initialization complete")


    def execute_cb(self, goal):
        result = StepControllerResult()

        if self.stopped:
            self.stepper.setVelocityLimit(0)
            self.stepper.setTargetPosition(self.stepper.getPosition())

            result.steps_done = 0
            result.done = False
            self._as.set_aborted(result)
            return

        origin = self.stepper.getPosition()
        current = origin
        target = origin + goal.steps_goal

        self.speed = goal.velocity_limit

        self.stepper.setVelocityLimit(int(self.speed * self.speed_factor))
        self.stepper.setTargetPosition(target)


        while abs(current - target) > 1:
            feedback = StepControllerFeedback()

            current = self.stepper.getPosition()

            # check that preempt has not been requested by the client
            if self._as.is_preempt_requested() or self.stopped:
                break

            # publish the feedback
            feedback.steps_from_start = int(target - current)
            self._as.publish_feedback(feedback)

            rospy.sleep(rospy.Duration(0.1))

        # publish result
        result.done = False
        result.steps_done = int(target - origin)

        if abs(target - current) <= 1:
            result.done = True
            self._as.set_succeeded(result)
        elif self.stopped:
            self._as.set_aborted(result)
        elif self._as.is_preempt_requested():
            self._as.set_preempted(result)
        else:
            self._as.set_aborted(result)

    def speed_callback(self, msg):
        self.speed_factor = msg.data

        if not self.stopped:
            self.stepper.setVelocityLimit(int(self.speed * self.speed_factor))

    def stop_callback(self, msg):
        self.stopped = msg.data

        if self.stopped:
            self.stepper.setVelocityLimit(0)
            self.stepper.setTargetPosition(self.stepper.getPosition())

