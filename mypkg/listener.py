# SPDX-FileCopyrightText: 2025 Souki Kajikawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt64

rclpy.init()
node = Node("listener")

def cd(msg):
    global node
    node.get_logger().info("receive: %d" % msg.data)


def main():
    pub = node.create_subscription(UInt64, "receive", cd, 10)
    rclpy.spin(node)
