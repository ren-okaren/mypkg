# SPDX-FileCopyrightText: 2025 Ren
# SPDX-License-Identifier: MIT

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class YearPub(Node):

    def __init__(self):
        super().__init__("year_pub")
        self.declare_parameter("year", 2004)
        self.pub = self.create_publisher(Int32, "year", 10)
        self.timer = self.create_timer(0.2, self.tick)
        self.count = 0

    def tick(self):
        year = int(self.get_parameter("year").value)
        msg = Int32()
        msg.data = year
        self.pub.publish(msg)
        self.count += 1
        if self.count >= 3:
            rclpy.shutdown()


def main():
    rclpy.init()
    node = YearPub()
    rclpy.spin(node)


if __name__ == "__main__":
    main()
