import pyrealsense2 as rs

# Create a context object to interact with the RealSense devices
context = rs.context()

# Get the list of connected devices
devices = context.query_devices()

if len(devices) == 0:
    print("No RealSense devices connected.")
else:
    print(f"{len(devices)} device(s) found:")
    for i, device in enumerate(devices):
        print(f"\nDevice {i+1}: {device.get_info(rs.camera_info.name)} (Serial: {device.get_info(rs.camera_info.serial_number)})")

        # Get the device's available streams (depth, color, etc.)
        for sensor in device.sensors:
            print(f"  Sensor: {sensor.get_info(rs.camera_info.name)}")
            
            # Get current configuration of the sensor (like resolution and fps)
            intrinsics = sensor.get_stream_profiles()
            for profile in intrinsics:
                print(f"    Stream: {profile.stream_name()}")
                print(f"    Resolution: {profile.as_video_stream_profile().width}x{profile.as_video_stream_profile().height}")
                print(f"    Frame Rate: {profile.as_video_stream_profile().fps} fps")

        print("\n--- End of Device Configuration ---\n")
