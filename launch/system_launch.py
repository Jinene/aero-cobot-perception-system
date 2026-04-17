from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lidar_processing',
            executable='lidar_node',
            name='lidar_node'
        ),
        Node(
            package='vision_2d',
            executable='camera_2d',
            name='camera_2d'
        ),
        Node(
            package='vision_3d',
            executable='camera_3d',
            name='camera_3d'
        ),
    ])
