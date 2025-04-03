
# TODO: First, install the required libraries:
# pip install inference_sdk opencv-python

from inference_sdk import InferenceHTTPClient
import os

# create an inference client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="ovceb4fOJqyDwEaLLsDj"
)

# TODO: replace with your own image

photos_directory = "C:/Users/student/Desktop/dir2025/GLOBINA 1"

def get_latest_file(directory):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        print("No files found in the directory.")
        return None
    
    # Get the full path of each file
    full_paths = [os.path.join(directory, f) for f in files]
    
    # Sort the files by their last modified time (descending order)
    latest_file = max(full_paths, key=os.path.getmtime)
    print(latest_file)


    return str(latest_file).replace("\\", "/")

img = get_latest_file(photos_directory)
# run inference on a local image
output = CLIENT.infer(
    img, 
    model_id="sui/1",
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