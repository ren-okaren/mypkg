import rclpy
from rclpy.node import Node
from ren_msgs.msg import Person


def cb(msg):
    node.get_logger().info("Listen: %s" % msg)


def main():
    rclpy.init()
    global node
    node = Node("listener")

    node.create_subscription(Person, "person", cb, 10)
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
