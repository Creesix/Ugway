#!/usr/bin/env python3
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
import asyncio

from phidget_stepper_controllers_msgs.action import SpeedController
from phidget_stepper_controllers.speed_controller_server import SpeedControllerServer


from std_msgs.msg import Float64, Bool

def speed_done(result):


    print(f"Action has ended. done = {result.done}")

def speed_feedback( feedback):
    print(f"Got feedback observed_velocity : {feedback.observed_velocity} theoretical_velocity : {feedback.theoretical_velocity}")

    
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


        # node.get_logger().info('Created node')

        stop_topic = self.create_publisher(Bool, 'stop', 10)
        speed_factor_topic = self.create_publisher(Float64, 'speed_factor', 10)

        # ==== SpeedControllerServer
        self.get_logger().info("Testing SpeedControllerServer")
        stepper_right = SpeedControllerServer(self, serialNumber, stepper, "speed_test", 1 / ticsPerStep, "stop", "speed_factor")

        client = ActionClient(self, SpeedController, "speed_test")
        client.wait_for_server()

        self.get_logger().info("Server up !")

        # ==== TEST 1
        goal = SpeedController.Goal()
        goal.velocity_limit = speed

        self.get_logger().info(f"stepper should turn at {step_per_rotation / 100} sec / revolution and do a complete rotation")
        result = client.send_goal(goal, feedback_callback=speed_feedback)
        speed_done(result)

        self.create_rate(5).sleep()

        self.get_logger().info(f"stopping the stepper")
        goal = SpeedController.Goal()
        goal.velocity_limit = 0
        # On est en synchrone le rsult sera dans tous les cas envoyé sur le fronts montants
        result = client.send_goal(goal, feedback_callback=speed_feedback)
        speed_done(result)

        # ==== TEST 2
        self.get_logger().info(
            f"stepper should turn at {step_per_rotation / 100} sec / revolution and stop because of the stop_topic in 0,1s.")

        goal = SpeedController.Goal()
        goal.velocity_limit = speed

        # On est en asynchrone le result donnera rien. Tu y vas j'attends pas la réponse
        client.send_goal_async(goal, feedback_callback=speed_feedback)

        self.create_rate(.1).sleep()
        stop_topic.publish(True)

        #Ici par contre je vien rechercher le résultat et j'attends qu'il me le donne 
        result = client.get_result()
        speed_done(result)

        # ==== TEST 3
        self.get_logger().info("stepper should not turn stop_topic")
        goal = SpeedController.Goal()
        goal.velocity_limit = speed
        client.send_goal_async(goal, feedback_callback=speed_feedback)

        self.create_rate(2).sleep()
        stop_topic.publish(False)

        #Ici par contre je vien rechercher le résultat et j'attends qu'il me le donne 
        result = client.get_result()
        speed_done(result)

        # ==== TEST 4
        self.get_logger().info("Test the speed factor")

        self.get_logger().info(f"stepper should turn during {step_per_rotation / 100} sec and do a complete rotation")
        goal = SpeedController.Goal()
        goal.velocity_limit = speed
        future = client.send_goal_async(goal, feedback_callback=speed_feedback)

        self.create_rate(step_per_rotation / speed / 3).sleep()
        self.get_logger().info("speed factor is now 0.5")
        speed_factor_topic.publish(0.5)

        self.create_rate(step_per_rotation / speed / 3).sleep()
        self.get_logger().info("speed factor is now 2")
        speed_factor_topic.publish(2)

        self.get_logger().info("Test instructions are finished.")

        return future

    
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
