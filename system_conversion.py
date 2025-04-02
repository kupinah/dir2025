import numpy as np

def pixel_to_robot(x_p, y_p):
    # Given reference points
    pixel1 = np.array([0, 0])
    robot1 = np.array([450, 395])
    pixel2 = np.array([1920, 1080])
    robot2 = np.array([270, 485])
    
    # Compute scaling factors
    scale_x = (robot2[0] - robot1[0]) / (pixel2[0] - pixel1[0])
    scale_y = (robot2[1] - robot1[1]) / (pixel2[1] - pixel1[1])
    
    # Compute translation offsets
    offset_x = robot1[0] - scale_x * pixel1[0]
    offset_y = robot1[1] - scale_y * pixel1[1]
    
    print(offset_x, offset_y)
    # Convert input pixel coordinates to robot coordinates
    x_r = scale_x * x_p + offset_x
    y_r = scale_y * y_p + offset_y
    
    return round(x_r,2 ), round(y_r, 2)

# Example usage:
print(pixel_to_robot(284, 773))
