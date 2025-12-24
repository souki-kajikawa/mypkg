import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def main():
    rclpy.init()
    node = Node("listener")

    def cb(msg):
        print(f"Listen: {msg.data}")
        node.get_logger().info(f"Listen: {msg.data}")

    node.create_subscription(Int16, "countup", cb, 10)
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
