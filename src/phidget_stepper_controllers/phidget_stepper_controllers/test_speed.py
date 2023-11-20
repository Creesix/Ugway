#!/usr/bin/env python3
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from phidget_stepper_controllers_msgs.action import SpeedController
from phidget_stepper_controllers.speed_controller_server import SpeedControllerServer


from actionlib_msgs.msg import GoalStatus
from std_msgs.msg import Float64, Bool


states = {GoalStatus.PREEMPTED: "PREEMPTED", GoalStatus.SUCCEEDED: "SUCCEEDED", GoalStatus.REJECTED: "REJECTED",
          GoalStatus.RECALLED: "RECALLED", GoalStatus.ABORTED: "ABORTED"}

def speed_done(state, result):
    if state in states:
        state = states[state]

    print(f"Action has ended with a state {state}. done = {result.done}")

def speed_feedback(feedback):
    print(f"Got feedback observed_velocity : {feedback.observed_velocity} theoretical_velocity : {feedback.theoretical_velocity}")

def main():
    rclpy.init()
    node = rclpy.create_node('testing_stepper_lib')

    #Declare parameter
    stepper = node.declare_parameter('stepper', 4).value
    serialNumber = node.declare_parameter('hub', 627520).value
    ticsPerStep = node.declare_parameter('ticsPerStep', 32).value
    step_per_rotation = 360/node.declare_parameter('pasStepper', 1.8).value


    speed = 100

    if step_per_rotation != int(step_per_rotation):
        print(f"step_per_rotation will be round of {step_per_rotation - int(step_per_rotation)}")
        step_per_rotation = int(step_per_rotation)


    # node.get_logger().info('Created node')


    stop_topic = node.create_publisher(Bool, 'stop', 10)
    speed_factor_topic = node.create_publisher(Float64, 'speed_factor', 10)

    # ==== SpeedControllerServer
    print("Testing SpeedControllerServer")
    stepper_right = SpeedControllerServer(node, serialNumber, stepper, "speed_test", 1 / ticsPerStep, "stop", "speed_factor")

    client = ActionClient(node, SpeedController, "step_test")
    client.wait_for_server()

    print("Server up !")

    # ==== TEST 1
    goal = SpeedController.Goal()
    goal.velocity_limit = speed
    client.send_goal(goal, done_cb=speed_done, feedback_cb=speed_feedback)

    print(f"stepper should turn at {step_per_rotation / 100} sec / revolution and do a complete rotation")

    client.wait_for_result()
    node.create_rate(5).sleep()

    print(f"stopping the stepper")
    goal = SpeedController.Goal()
    goal.velocity_limit = 0
    client.send_goal(goal, done_cb=speed_done, feedback_cb=speed_feedback)
    client.wait_for_result()

    # ==== TEST 2
    print(
        f"stepper should turn at {step_per_rotation / 100} sec / revolution and stop because of the stop_topic in 0,1s.")

    goal = SpeedController.Goal()
    goal.velocity_limit = speed
    client.send_goal(goal, done_cb=speed_done, feedback_cb=speed_feedback)

    node.create_rate(.1).sleep()
    stop_topic.publish(True)

    client.wait_for_result()

    # ==== TEST 3
    print("stepper should not turn stop_topic")
    goal = SpeedController.Goal()
    goal.velocity_limit = speed
    client.send_goal(goal, done_cb=speed_done, feedback_cb=speed_feedback)

    node.create_rate(2).sleep()
    stop_topic.publish(False)

    client.wait_for_result()

    # ==== TEST 4
    print("Test the speed factor")

    print(f"stepper should turn during {step_per_rotation / 100} sec and do a complete rotation")
    goal = SpeedController.Goal()
    goal.velocity_limit = speed
    client.send_goal(goal, done_cb=speed_done, feedback_cb=speed_feedback)

    node.create_rate(step_per_rotation / speed / 3).sleep()
    print("speed factor is now 0.5")
    speed_factor_topic.publish(0.5)

    node.create_rate(step_per_rotation / speed / 3).sleep()
    print("speed factor is now 2")
    speed_factor_topic.publish(2)

    client.wait_for_result()

    print("Test instructions are finished.")

if __name__ == '__main__':

    main()
