import serial
import serial.tools.list_ports
import RPi.GPIO as GPIO
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from start_robot_interface.srv import StrategyInt

class StartClient(Node):

    def __init__(self):
        super().__init__('start_client')
        self.srv_client = self.create_client(StrategyInt, 'start')     
        while not self.srv_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        self.req = StrategyInt.Request()
        self.stop_publisher = self.create_publisher(Bool, 'stop', 10)

    def send_request(self, strategy):
        self.req.strategy = strategy
        self.future = self.srv_client.call_async(self.req)

# Recherche du port USB lié à l'écran
def find_screen_port():
    stlink_ports = [port.device for port in serial.tools.list_ports.comports() if "ST-Link" in port.description]
    if stlink_ports:
        return stlink_ports[0]
    else:
        return None

def main(args=None):
    rclpy.init(args=args)
    start_client = StartClient()
    
    # Connexion série
    port = find_screen_port() 
    baudrate = 115200  
    timeout = 1

    # Broche de la tirette
    start_pin = 26

    if port:
        ser = serial.Serial(port, baudrate, timeout=timeout)
    else: 
        start_client.get_logger().info("No screen device found on target !")
        exit()
    
    # Lecture de la stratégie
    while True:
        received_data = ser.readline().decode().strip()
        if len(received_data) != 0:
            strategy = int(received_data)
            break

    ser.close()
    
    # Initialisation de la tirette
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(start_pin, GPIO.IN)
    previous_state = GPIO.input(start_pin)

    while True:
        current_state = GPIO.input(start_pin)
        
        if current_state != previous_state:
            start_client.send_request(strategy)
            
            # Durée d'un match
            time.sleep(89)
            msg = Bool()
            msg.data = True
            start_client.get_logger().info("Match timeout !")
            start_client.stop_publisher.publish(msg)
            break
        
        time.sleep(0.01)

    GPIO.cleanup()
    rclpy.spin_once(start_client)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

