# SPDX-FileCopyrightText: 2025 Ren
# SPDX-License-Identifier: MIT

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

def to_wareki(year: int) -> str:
    # NOTE: 「年内の改元日」は考慮せず、西暦年だけで判定する（仕様としてREADMEに明記）
    if year >= 2019:
        return f"令和{year - 2018}年"
    if year >= 1989:
        return f"平成{year - 1988}年"
    if year >= 1926:
        return f"昭和{year - 1925}年"
    if year >= 1912:
        return f"大正{year - 1911}年"
    if year >= 1868:
        return f"明治{year - 1867}年"
    return "対応外"

class WarekiConverter(Node):
    def __init__(self):
        super().__init__("wareki_converter")
        self.sub = self.create_subscription(Int32, "year", self.cb, 10)

    def cb(self, msg: Int32):
        y = int(msg.data)
        w = to_wareki(y)
        self.get_logger().info(f"year={y} -> {w}")

def main():
    rclpy.init()
    node = WarekiConverter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
