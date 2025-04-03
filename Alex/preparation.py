# priprava za gibanje

import os
import time
import yaml
import detect3 
from robot_control import robot_init, moveL, current_position, move_complete

robot_targets = []  # globalna spremenljivka za shranjevanje ciljev

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

def run_preparation():  # glavna funkcija za pripravo ciljev
    global robot_targets

    # začetna pozicija z orientacijo (v mm in stopinjah)
    start_point_mm = (410.0, 485.7,  40.0, -180.0, 0.0, 0.0)

    # Inicializacija robota (odkomentiraj, če uporabljaš robota)
    robot_init()

    # Premik na začetno točko
    start_point = to_internal(*start_point_mm)
    print("Premik na začetno točko...")
    moveL(start_point)
    while not move_complete():
        pass

    time.sleep(5)
    print("Pripravljen za nalogo:")

    # Pot do slike
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "Cokoladke2.jpg")
    output_path = os.path.join(script_dir, "output.jpg")

    # Zaznavanje objektov
    output = detect3.detect_objects(image_path)
    centers = detect3.draw_boxes_and_return_centers(image_path, output_path, output)

    # Spremeni Y koordinato (nova_y = 1080 - stara_y)
    for prediction in output['predictions']:
        prediction['y'] = 1080 - prediction['y']

    # Pretvorba pixl - mm
    px_per_mm = 7.0  # ← prilagodi glede na umerjanje

    robot_targets = []  # ponastavi cilje

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
    print("\n koordinate čokoladk v mkm:")
    for i, target in enumerate(robot_targets, 1):
        print(f"{i}. {target}")

def get_robot_targets():
    return robot_targets  # vrne seznam ciljnih koordinat

# Če se datoteka zažene neposredno, zaženi pripravo in glavni skript
if __name__ == "__main__":
    run_preparation()
    exec(open("moving1.py", encoding="utf-8").read())  # zažene glavni skript"

