#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image


class ImgReceiver(Node):

    def __init__(self):
        super().__init__('img_receiver')
        self.subscription = self.create_subscription(
            Image,
            'image_raw',
            self.image_callback,
            qos_profile_sensor_data)

    def image_callback(self, data):
        self.get_logger().info('got image!')

        source = self.br.imgmsg_to_cv2(data, 'bgr8')
        edges = cv2.Canny(source, 50, 150)  # 50と150は下限と上限の閾値
        result_msg = self.br.cv2_to_imgmsg(edges, 'passthrough')
        self.publisher.publish(result_msg)
        self.get_logger().info('publish image!')

        pass


def main():
    print("hello")
    rclpy.init()
    img_receiver = ImgReceiver()
    print("start img_receiver node")
    try:
        rclpy.spin(img_receiver)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__=='__main__':
    main()
