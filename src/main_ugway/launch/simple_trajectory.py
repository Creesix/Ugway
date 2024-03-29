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

    config2 = os.path.join(
      get_package_share_directory('navigation_utils'),
      'config',
      'exampletrajectories.yaml'
    )

    return LaunchDescription([
        Node(
            package='navigation_utils',
            executable='distance_differential_robot_controller',
            name='distance_differential_robot',
            parameters=[config]
        ),
        Node(
            package='navigation_utils',
            executable='trajectory_action_server',
            name='trajectory_handle',
            parameters=[config2]
        ),
        Node(
            package='main_ugway',
            executable='traj_dir_cdrf',
            name='super_test'
        )
    ])