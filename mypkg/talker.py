# SPDX-FileCopyrightText: 2025 Souki Kajikawa
# SPDX-License-Identifier: BSD-3-Clause

import psutil
import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import UInt64

rclpy.init()
node = Node("talker")
pub = node.create_publisher(UInt64, "receive", 10)



def cd():
    n = 0
    rec0 = psutil.net_io_counters().bytes_recv
    time.sleep(2.9)
    rec1 = psutil.net_io_counters().bytes_recv
    n = rec1 - rec0
    msg = UInt64()
    msg.data = n
    pub.publish(msg)


def main():
    node.create_timer(0.1, cd)
    rclpy.spin(node)
