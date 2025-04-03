# Prenos izdelkov
import time
import yaml
from robot_control import robot_init, moveL, current_position, move_complete

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

# Izpiši podatke z razlago tipa objekta
for indeks, element in enumerate(podatki):
    x, y, z, tip = element
    ime = tipi_objektov.get(tip, "neznano")
    print(f"{indeks + 1}. x: {x}, y: {y}, z: {z}, tip: {tip} ({ime})")

# začetna pozicija z orientacijo (v mm in stopinjah)
start_point_mm = (400.0, 400.0, 400.0, 0.0, 180.0, 0.0)


# --------------------------------------------------

# Inicializacija robota
#robot_init()

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

# Premik na začetno točko
start_point = to_internal(*start_point_mm)
print("Premik na začetno točko...")
#moveL(start_point)
#while not move_complete():
#    time.sleep(0.1)

# Izpis končne pozicije
print("Pripravljen za nalogo:")
#pos = current_position(format="mm_deg")
#print(pos)
