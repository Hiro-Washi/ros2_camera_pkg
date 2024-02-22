#!/usr/bin/env python3


import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class VideoImagePublisher(Node):
    def __init__(self):
        super().__init__('video_image_publisher')
        self.publisher_ = self.create_publisher(Image, '/video', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.br = CvBridge()

    def timer_callback(self):
        #img = cv2.imread('path_to_your_image.jpg')  # 画像ファイルのパスを指定
        img = cv2.VideoCapture(0)
        ros_image = self.br.cv2_to_imgmsg(img, "bgr8")
        self.publisher_.publish(ros_image)
        self.get_logger().info('Publishing video frame')

def main(args=None):
    rclpy.init(args=args)
    video_image_publisher = VideoImagePublisher()
    rclpy.spin(video_image_publisher)
    video_image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

