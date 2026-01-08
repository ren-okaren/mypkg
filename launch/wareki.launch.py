# SPDX-FileCopyrightText: 2025 Ren
# SPDX-License-Identifier: MIT

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    year = LaunchConfiguration('year')

    return LaunchDescription(
        [
            DeclareLaunchArgument('year', default_value='2004'),
            Node(package='mypkg', executable='wareki_converter', output='screen'),
            Node(
                package='mypkg',
                executable='year_pub',
                parameters=[{'year': year}],
                output='screen',
            ),
        ]
    )
