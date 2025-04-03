# Prenos izdelkov

import os
import time
import yaml
import detect2 
from robot_control import robot_init, moveL, current_position, move_complete

# Pretvorba iz mm in ° v notranji format robota
def to_internal(x_mm, y_mm, z_mm, rx_deg, ry_deg, rz_deg, re_deg=0):
    x = int(x_mm * 1000)          # mm → mikrometri
    y = int(y_mm * 1000)
    z = int(z_mm * 1000)
    rx = int(rx_deg * 10000)      # ° → 0.0001 stopinje
    ry = int(ry_deg * 10000)
    rz = int(rz_deg * 10000)
    re = int(re_deg * 10000)
    return (x, y, z, rx, ry, rz, re)

# Pot do datoteke v podmapi 'yaml'
ime_datoteke = "yaml/finish_points.yaml"

# Odpri datoteko in preberi vsebino
with open(ime_datoteke, 'r', encoding='utf-8') as datoteka:
    podatki = yaml.safe_load(datoteka)

# Slovar za preslikavo tipa v ime živali
tipi_objektov = {
    1: "medved",
    2: "slon",
    3: "konj",
    4: "lev"
}

# začetna pozicija z orientacijo (v mm in stopinjah)
start_point_mm = (400.0, 400.0, 400.0, 0.0, 180.0, 0.0)

# Inicializacija robota (odkomentiraj, če uporabljaš robota)
# robot_init()

# Premik na začetno točko
start_point = to_internal(*start_point_mm)
print("Premik na začetno točko...")
# moveL(start_point)
# while not move_complete():
#     time.sleep(0.1)

print("Pripravljen za nalogo:")

# Pot do slike
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "Cokoladke2.jpg")
output_path = os.path.join(script_dir, "output.jpg")

# Zaznavanje objektov
output = detect2.detect_objects(image_path)
centers = detect2.draw_boxes_and_return_centers(image_path, output_path, output)

# Spremeni Y koordinato (nova_y = 1080 - stara_y)
for prediction in output['predictions']:
    prediction['y'] = 1080 - prediction['y']

# Izpis rezultatov
print("Seznam spremenjenih centrov objektov:")
for prediction in output['predictions']:
    x = int(prediction['x'])
    y = int(prediction['y'])
    class_name = prediction['class']
    confidence = prediction['confidence']
    print(f"({x}, {y}) - {class_name} ({confidence:.2f})")

# ------------------------------------------------------------------
# Pretvorba v notranji format robota

px_per_mm = 1.0  # ← prilagodi glede na umerjanje

robot_targets = []

for prediction in output['predictions']:
    x_px = int(prediction['x'])
    y_px = int(prediction['y'])

    # Pretvorba v mm
    x_mm = x_px / px_per_mm
    y_mm = y_px / px_per_mm
    z_mm = 400.0

    rx, ry, rz = 0.0, 180.0, 0.0

    target = to_internal(x_mm, y_mm, z_mm, rx, ry, rz)
    robot_targets.append(target)

# Obdrži največ 8 ciljev
robot_targets = robot_targets[:8]

# Izpis končnih točk za robota
print("\nKoordinate v internem formatu robota:")
for i, target in enumerate(robot_targets, 1):
    print(f"{i}. {target}")

exec(open("transfer.py").read())