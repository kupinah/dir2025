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
MIN_DEPTH = 0.823  # 20 cm
# MAX_DEPTH = 1  # 30 cm

# MIN_DEPTH = 0.38
MAX_DEPTH = 0.89


profile = pipeline.get_active_profile()
sensor = profile.get_device().query_sensors()[0]  # 0 for depth sensor, 1 for camera sensor
sensor.set_option(rs.option.min_distance, 0)

# colorize = rs.colorizer()
# colorize.set_option(rs.option.histogram_equalization_enabled, 1.0)

# sensor.set_option(rs.option.enable_max_usable_range, 0)
img_index = 1
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

        # Convert the depth frame to a NumPy array (depth in millimeters)
        depth_image = np.asanyarray(depth_frame.get_data())

        # Apply histogram equalization to the depth image manually
        # Convert depth to 8-bit image first for histogram equalization
        depth_8bit = cv2.convertScaleAbs(depth_image, alpha=0.03)  # Normalize the depth image
        equalized_depth = cv2.equalizeHist(depth_8bit)  # Apply histogram equalization

        # Create a mask to filter out depth values below 40 cm (400 mm)
        depth_mask = (depth_image >= MIN_DEPTH * 1000) & (depth_image <= MAX_DEPTH * 1000)

        # Apply a colormap to the normalized depth data
        depth_colormap = cv2.applyColorMap(equalized_depth, cv2.COLORMAP_JET)

        # Highlight the objects within the desired depth range (40 cm to 100 cm)
        depth_colormap[depth_mask] = [0, 0, 0]  # Highlight in red for objects in range

        # For objects outside the valid range, set them to black (underexposure)
        depth_colormap[~depth_mask] = [255, 255, 255]  # Underexpose areas outside the range

        # Display the depth map with histogram equalization and range filtering
        cv2.imshow("Depth Visualization with Range Filtering", depth_colormap)

        # Check for exit key press
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Press 'q' to exit
            break

        if key == ord('s'):
            cv2.imwrite(f"C:/Users/student/Desktop/dir2025/GLOBINA 1/image{img_index}.png", depth_colormap)
            img_index += 1

finally:
    # Stop the pipeline
    pipeline.stop()

    # Close the OpenCV window
    cv2.destroyAllWindows()