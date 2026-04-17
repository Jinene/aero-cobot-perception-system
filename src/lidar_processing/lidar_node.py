import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_node')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.lidar_callback,
            10
        )

    def lidar_callback(self, msg):
        valid_ranges = [r for r in msg.ranges if r > 0]
        if valid_ranges:
            min_distance = min(valid_ranges)
            self.get_logger().info(f"Closest obstacle: {min_distance:.2f} m")

def main(args=None):
    rclpy.init(args=args)
    node = LidarNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
