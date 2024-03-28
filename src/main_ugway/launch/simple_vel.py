import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    config = os.path.join(
      get_package_share_directory('navigation_utils'),
      'config',
      'defaultparams.yaml'
    )

    return LaunchDescription([
        Node(
            package='navigation_utils',
            executable='cmd_vel_differential_robot_subscriber',
            name='cmd_vel_subscriber',
            parameters=[config]
        ),
        Node(
            package='main_ugway',
            executable='cmd_vel_cdrf',
            name='super_test'
        )
        Node(
            package='lidar_vl53l1x_processing',
            executable='lidar_ensea',
            name='super_lidar'
        )
    ])