# Skripta za določanje in shranjevanje zunanje kalibracije kamere glede na šahovnico na mizi

import cv2
import numpy as np
import yaml
import os

# --- Naloži parametre notranje kalibracije ---
with open("jaml/calibration.yaml", "r") as f:
    calib_data = yaml.safe_load(f)

camera_matrix = np.array(calib_data["camera_matrix"])
dist_coeffs = np.array(calib_data["dist_coeff"])

# --- Parametri šahovnice ---
chessboard_size = (9, 7)
square_size = 25  # v mm

# --- Priprava 3D točk šahovnice ---
objp = np.zeros((chessboard_size[0]*chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
objp *= square_size

# --- Zagon kamere ---
cap = cv2.VideoCapture(0)
cv2.namedWindow("Kalibracija", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Kalibracija", 960, 720)

print("Pritisni 's' za zajem slike in izračun extrinsics. ESC za izhod.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Napaka pri zajemu slike.")
        break

    cv2.imshow("Kalibracija", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        found, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

        if not found:
            print("Šahovnica ni bila zaznana.")
            continue

        corners_subpix = cv2.cornerSubPix(
            gray, corners, (11, 11), (-1, -1),
            criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        )

        ret, rvec, tvec = cv2.solvePnP(objp, corners_subpix, camera_matrix, dist_coeffs)

        print("rvec (rotacijski vektor):\n", rvec)
        print("tvec (translacijski vektor):\n", tvec)

        # Prikaz
        vis = frame.copy()
        cv2.drawChessboardCorners(vis, chessboard_size, corners_subpix, found)
        cv2.imshow("Zaznana šahovnica", vis)

        # Shrani extrinsics v YAML
        extrinsics = {
            'rvec': rvec.tolist(),
            'tvec': tvec.tolist()
        }

        os.makedirs("jaml", exist_ok=True)
        with open("jaml/extrinsics.yaml", "w") as f:
            yaml.dump(extrinsics, f)

        print("Extrinsics shranjeni v 'jaml/extrinsics.yaml'")

    elif key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
