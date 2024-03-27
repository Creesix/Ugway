import rclpy
import time
from rclpy.node import Node

from geometry_msgs.msg import Twist



class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 1)
        
        self.get_logger().info('Publisher: READY')

        time.sleep(5)

        self.publish_callback()

    def publish_callback(self):
        msg = Twist()

        # Setting linear and angular velocities
        msg.linear.x = 0.8
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')

        time.sleep(5)

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
        
        time.sleep(5)

        # Setting linear and angular velocities
        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.4

        self.publisher_.publish(msg)

        # Logging the published message's details
        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')
        
        time.sleep(5)

        # Setting linear and angular velocities
        msg.linear.x = -0.8
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        self.publisher_.publish(msg)

        self.get_logger().info(f'Publishing linear: {msg.linear.x}, {msg.linear.y}, {msg.linear.z}; angular: {msg.angular.x}, {msg.angular.y}, {msg.angular.z}')

        time.sleep(5)

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

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()