import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import pigpio
import yaml
import os

class DigitalWriter(Node):

    def __init__(self, pin):
        super().__init__('gpio_subscriber_' + str(pin))
        self.pin = pin
        self.get_logger().info(f'Write GPIO-{self.pin:02d}')

        try:
            self.pi = pigpio.pi()
            if self.pi.connected:
                self.pi.set_mode(self.pin, pigpio.OUTPUT)
                topic_name = f'gpio_output_{self.pin:02d}'
                self.subscription = self.create_subscription(
                    Bool, topic_name, self.topic_callback, 10)
            else:
                self.get_logger().error('Cannot connect pigpiod')
                rclpy.shutdown()
                exit(1)
        except Exception as e:
            self.get_logger().error(f'Error: {e}')
            rclpy.shutdown()
            exit(1)

    def topic_callback(self, msg):
        self.pi.write(self.pin, msg.data)
        self.get_logger().info(f'Write {msg.data} on GPIO-{self.pin}')

    def __del__(self):
        self.pi.set_mode(self.pin, pigpio.INPUT)
        self.pi.stop()


def load_config_from_yaml():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(script_dir, '..', 'config', 'config_writer.yaml')

    with open(yaml_file_path, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)

    return config.get('pin_list', [])


def main(args=None):
    rclpy.init(args=args)

    pin_list = load_config_from_yaml()

    digital_writers = [DigitalWriter(pin) for pin in pin_list]

    rclpy.spin(digital_writers)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
