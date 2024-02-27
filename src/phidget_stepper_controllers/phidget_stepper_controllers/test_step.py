#!/usr/bin/env python3
import rclpy
import time
from rclpy.action import ActionClient
from rclpy.node import Node

from phidget_stepper_controllers_msgs.action import StepController
from phidget_stepper_controllers.step_controller_server import StepControllerServer

## Verification du StepControllerGoal ##

from std_msgs.msg import Float64, Bool

def step_feedback(feedback):
    print(f"Got feedback {feedback.steps_from_start}")

class SimpleActionClient(Node):
    def __init__(self):
        super().__init__('simple_action_client')

        #Declare parameter
        self.declare_parameter('stepper', 3)
        self.declare_parameter('hub', 723793)
        self.declare_parameter('ticsPerStep', 32)
        self.declare_parameter('pasStepper', 1.8)
        
        #Get parameter
        stepper = self.get_parameter('stepper').get_parameter_value().integer_value
        serialNumber = self.get_parameter('hub').get_parameter_value().integer_value
        ticsPerStep = self.get_parameter('ticsPerStep').get_parameter_value().integer_value
        step_per_rotation = 360/self.get_parameter('pasStepper').get_parameter_value().double_value

        self.get_logger().info('Creating step_test action server')
        self.stepper_object = StepControllerServer(self, serialNumber, stepper, "speed_test", 1 / ticsPerStep, "stop", "speed_factor")

        self.get_logger().info('Creating step_test action client')
        self._action_client = ActionClient(self, StepController, 'speed_test')

    def send_goal(self, vel, step):
        self.get_logger().info('Creating step_test goal')

        self.get_logger().info(f"step_per_rotation will be round of {step - int(step)}")
        step = int(step)

        goal_msg = StepController.Goal()
        goal_msg.velocity_limit = vel
        goal_msg.steps_goal = step

        self.get_logger().info('Wainting step_test action')
        self._action_client.wait_for_server()

        self.get_logger().info('Sending goal to step_test')
        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = SimpleActionClient()

    stop_topic = action_client.create_publisher(Bool, 'stop', 10)
    speed_factor_topic = action_client.create_publisher(Float64, 'speed_factor', 10)

    step_per_rotation = 360/action_client.get_parameter('pasStepper').get_parameter_value().double_value
    
    speed = 600

    # ==== TEST 1
    future = action_client.send_goal(speed, 1000)
    action_client.get_logger().info(f"stepper should turn at {step_per_rotation / speed} sec / revolution and do a complete rotation")
    rclpy.spin_until_future_complete(action_client, future)

    time.sleep(5)

    # ==== TEST 2
    action_client.get_logger().info(
        f"stepper should turn at {step_per_rotation / speed} sec / revolution and stop because of the stop_topic in 0,5s.")
    future = action_client.send_goal(speed, 1000)
    rclpy.spin_until_future_complete(action_client, future)


    
    time.sleep(1)
    speed_factor_msg = Float64()
    speed_factor_msg.data = 1.5
    speed_factor_topic.publish(speed_factor_msg)

    action_client.get_logger().info(f"Stepper here")

    rclpy.spin(action_client)
    
    action_client.get_logger().info(f"Stepper not here")
    
    rclpy.shutdown()
  
if __name__ == '__main__':
	main()