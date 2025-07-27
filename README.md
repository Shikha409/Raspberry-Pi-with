# Raspberry-Pi-with Pi Camera
Pi Camera


# Raspberry Pi Camera Interfacing

This project demonstrates capturing images and videos using the Raspberry Pi Camera Module with Python. It provides a menu-driven interface to capture images with timestamp annotations and videos in `.h264` format, with error handling and logging.

## Requirements
- Raspberry Pi (with camera port)
- Raspberry Pi Camera Module (v1/v2/HQ)
- Python 3
- Libraries: `picamera` (install with `pip install picamera`)
- `omxplayer` for video playback (install with `apt-get install omxplayer`)

## Setup
1. Connect the Pi Camera to the CSI port.
2. Enable the camera:
   
   sudo raspi-config

 ## 3. Install dependencies:
sudo pip install picamera
sudo apt-get install omxplayer
Run the code:

python3 pi_camera.py
Features
Capture images (1024x768) with timestamp annotations.
Capture 10-second videos (640x480) in .h264 format.
Log actions to camera.log.
Menu-driven interface for ease of use.
Usage
Run python3 pi_camera.py and choose:
1: Capture an image (saved as image_YYYYMMDD_HHMMSS.jpeg).
2: Capture a 10-second video (saved as video_YYYYMMDD_HHMMSS.h264).
3: Exit.
Play videos with:
omxplayer video_YYYYMMDD_HHMMSS.h264
License
MIT License (see LICENSE file).
