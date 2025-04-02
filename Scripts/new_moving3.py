# shranjevanje trenutne pozicije v datoteko YAML

import time
import keyboard
import yaml
import os
from datetime import datetime
from robot_control import robot_init, current_position

# Inicializacija robota
robot_init()

# Ustvari mapo za shranjevanje
save_dir = "saved_points"
os.makedirs(save_dir, exist_ok=True)

# Ustvari unikatno ime datoteke z datumom in uro
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = os.path.join(save_dir, f"points_{timestamp}.yaml")

# Ustvari začetno strukturo
data = {"points": []}

print("🟢 Skripta pripravljena.")
print("Premakni robota ročno s pultom.")
print("Pritisni [SPACE], da shraniš trenutno pozicijo.")
print("Za izhod pritisni Ctrl+C.")
print(f"Shranjevanje v: {filename}")

try:
    while True:
        if keyboard.is_pressed("space"):
            pos = current_position("mm_deg")  # (x, y, z, rx, ry, rz)
            rounded = [round(val, 3) for val in pos]
            data["points"].append(rounded)

            with open(filename, "w") as f:
                yaml.dump(data, f, sort_keys=False)

            print(f"💾 Shranjeno: {rounded}")
            time.sleep(0.3)

except KeyboardInterrupt:
    print("🛑 Skripta končana.")
