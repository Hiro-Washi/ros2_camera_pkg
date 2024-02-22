#!/usr/bin/env python3

# 


import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ImageSubscriber(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.listener_callback,
            10)
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        # ROS画像メッセージをOpenCV形式に変換
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # 画像を表示
        cv2.imshow("Image Window", cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    subscriber = ImageSubscriber()
    rclpy.spin(subscriber)
    # ウィンドウを閉じる前にOpenCVを適切に終了
    cv2.destroyAllWindows()
    subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

