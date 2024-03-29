import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import pigpio
import yaml
import os

class DigitalReader(Node):

    def __init__(self, pin, is_pull_up):
        super().__init__('gpio_publisher_' + str(pin))

        self.pin = pin
        self.is_pull_up = is_pull_up

        if self.is_pull_up:
            self.get_logger().info(f'Read GPIO-{self.pin:02d} (PULL_UP)')
        else:
            self.get_logger().info(f'Read GPIO-{self.pin:02d} (PULL_DOWN)')

        try:
            self.pi = pigpio.pi()
            if self.pi.connected:
                self.pi.set_mode(self.pin, pigpio.INPUT)
                if self.is_pull_up:
                    self.pi.set_pull_up_down(self.pin, pigpio.PUD_UP)
                else:
                    self.pi.set_pull_up_down(self.pin, pigpio.PUD_OFF)

                topic_name = f'gpio_input_{self.pin:02d}'
                self.publisher = self.create_publisher(Bool, topic_name, 10)
                self.timer = self.create_timer(0.5, self.timer_callback)
            else:
                self.get_logger().error('Cannot connect pigpiod')
                rclpy.shutdown()
                exit(1)
        except Exception as e:
            self.get_logger().error(f'Error: {e}')
            rclpy.shutdown()
            exit(1)

    def timer_callback(self):
        message = Bool()
        message.data = self.pi.read(self.pin)
        self.get_logger().info(f'Publishing: "{message.data}" on GPIO-{self.pin:02d}')
        self.publisher.publish(message)

    def __del__(self):
        self.pi.stop()

class DigitalPinManager(Node):
    def __init__(self):
        super().__init__('my_pin_manager_node')

        self.declare_parameter('pin_list', [])
        pin_configs = self.get_parameter('pin_list').get_parameter_value().string_array_value

        self.digital_pin_managers = [
            DigitalReader(pin['pin'], pin['is_pull_up']) for pin in pin_configs
        ]


def main(args=None):
    rclpy.init(args=args)

    gpio_reader = DigitalPinManager()

    rclpy.spin(gpio_reader)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    gpio_reader.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
