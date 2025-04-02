# gibanje horizontalno in vertikalno

import time
import yaml
from robot_control import robot_init, moveL, move_complete, execute_job

# Inicializacija robota
robot_init()

# Pretvorba v notranji format (mm → μm, ° → 0.0001°)
def to_internal(x_mm, y_mm, z_mm, rx_deg, ry_deg, rz_deg, re_deg=0, job_name=""):
    x = int(x_mm * 1000)
    y = int(y_mm * 1000)
    z = int(z_mm * 1000)
    rx = int(rx_deg * 10000)
    ry = int(ry_deg * 10000)
    rz = int(rz_deg * 10000)
    re = int(re_deg * 10000)
    return (x, y, z, rx, ry, rz, re), job_name

# Horizontalno gibanje
def move(points, index, pause=0.1):
    print("▶️ Horizontalno gibanje...")
    target_pos, job = to_internal(*points[index])
    moveL(target_pos)
    while not move_complete():
        time.sleep(0.1)
    execute_job(job)
    time.sleep(pause)

# # Vertikalno gibanje
# def vertical_move(points, index, pause=0.1):
#     print("⬆️ Vertikalno gibanje...")
#     target_pos = to_internal(*points[index])
#     moveL(target_pos)
#     while not move_complete():
#         time.sleep(0.1)
#     time.sleep(pause)

def main():
    # Ime datoteke z zajetimi točkami
    filename = "points.yaml"

    # Branje točk iz datoteke
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
        points = data.get("points", [])

    if len(points) < 2:
        print("⚠️ Ni dovolj točk v datoteki.")
        return
    for i in range(len(points)):
        move(points, index=i, pause=0.2)
    # vertical_move(points, index=1, pause=0.3)

if __name__ == "__main__":
    main()
