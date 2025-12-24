import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def main():
    rclpy.init()
    node = Node("talker")
    pub = node.create_publisher(Int16, "countup", 10)
    n = 0

    def timer_callback():
        nonlocal n
        msg = Int16()
        msg.data = n
        pub.publish(msg)
        n += 1

    node.create_timer(0.5, timer_callback)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
