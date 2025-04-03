# Prepoznavanje čokoladk, generiranje bounding boxes, koordinate središč

from inference_sdk import InferenceHTTPClient
import cv2
import numpy as np
import os

# Ustvari API odjemalca
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="ujwzpVqKpNMqRirBWTXZ"
)

# Pot do slike
image_filename = "Cokoladke2.jpg"
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, image_filename)

# Preveri, če slika obstaja
if not os.path.isfile(image_path):
    raise FileNotFoundError(f"Slika ni bila najdena: {image_path}")

# Pošlji pot do slike kot string
output = CLIENT.infer(image_path, model_id="dir2025/2")

# Nariši in shrani rezultate
def draw_boxes_and_return_centers(image_path, output_path, data):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Slike ni bilo mogoče naložiti.")

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
    print(f"Izhodna slika shranjena kot: {output_path}")
    return centers

# -----------------------------------------------------------------------------

# Shrani rezultat in izpiši centre
output_image_path = os.path.join(script_dir, "output.jpg")
object_centers = draw_boxes_and_return_centers(image_path, output_image_path, output)

print("Seznam centrov objektov:")
for prediction in output['predictions']:
    x, y = int(prediction['x']), int(prediction['y'])
    class_name = prediction['class']
    confidence = prediction['confidence']
    print(f"({x}, {y}) - {class_name} ({confidence:.2f})")

