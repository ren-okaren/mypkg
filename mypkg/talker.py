import rclpy
from rclpy.node import Node
from ren_msgs.srv import Query


def cb(request, response):
    if request.name == "ren":
        response.age = 20
    else:
        response.age = 255
    return response


def main():
    rclpy.init()
    node = Node("talker")

    node.create_service(Query, "query", cb)
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
