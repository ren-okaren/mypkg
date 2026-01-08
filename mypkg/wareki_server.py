from mypkg_interfaces.srv import AdTowareki

import rclpy
from rclpy.node import Node


def ad_to_wareki(year: int) -> str:
    """Convert AD year to Japanese era."""
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
    return "対象外"


class WarekiServer(Node):

    def __init__(self) -> None:
        super().__init__('wareki_server')
        self.srv = self.create_service(AdTowareki, 'ad_to_wareki', self.cb)
        self.get_logger().info('service /ad_to_wareki ready')

    def cb(self, req, res):
        res.wareki = ad_to_wareki(req.ad_year)
        self.get_logger().info(f'req: {req.ad_year} -> {res.wareki}')
        return res


def main() -> None:
    rclpy.init()
    node = WarekiServer()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
