import os

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Declare the path to config file as a launch argument with a default
    config_file_path = LaunchConfiguration("config_file")
    config_file_arg = DeclareLaunchArgument(
        "config_file",
        default_value=os.path.join(
            get_package_share_directory("charuco_detector"),
            "config/camera_calibration/camera_calibration.yaml",
        ),
        description="Path to camera calibration YAML file",
    )

    ros_param_file_path = LaunchConfiguration("ros_param_file")
    ros_param_file_arg = DeclareLaunchArgument(
        "ros_param_file",
        default_value=os.path.join(
            get_package_share_directory("charuco_detector"), "config/ros.yaml"
        ),
        description="Path to file with ROS related config",
    )

    charuco_file_path = LaunchConfiguration("charuco_param_file")
    charuco_param_file_arg = DeclareLaunchArgument(
        "charuco_param_file",
        default_value=os.path.join(
            get_package_share_directory("charuco_detector"), "yaml/charuco.yaml"
        ),
        description="Path to file with charuco related config",
    )

    # Declare additional parameters
    image_topic = LaunchConfiguration("image_topic")
    camera_info_topic = LaunchConfiguration("camera_info_topic")
    use_calibration_file = LaunchConfiguration("use_calibration_file")
    calibration_file = LaunchConfiguration("calibration_file")

    # Create launch arguments for each parameter
    image_topic_arg = DeclareLaunchArgument(
        "image_topic",
        default_value="/camera/color/image_raw",
        description="Topic for camera images",
    )

    camera_info_topic_arg = DeclareLaunchArgument(
        "camera_info_topic",
        default_value="/camera/color/camera_info",
        description="Topic for camera info",
    )

    use_calibration_file_arg = DeclareLaunchArgument(
        "use_calibration_file",
        default_value="false",
        description="Whether to use a calibration file",
    )

    calibration_file_arg = DeclareLaunchArgument(
        "calibration_file",
        default_value=os.path.join(
            get_package_share_directory("charuco_detector"),
            "config/camera_calibration/camera_calibration.yaml",
        ),
        description="Path to camera calibration file",
    )

    charuco_node = Node(
        package="charuco_detector",
        executable="charuco_detector_node",
        name="charuco_detector",
        output="screen",
        parameters=[
            config_file_path,
            ros_param_file_path,
            charuco_file_path,
            {
                "image_topic": image_topic,
                "camera_info_topic": camera_info_topic,
                "use_calibration_file": use_calibration_file,
                "calibration_file": calibration_file,
            },
        ],
    )

    return LaunchDescription(
        [
            config_file_arg,
            ros_param_file_arg,
            charuco_param_file_arg,
            image_topic_arg,
            camera_info_topic_arg,
            use_calibration_file_arg,
            calibration_file_arg,
            charuco_node,
        ]
    )
