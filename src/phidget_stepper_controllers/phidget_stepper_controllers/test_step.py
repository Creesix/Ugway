#!/usr/bin/env python3
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from phidget_stepper_controllers.msg import StepControllerAction, StepControllerGoal
from phidget_stepper_controllers.step_controller_server import StepControllerServer

## Verification du StepControllerGoal ##

from std_msgs.msg import Float64, Bool

def step_feedback(feedback):
    print(f"Got feedback {feedback.steps_from_start}")

class TestNode(Node):
  def __init__(self):
      super().__init__('testing_stepper_lib')

  def run(self):
        #Declare parameter
        stepper = self.declare_parameter('stepper', 0).value
        serialNumber = self.declare_parameter('hub', 723793).value
        ticsPerStep = self.declare_parameter('ticsPerStep', 32).value
        step_per_rotation = 360/self.declare_parameter('pasStepper', 1.8).value

        speed = 100.

        if step_per_rotation != int(step_per_rotation):
            self.get_logger().info(f"step_per_rotation will be round of {step_per_rotation - int(step_per_rotation)}")
            step_per_rotation = int(step_per_rotation)

        self.get_logger().info('Created node')

        stop_topic = self.create_publisher(Bool, 'stop', 10)
        speed_factor_topic = self.create_publisher(Float64, 'speed_factor', 10)

        # ==== SpeedControllerServer
        self.get_logger().info("Testing SpeedControllerServer")
        stepper_right = StepControllerServer(self, serialNumber, stepper, "step_test", 1 / ticsPerStep, "stop", "speed_factor")

        client = ActionClient(self, StepControllerAction, "step_test")
        client.wait_for_server()

        self.get_logger().info("Server up !")

         # ==== TEST 1
        goal = StepControllerGoal(steps_goal=step_per_rotation, velocity_limit=speed)
        client.send_goal(goal, feedback_callback=step_feedback)

        self.get_logger().info(f"stepper should turn during {step_per_rotation / 100} sec and do a complete rotation")

        client.wait_for_result()

        # ==== TEST 2
        self.get_logger().info(f"stepper should turn during 0.5s and stop because of the stop_topic. Without the stop_topic it should have turn during {10* step_per_rotation / speed}")

        goal = StepControllerGoal(steps_goal=10*step_per_rotation, velocity_limit=speed)
        client.send_goal(goal, feedback_callback=step_feedback)

        self.create_rate(.5).sleep()
        stop_topic.publish(True)

        client.wait_for_result()

        # ==== TEST 3
        self.get_logger().info("stepper should not turn stop_topic")
        goal = StepControllerGoal(steps_goal=step_per_rotation, velocity_limit=speed)
        client.send_goal(goal, feedback_callback=step_feedback)

        self.create_rate(.2).sleep()
        stop_topic.publish(False)

        client.wait_for_result()

        # ==== TEST 4
        self.get_logger().info("Test the speed factor")

        self.get_logger().info(f"right wheel should turn during {step_per_rotation / speed} sec and do a complete rotation")
        goal = StepControllerGoal(steps_goal=step_per_rotation, velocity_limit=speed)
        client.send_goal(goal, feedback_callback=step_feedback)

        self.create_rate(step_per_rotation / speed / 3).sleep()
        self.get_logger().info("speed factor is now 0.5")
        speed_factor_topic.publish(0.5)

        self.create_rate(step_per_rotation / speed / 3).sleep()
        self.get_logger().info("speed factor is now 2")
        speed_factor_topic.publish(2)

        client.wait_for_result()
        self.get_logger().info("Test instructions are finished.")

def main():
    rclpy.init()

    #Création de la node 
    node = TestNode()

    #On cherche le future qu'on veut avoir et on wait ce future
    future = node.run()
    rclpy.spin_until_future_complete(node, future)

    #On kill tout histoire que ca soit tout propre
    node.destroy_node()
    rclpy.shutdown()
  
  
if __name__ == '__main__':
	main()