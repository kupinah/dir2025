# Skripta za notranjo kalibracijo spletne kamere s shranjevanjem rezultatov v mapo "jaml"

import cv2
import numpy as np
import yaml
import os

# --- Parametri šahovnice ---
chessboard_size = (9, 7)  # število notranjih kotov (vodoravno, navpično)
square_size = 20  # velikost kvadratka v mm

# --- Priprava 3D točk šahovnice ---
objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
objp *= square_size

# --- Seznami za shranjevanje 3D in 2D točk ---
objpoints = []
imgpoints = []

# --- Ustvari mapo "jaml" za shranjevanje rezultatov ---
output_dir = "jaml"
os.makedirs(output_dir, exist_ok=True)

# --- Zagon kamere ---
cap = cv2.VideoCapture(0)
cv2.namedWindow('Kalibracija', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Kalibracija', 960, 720)

max_frames = 15  # največje število uporabnih slik
saved_frames = 0

print("Pritisnite 's' za shranjevanje slike, 'q' za izhod.")

while saved_frames < max_frames:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    found, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if found:
        cv2.drawChessboardCorners(frame, chessboard_size, corners, found)

    # Prikaz slike v oknu
    cv2.imshow('Kalibracija', frame)
    key = cv2.waitKey(1)

    if key == ord('s') and found:
        # Shranjevanje točk za kalibracijo
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11,11), (-1,-1),
                                    criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        imgpoints.append(corners2)
        saved_frames += 1
        print(f"Slika {saved_frames}/{max_frames} shranjena.")

    elif key == ord('q'):
        break

print("Zajem zaključen.")
cap.release()
cv2.destroyAllWindows()

# --- Kalibracija ---
print("Izvajanje kalibracije...")
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, gray.shape[::-1], None, None)

print("Matrika kamere:\n", camera_matrix)
print("Koeficienti popačenja:\n", dist_coeffs)

# --- Shranjevanje rezultatov v YAML datoteko v mapo "jaml" ---
calib_data = {
    'camera_matrix': camera_matrix.tolist(),
    'dist_coeff': dist_coeffs.tolist()
}

yaml_path = os.path.join(output_dir, "calibration.yaml")
with open(yaml_path, "w") as f:
    yaml.dump(calib_data, f)

print(f"Rezultati kalibracije shranjeni v '{yaml_path}'")
