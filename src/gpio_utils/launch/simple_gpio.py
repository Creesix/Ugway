import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    config = os.path.join(
      get_package_share_directory('gpio_utils'),
      'config',
      'configreader.yaml'
    )

    return LaunchDescription([
        Node(
            package='gpio_utils',
            executable='gpio_reader_test',
            name='test_gpio_hugway',
            parameters=[config]
        )
    ])