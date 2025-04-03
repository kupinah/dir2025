import os
import time
import yaml
import detect2 
#from preparation import get_robot_targets
from robot_control import robot_init, moveL, current_position, move_complete

#robot_targets = get_robot_targets()  # pridobi cilje iz datoteke preparation.py

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

print("Koordinate za prenos 8 cokoladk v KS kamere (mm, stopinje):")

for i, point in enumerate(finish_points, start=1):
    x, y, z = point
    rx, ry, rz = 0.0, 180.0, 0.0  # predpostavljena orientacija

    formatted_point = (x, y, z, rx, ry, rz)
    print(f"{i}. {formatted_point}")


adjusted_targets = []  # seznam premaknjenih koordinat

# prilagoditev koordinat glede na zamik med kamero in robotom
for target in robot_targets:
    x_um = target[0] + delta_X_kamera_robot * 1000
    y_um = target[1] + delta_Y_kamera_robot * 1000
    adjusted_target = (x_um, y_um, target[2], target[3], target[4], target[5], target[6])
    adjusted_targets.append(adjusted_target)

# izpis trenutne pozicije robota v mm in stopinjah
#position_mm_deg = current_position(format="mm_deg")
#print("Trenutna pozicija robota (mm, stopinje):")
#print(position_mm_deg)

# začasna pozicija robota (x_mm, y_mm, z_mm, rx_deg, ry_deg, rz_deg)
robot_position_mm = (120.0, 80.0, 400.0, 0.0, 180.0, 0.0)  # ← začasna vrednost brez povezave z robotom
print("")
print("Trenutna pozicija robota (mm, stopinje):")
print(robot_position_mm)

# upoštevanje zamika kamere glede na robota
delta_x = delta_X_kamera_robot
delta_y = delta_Y_kamera_robot

final_position_mm = (
    robot_position_mm[0] + delta_x,
    robot_position_mm[1] + delta_y,
    robot_position_mm[2],
    robot_position_mm[3],
    robot_position_mm[4],
    robot_position_mm[5]
)

# pozicija kamere v KS robota
print("")
print("pozicija kamere v KS robota (mm, stopinje):")
print(final_position_mm)

# pridobi prvo koordinato iz seznama čokoladk
first_target_um = robot_targets[0]  # v mikrometrih
first_target_mm = (first_target_um[0] / 1000, first_target_um[1] / 1000)  # pretvori v mm

print("")
print("koordinate vseh čokoladk v KS robota (mm, stopinje):")

for i, target_um in enumerate(robot_targets, start=1):
    target_mm = (target_um[0] / 1000, target_um[1] / 1000)  # pretvori v mm

    position_with_object = (
        final_position_mm[0] + target_mm[0],
        final_position_mm[1] + target_mm[1],
        final_position_mm[2],
        final_position_mm[3],
        final_position_mm[4],
        final_position_mm[5]
    )

    print(f"{i}. {position_with_object}")




