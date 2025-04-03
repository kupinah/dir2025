import os
import time
import yaml
import detect2 
from preparation import get_robot_targets
from robot_control import robot_init, moveL, current_position, move_complete

robot_targets = get_robot_targets()  # pridobi cilje iz datoteke preparation.py

# zamik KS kamera - KS robota
delta_X_kamera_robot = 10      # [mm]
delta_Y_kamera_robot = 50      # [mm]

# zamik KS seske - KS robota
# delta_X_seska_robot = 10      # [mm]
# delta_Y_seska_robot = 50      # [mm]

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

# branje končnih koordinat iz YAML datoteke
yaml_path = os.path.join("yaml", "finish_points.yaml")
with open(yaml_path, 'r', encoding='utf-8') as file:
    finish_points = yaml.safe_load(file)

print("Koordinate za prenos 8 cokoladk")
print(finish_points)

adjusted_targets = []  # seznam premaknjenih koordinat

# prilagoditev koordinat glede na zamik med kamero in robotom
for target in robot_targets:
    x_um = target[0] + delta_X_kamera_robot * 1000
    y_um = target[1] + delta_Y_kamera_robot * 1000
    adjusted_target = (x_um, y_um, target[2], target[3], target[4], target[5], target[6])
    adjusted_targets.append(adjusted_target)

# izpis trenutne pozicije robota v mm in stopinjah
position_mm_deg = current_position(format="mm_deg")
print("Trenutna pozicija robota (mm, stopinje):")
print(position_mm_deg)
