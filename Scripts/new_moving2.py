#Gibanje med več točkami v zanki

import time
from robot_control import robot_init, moveL, current_position, move_complete


# parametre
pause = 0.1

# Seznam točk (v mm in stopinjah)
path_points_mm = [
    (300.0, -500.0, 400.0, 60.0, -60.0, -50.0),
    (320.0, -480.0, 420.0, 61.0, -59.0, -49.0),
    (340.0, -460.0, 440.0, 62.0, -58.0, -48.0),
]

# Inicializacija robota
robot_init()


# Funkcija: pretvori mm in ° v notranji format robota
def to_internal(x_mm, y_mm, z_mm, rx_deg, ry_deg, rz_deg, re_deg=0):
    x = int(x_mm * 1000)
    y = int(y_mm * 1000)
    z = int(z_mm * 1000)
    rx = int(rx_deg * 10000)
    ry = int(ry_deg * 10000)
    rz = int(rz_deg * 10000)
    re = int(re_deg * 10000)
    return (x, y, z, rx, ry, rz, re)


# Neskončna zanka: premikanje po vseh točkah v krogu
try:
    while True:
        for idx, pt_mm in enumerate(path_points_mm):
            point = to_internal(*pt_mm)
            print(f"Premik na točko {idx+1}...")
            moveL(point)
            while not move_complete():
                time.sleep(pause)
except KeyboardInterrupt:
    print("🛑 Premikanje prekinjeno s strani uporabnika.")


# Izpis končne pozicije (če kdaj konča)
print("Končna pozicija:")
pos = current_position("mm_deg")
print(pos)
