#!/usr/bin/env python3
import rospy
import actionlib

from phidget_stepper_controllers.msg import StepControllerAction, StepControllerGoal
from phidget_stepper_controllers.step_controller_server import StepControllerServer

from actionlib_msgs.msg import GoalStatus
from std_msgs.msg import Float64, Bool

stepper = rospy.get_param('stepper')
serialNumber = rospy.get_param('hub')
ticsPerStep = rospy.get_param('ticsPerStep')
step_per_rotation = 360/rospy.get_param('pasStepper')
speed = 100

if step_per_rotation != int(step_per_rotation):
    print(f"step_per_rotation will be round of {step_per_rotation - int(step_per_rotation)}")
step_per_rotation = int(step_per_rotation)

states = {GoalStatus.PREEMPTED: "PREEMPTED", GoalStatus.SUCCEEDED: "SUCCEEDED", GoalStatus.REJECTED: "REJECTED",
          GoalStatus.RECALLED: "RECALLED", GoalStatus.ABORTED: "ABORTED"}


def step_done(state, result):
    if state in states:
        state = states[state]

    print(f"Action has ended with a state {state}. {result.steps_done} steps done. other done = {result.done}")

def step_feedback(feedback):
    print(f"Got feedback {feedback.steps_from_start}")

if __name__ == '__main__':
    rospy.init_node("testing_stepper_lib")

    stop_topic = rospy.Publisher('stop', Bool, queue_size=10)
    speed_factor_topic = rospy.Publisher('speed_factor', Float64, queue_size=10)

    # ==== StepControllerServer
    print("Testing StepControllerServer")
    stepper_object = StepControllerServer(serialNumber, stepper, "step_test", 1/ticsPerStep, "stop", "speed_factor")

    client = actionlib.SimpleActionClient("step_test", StepControllerAction)
    client.wait_for_server()

    print("Server up !")

    # ==== TEST 1
    goal = StepControllerGoal(steps_goal=step_per_rotation, velocity_limit=speed)
    client.send_goal(goal, done_cb=step_done, feedback_cb=step_feedback)

    print(f"stepper should turn during {step_per_rotation / 100} sec and do a complete rotation")

    client.wait_for_result()

    # ==== TEST 2
    print(f"stepper should turn during 0.5s and stop because of the stop_topic. Without the stop_topic it should have turn during {10* step_per_rotation / speed}")

    goal = StepControllerGoal(steps_goal=10*step_per_rotation, velocity_limit=speed)
    client.send_goal(goal, done_cb=step_done, feedback_cb=step_feedback)

    rospy.sleep(.5)
    stop_topic.publish(True)

    client.wait_for_result()

    # ==== TEST 3
    print("stepper should not turn stop_topic")
    goal = StepControllerGoal(steps_goal=step_per_rotation, velocity_limit=speed)
    client.send_goal(goal, done_cb=step_done, feedback_cb=step_feedback)

    rospy.sleep(2.)
    stop_topic.publish(False)

    client.wait_for_result()

    # ==== TEST 4
    print("Test the speed factor")

    print(f"right wheel should turn during {step_per_rotation / speed} sec and do a complete rotation")
    goal = StepControllerGoal(steps_goal=step_per_rotation, velocity_limit=speed)
    client.send_goal(goal, done_cb=step_done, feedback_cb=step_feedback)

    rospy.sleep(step_per_rotation / speed / 3)
    print("speed factor is now 0.5")
    speed_factor_topic.publish(0.5)

    rospy.sleep(step_per_rotation / speed / 3)
    print("speed factor is now 2")
    speed_factor_topic.publish(2)

    client.wait_for_result()
    print("Test instructions are finished.")
