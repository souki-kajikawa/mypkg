#!/bin/bash
dir=/root
cd $dir/ros2_ws
rm -rf build/ install/ log/
colcon build
source /opt/ros/humble/setup.bash
source install/local_setup.bash
timeout 60 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1

cat /tmp/mypkg.log | grep 'Listen: 10'
