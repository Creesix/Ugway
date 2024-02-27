import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    config = os.path.join(
      get_package_share_directory('phidget_stepper_controllers'),
      'config',
      'tests.yaml'
    )

    return LaunchDescription([
        Node(
            package='phidget_stepper_controllers',
            executable='test_speed',
            name='testing_stepper_lib',
            parameters=[config]
        ),
    ])