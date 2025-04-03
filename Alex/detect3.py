from inference_sdk import InferenceHTTPClient
import cv2
import numpy as np
import os

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="ujwzpVqKpNMqRirBWTXZ"
)

def detect_objects(image, model_id="dir2025/2"):
    return CLIENT.infer(image, model_id=model_id)

def draw_boxes_and_return_centers(image, output_path, data):
    centers = []

    for prediction in data['predictions']:
        x, y = int(prediction['x']), int(prediction['y'])
        w, h = int(prediction['width']), int(prediction['height'])
        class_name = prediction['class']
        confidence = prediction['confidence']

        top_left = (x - w // 2, y - h // 2)
        bottom_right = (x + w // 2, y + h // 2)

        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 3)
        cv2.circle(image, (x, y), 5, (255, 0, 0), -1)

        label = f"{class_name} ({confidence:.2f})"
        cv2.putText(image, label, (top_left[0], top_left[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        centers.append((x, y))

    cv2.imwrite(output_path, image)
    return centers

def print_centers(data):
    for prediction in data['predictions']:
        x, y = int(prediction['x']), int(prediction['y'])
        class_name = prediction['class']
        confidence = prediction['confidence']
        print(f"({x}, {y}) - {class_name} ({confidence:.2f})")

if __name__ == "__main__":
    # Initialize camera (use 0 for default camera, or change to another index if you have multiple cameras)
    cap = cv2.VideoCapture(1)
    
    if not cap.isOpened():
        print("Napaka pri odpiranju kamere!")
        exit()

    # Capture a frame from the camera
    ret, frame = cap.read()
    
    if not ret:
        print("Napaka pri zajemu slike!")
        exit()

    # Close the camera
    cap.release()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_image_path = os.path.join(script_dir, "output1.jpg")
    cv2.imwrite(output_image_path, frame)
    # Perform detection on the captured frame
    output = detect_objects(frame)
    
    # Output image path
    output_image_path = os.path.join(script_dir, "output.jpg")
    
    # Draw boxes on the frame and save the result
    centers = draw_boxes_and_return_centers(frame, output_image_path, output)

    # Optionally print the centers to the console
    print_centers(output)
