import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import pigpio
import yaml
import os

class PWMWriter(Node):

    def __init__(self, pin):
        super().__init__('gpio_pwm_subscriber_' + str(pin))
        self.pin = pin
        self.pi = None

        try:
            self.pi = pigpio.pi()
            if self.pi.connected:
                self.pi.set_mode(self.pin, pigpio.OUTPUT)
                topic_name = f'gpio_pwm_{self.pin:02d}'
                self.subscription = self.create_subscription(Int16, topic_name, self.topic_callback, 10)
            else:
                self.get_logger().error('Cannot connect pigpiod')
                rclpy.shutdown()
                exit(1)
        except Exception as e:
            self.get_logger().error(f'Error: {e}')
            rclpy.shutdown()
            exit(1)

    def topic_callback(self, msg):
        duty_cycle = msg.data
        self.pi.set_PWM_dutycycle(self.pin, duty_cycle)
        self.get_logger().info(f'Write {duty_cycle:03d} on GPIO-{self.pin}')

    def __del__(self):
        if self.pi:
            self.pi.set_mode(self.pin, pigpio.INPUT)
            self.pi.stop()


def load_pwm_config_from_yaml():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_file_path = os.path.join(script_dir, '..', 'config', 'config_pwm.yaml')

    with open(yaml_file_path, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)

    return config.get('pwm_pins', [])


def main(args=None):
    rclpy.init(args=args)

    pwm_pin_configs = load_pwm_config_from_yaml()

    pwm_writers = [PWMWriter(pin['pin']) for pin in pwm_pin_configs]

    rclpy.spin(pwm_writers)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
