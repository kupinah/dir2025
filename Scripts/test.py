import robot_control
import time

robot_control.robot_init()

pos1 = (600000, 000000, 600000, 0000, 1800000, 0, 0)

pos2 = (400000, 400000, 400000, 0000, 0000, 0000, 0)

print("POS2")

robot_control.moveJ(target_pos=pos2)

while robot_control.move_complete():
    continue

robot_control.current_position()

print("POS1")

robot_control.moveJ(target_pos=pos1)


while robot_control.move_complete():
    continue

robot_control.current_position()
