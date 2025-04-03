import pyrealsense2 as rs
import numpy as np
import cv2

pipe = rs.pipeline()
cfg = rs.config()

# Configure the pipeline to stream different resolutions of color and depth streams
cfg.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
cfg.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
# Start the pipeline
pipe.start(cfg)
# Get the intrinsic parameters of the color camera
profile = pipe.get_active_profile()
intr = profile.get_stream(rs.stream.color).as_video_stream_profile().get_intrinsics()
# Print the intrinsic parameters
print("Intrinsic parameters:")
print("Width:", intr.width)
print("Height:", intr.height)
print("PPX:", intr.ppx)
print("PPY:", intr.ppy)
print("FX:", intr.fx)
print("FY:", intr.fy)
# Print the extrinsic parameters
print("Extrinsic parameters:")
