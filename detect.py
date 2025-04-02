# TODO: First, install the required libraries:
# pip install inference_sdk opencv-python

from inference_sdk import InferenceHTTPClient

# create an inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="ujwzpVqKpNMqRirBWTXZ"
)

# TODO: replace with your own image

img = "C:/Users/student/Pictures/Camera Roll/WIN_20250402_19_16_01_Pro.jpg" 
# run inference on a local image
output = CLIENT.infer(
    img, 
    model_id="dir2025/2",
)

import cv2
import numpy as np

def draw_bounding_boxes(image_path, output_path, detection_data):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not open or find the image")
    
    height, width, _ = image.shape
    
    # Iterate through predictions
    for prediction in detection_data['predictions']:
        x, y = int(prediction['x']), int(prediction['y'])
        w, h = int(prediction['width']), int(prediction['height'])
        class_name = prediction['class']
        confidence = prediction['confidence']
        
        # Calculate top-left and bottom-right coordinates
        top_left = (x - w // 2, y - h // 2)
        bottom_right = (x + w // 2, y + h // 2)
        
        # Draw rectangle
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)

        # Draw center point
        center = (x, y)
        cv2.circle(image, center, 5, (255, 0, 0), -1)

        # Print center points
        print(f"Center Point: {center}")
        
        # Put label
        label = f"{class_name} ({confidence:.2f})"
        cv2.putText(image, label, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # Save the image
    cv2.imwrite(output_path, image)
    print(f"Saved output image to {output_path}")


# Paths
output_image_path = "output.jpg"

# Draw bounding boxes and save the image
draw_bounding_boxes(img, output_image_path, output)