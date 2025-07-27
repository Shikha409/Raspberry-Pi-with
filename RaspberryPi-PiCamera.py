import picamera
from time import sleep
import datetime
import os
import logging

# Configure logging
logging.basicConfig(
    filename='camera.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def setup_camera():
    """Initialize Pi Camera with error handling."""
    try:
        camera = picamera.PiCamera()
        camera.resolution = (1024, 768)  # Default for images
        camera.brightness = 60
        logging.info("Camera initialized successfully")
        return camera
    except picamera.exc.PiCameraError as e:
        logging.error(f"Failed to initialize camera: {e}")
        print(f"Error: Camera initialization failed. Ensure camera is enabled and connected.")
        return None

def capture_image(camera, filename=None):
    """Capture an image with timestamp annotation."""
    try:
        if not filename:
            filename = f"image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.jpeg"
        camera.resolution = (1024, 768)
        camera.annotate_text = f"Captured: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        camera.start_preview()
        sleep(2)  # Allow camera to adjust
        camera.capture(filename)
        camera.stop_preview()
        logging.info(f"Image captured: {filename}")
        print(f"Image saved as {filename}")
    except picamera.exc.PiCameraError as e:
        logging.error(f"Image capture failed: {e}")
        print("Error: Failed to capture image.")

def capture_video(camera, duration=10, filename=None):
    """Capture a video for specified duration."""
    try:
        if not filename:
            filename = f"video_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.h264"
        camera.resolution = (640, 480)
        camera.start_recording(filename)
        camera.wait_recording(duration)
        camera.stop_recording()
        logging.info(f"Video captured: {filename} (Duration: {duration}s)")
        print(f"Video saved as {filename}. Play with 'omxplayer {filename}'")
    except picamera.exc.PiCameraError as e:
        logging.error(f"Video capture failed: {e}")
        print("Error: Failed to capture video.")

def main():
    camera = setup_camera()
    if not camera:
        return

    try:
        while True:
            print("\nPi Camera Menu:")
            print("1. Capture Image")
            print("2. Capture Video (10 seconds)")
            print("3. Exit")
            choice = input("Enter choice (1-3): ")

            if choice == '1':
                capture_image(camera)
            elif choice == '2':
                duration = 10  # Fixed duration, can be modified
                capture_video(camera, duration)
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    finally:
        if camera:
            camera.close()
            logging.info("Camera closed")
            print("Camera closed.")

if __name__ == "__main__":
    main()
