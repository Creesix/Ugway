import serial
import serial.tools.list_ports
import RPi.GPIO as GPIO
import time
import rclpy
from rclpy.node import Node
from start_robot_interface.srv import StrategyInt

class StartClient(Node):

    def __init__(self):
        super().__init__('start_client')
        self.srv_client = self.create_client(StrategyInt, 'start_cli')     
        while not self.srv_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = StrategyInt.Request()

    def send_request(self, strategy):
        self.req.strategy = strategy
        self.future = self.srv_client.call_async(self.req)

def find_screen_port():
    stlink_ports = [port.device for port in serial.tools.list_ports.comports() if "ST-Link" in port.description]
    if stlink_ports:
        return stlink_ports[0]
    else:
        return None

def main(args=None):
    rclpy.init(args=args)
    start_client = StartClient()

    port = find_screen_port() 
    baudrate = 115200  
    timeout = 1
    start_pin = 26

    if port:
        ser = serial.Serial(port, baudrate, timeout=timeout)
    else: 
        minimal_client.get_logger().info("No screen device found on target !")
        exit()

    while True:
        received_data = ser.readline().decode().strip()
        if len(received_data) != 0:
            strategy = received_data
            break

    ser.close()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(start_pin, GPIO.IN)
    previous_state = GPIO.input(start_pin)

    while True:
        current_state = GPIO.input(start_pin)
        
        if current_state != previous_state:
            start_client.send_request(strategy)
            time.sleep(3)
            minimal_client.get_logger().info("Match timeout !")
            break
        
        time.sleep(0.1)

    GPIO.cleanup()
    rclpy.spin_once(start_client)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

