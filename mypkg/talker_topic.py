import rclpy
from rclpy.node import Node
from ren_msgs.msg import Person


def main():
    rclpy.init()
    node = Node("talker")
    pub = node.create_publisher(Person, "person", 10)

    i = 0

    def cb():
        nonlocal i
        msg = Person()
        msg.name = "ren"
        msg.age = i
        node.get_logger().info("Talk: %s %s" % (msg.name, msg.age))
        pub.publish(msg)
        i = (i + 1) % 256

    node.create_timer(0.5, cb)
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
