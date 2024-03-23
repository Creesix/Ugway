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


def load_config_from_yaml():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(script_dir, '..', 'config', 'config_reader.yaml')

    with open(yaml_file_path, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)

    return config.get('pin_list', [])


def main(args=None):
    rclpy.init(args=args)

    pin_configs = load_config_from_yaml()

    digital_readers = [DigitalReader(pin['pin'], pin['is_pull_up']) for pin in pin_configs]

    rclpy.spin(digital_readers)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
