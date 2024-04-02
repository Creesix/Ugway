from start_robot_interface.srv import StrategyInt                                                          
import rclpy
import time
from rclpy.node import Node

from geometry_msgs.msg import Twist

class StartService(Node):

    def __init__(self):
        super().__init__('start_service')
        self.srv = self.create_service(StrategyInt, 'start', self.strategy_callback)   

        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 1)
        
        self.get_logger().info('Publisher: READY')

        time.sleep(3)

        self.publish_callback()   
    
    # Récupération de la stratégie
    def strategy_callback(self, request, response):
        response.strategy = request.strategy                                          
        self.get_logger().info('Incoming strategy: %d' % (request.strategy))  

        return response

    def publish_callback(self):
        msg = Twist()

        # Setting linear and angular velocities
        msg.linear.x = 2.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')

        time.sleep(3.2)

        # Setting linear and angular velocities
        msg.linear.x = 1.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.05

        self.publisher_.publish(msg)

        # Logging the published message's details
        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')
        
        time.sleep(1.5)

        # Setting linear and angular velocities
        msg.linear.x = 3.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher_.publish(msg)

        # Logging the published message's details
        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')
        
        time.sleep(3)

        # Setting linear and angular velocities
        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')

        time.sleep(4)

        # Setting linear and angular velocities
        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.05

        self.publisher_.publish(msg)

        # Logging the published message's details
        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')
        
        time.sleep(1.5)
        
        # Setting linear and angular velocities
        msg.linear.x = -2.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = -0.5

        self.publisher_.publish(msg)

        time.sleep(3.5)

        # Logging the published message's details
        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')
        
        # Setting linear and angular velocities
        msg.linear.x = -2.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = -0.0

        self.publisher_.publish(msg)

        # Logging the published message's details
        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')
        
        time.sleep(2)

        # Setting linear and angular velocities
        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher_.publish(msg)

        # Logging the published message's details
        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')
        

def main(args=None):

    rclpy.init(args=args)
    start_service = StartService()
    rclpy.spin(start_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
