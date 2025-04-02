# Skripta: klikni na točko na mizi in izpiše njene koordinate (Z = 0)

import cv2
import numpy as np
import yaml

# --- Naloži kalibracijske podatke ---
with open("jaml/calibration.yaml", "r") as f:
    calib = yaml.safe_load(f)
K = np.array(calib["camera_matrix"])
dist = np.array(calib["dist_coeff"])

with open("jaml/extrinsics.yaml", "r") as f:
    extr = yaml.safe_load(f)
rvec = np.array(extr["rvec"])
tvec = np.array(extr["tvec"]).reshape(3, 1)
R, _ = cv2.Rodrigues(rvec)
R_inv = R.T

# --- Parametri šahovnice ---
rows, cols = 6, 9
square_size = 25  # mm

transform_matrix = np.diag([1, 1, 1])  # brez obračanja

click_points = []

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pt = np.array([[[x, y]]], dtype=np.float32)
        pt_undist = cv2.undistortPoints(pt, K, dist, P=K)
        ray = np.append(pt_undist[0, 0], 1).reshape(3, 1)

        normal = np.array([0, 0, 1]).reshape(1, 3)
        s = -normal @ R_inv @ tvec / (normal @ R_inv @ ray)
        P_camera = s * ray
        P_board = R_inv @ (P_camera - tvec)

        P_custom = transform_matrix @ P_board
        P_custom[2, 0] = 0  # Z = 0
        P_flat = P_custom.ravel()

        print(f"Klik: ({x}, {y}) → Koordinate na mizi: {P_flat[:2]} mm")
        click_points.append((x, y, P_flat))

# --- Kamera in okno ---
cap = cv2.VideoCapture(0)
cv2.namedWindow("Kamera", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Kamera", 960, 720)
cv2.setMouseCallback("Kamera", on_mouse_click)

print("Klikni na točko na mizi (ESC za izhod).")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for (x, y, coords) in click_points:
        label = f"[{coords[0]:.1f}, {coords[1]:.1f}] mm"
        cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)
        cv2.putText(frame, label, (x + 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow("Kamera", frame)
    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
