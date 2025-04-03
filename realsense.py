import pyrealsense2 as rs
import cv2
import numpy as np

# Create a context object to interact with the RealSense devices
context = rs.context()

# Check if there are any connected devices
devices = context.query_devices()

if len(devices) == 0:
    print("No RealSense devices connected.")
    exit()

# Initialize RealSense pipeline
pipeline = rs.pipeline()

# Configure the pipeline to stream color and depth
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # Color stream (RGB)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)   # Depth stream

# Start streaming
pipeline.start(config)

# Depth range in meters (20 cm to 30 cm)
MIN_DEPTH = 0.2  # 20 cm
MAX_DEPTH = 0.3  # 30 cm



profile = pipeline.get_active_profile()
sensor = profile.get_device().query_sensors()[0]  # 0 for depth sensor, 1 for camera sensor
sensor.set_option(rs.option.min_distance, 0)
sensor.set_option(rs.option.max_distance, 0.5)

# sensor.set_option(rs.option.enable_max_usable_range, 0)

try:
    while True:
        # Wait for a coherent pair of frames: color and depth
        frames = pipeline.wait_for_frames()

        # Get color and depth frames
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        if not color_frame or not depth_frame:
            continue

        # Convert the RealSense color frame to a NumPy array
        color_image = np.asanyarray(color_frame.get_data())

        # Convert the depth frame to a NumPy array
        depth_image = np.asanyarray(depth_frame.get_data())
        print(depth_image[0][0])

        # Create a mask for depth values between 20 cm and 30 cm
        depth_mask = ((depth_image >= MIN_DEPTH * 1000) & (depth_image <= MAX_DEPTH * 1000)).astype(np.int16)

        # Highlight the regions within the desired depth range by modifying the color image
        color_image[depth_mask] = [0, 0, 255]  # Red color for the detected objects (you can change the color)

        # Display the color frame with detected regions
        cv2.imshow("Color Frame with Depth Detection", depth_image)

        # Check for exit key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Press 'q' to exit
            break

finally:
    # Stop the pipeline
    pipeline.stop()

    # Close the OpenCV window
    cv2.destroyAllWindows()
