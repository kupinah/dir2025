import robot_control
import time

robot_control.robot_init()

pos1 = (600000, 000000, 600000, 0000, 0000, 0000, 0)

pos2 = (400000, 400000, 400000, 0000, 0000, 0000, 0)

robot_control.moveJ(target_pos=pos2)

time.sleep(10)

robot_control.moveJ(target_pos=pos1)


robot_control.current_position()
