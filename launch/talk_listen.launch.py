import launch
import launch.actions
<<<<<<< HEAD
import launch.substitution
=======
import launch.substitutions
>>>>>>> lesson10
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
            package='mypkg',
            executable='talker',
            )
    listener = launch_ros.actions.Node(
<<<<<<< HEAD
            package='mypkg',
            executable='listener',
=======
            package='mypkg'
            executable='listener'
>>>>>>> lesson10
            output='screen'
            )
    return launch.LaunchDescription([talker, listener])
