# aero-cobot-perception-system
# ✈️ Aero Cobot Perception System

## Overview
This project implements a perception and control system for a collaborative robot (cobot) used in aeronautical manufacturing.

## Features
- LiDAR obstacle detection
- 2D camera processing (OpenCV)
- 3D point cloud processing (Open3D)
- Sensor fusion
- Safe motion control

## Tech Stack
- ROS2
- Python
- OpenCV
- Open3D

## Run
```bash
pip install -r requirements.txt
python src/vision_2d/camera_2d.py
Author

Jinene Ben Said


---

# 📄 requirements.txt

```txt
opencv-python
open3d
numpy
rclpy
sensor_msgs
📄 Dockerfile
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]
