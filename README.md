- usb cam node
  - ros2 run usb_camera_driver usb_camera_driver_node __ns:=/<your namespace> __params:=config.yaml
  - ros2 run image_transport republish raw in:=image_raw compressed out:=image_raw_compressed
  - ros2 run usb_cam usb_cam_node_exe
  - ros2 run v4l2_camera v4l2_camera_node
  - ros2 run rqt_image_view rqt_image_view
- realsense_ros
  - ros2 launch realsense2_camera rs_launch.py align_depth.enable:=true
- ultralytics_ros
  - ros2 launch ultralytics_ros tracker.launch.xml debug:=true
  - ros2 launch ultralytics_ros tracker_with_cloud.launch.xml debug:=true
- yolov8_ros
  - ros2 launch yolov8_bringup yolov8.launch.py
  - ros2 launch yolov8_bringup yolov8_3d.launch.py
  - instance segmentation
    - ros2 launch yolov8_bringup yolov8.launch.py model:=yolov8m-seg.pt
  - human pose
    - ros2 launch yolov8_bringup yolov8.launch.py model:=yolov8m-pose.pt
  - 3b object detection
    - ros2 launch yolov8_bringup yolov8_3d.launch.py



refes:
- https://github.com/Alpaca-zip/ultralytics_ros
- https://github.com/mgonzs13/yolov8_ros
- https://github.com/klintan/ros2_usb_camera
- https://qiita.com/Hiroaki-K4/items/53c2565c77319ecc76e2
- https://note.com/kan_hatakeyama/n/n2aa17f80c369
- [Dockerコンテナ内の ROS 2 環境でRealSense D435を使用する](https://qiita.com/porizou1/items/8bf56efc3307e40624af)https://qiita.com/porizou1/items/8bf56efc3307e40624af
