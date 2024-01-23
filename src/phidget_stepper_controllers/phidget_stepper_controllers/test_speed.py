import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from phidget_stepper_controllers_msgs.action import SpeedController
from phidget_stepper_controllers.speed_controller_server import SpeedControllerServer

class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        
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
        
        self.get_logger().info('Creating speed_test action server')
        self.stepper_object = SpeedControllerServer(self, serialNumber, stepper, "speed_test", 1 / ticsPerStep, "stop", "speed_factor")

        self.get_logger().info('Creating speed_test action client')
        self._action_client = ActionClient(self, SpeedController, 'speed_test')

    def send_goal(self, vel):
        self.get_logger().info('Creating speed_test goal')
        goal_msg = SpeedController.Goal()
        goal_msg.velocity_limit = vel

        self.get_logger().info('Wainting speed_test action')
        self._action_client.wait_for_server()

        self.get_logger().info('Sending goal to speed_test')
        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = FibonacciActionClient()

    future = action_client.send_goal(1)

    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()