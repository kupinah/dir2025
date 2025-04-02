import numpy as np
import pandas as pd
import time
import lib.robot as robotComm
import sys



#robot = robotComm.HC10('172.16.0.1')


robot = robotComm.HC10('172.16.0.1')

#incilizacija robota 


info = {}
if robot.ERROR_SUCCESS == robot.acquire_system_info(robot.SystemInfoType.R1, info):
    print("Robot version:")
    print(info)
    print("\n")
    
if robot.ERROR_SUCCESS != robot.reset_alarm(robot.RESET_ALARM_TYPE_ALARM):
    print("failed resetting alarms, err={}".format(hex(robot.errno)))
    
if robot.ERROR_SUCCESS != robot.switch_power(robot.POWER_TYPE_SERVO, robot.POWER_SWITCH_ON):
    print("failed turning on servo power supply, err={}".format(hex(robot.errno)))

# 0x3450 
status = {}
if robot.ERROR_SUCCESS == robot.get_status(status):
    print("Robot status:")
    print(status)
    print("\n")


# get last alarm 
'''
alarm = {}
if robot.ERROR_SUCCESS == robot.get_last_alarm(alarm):
    print("the last alarm: code={}, data={}, type={}, time={}, name={}"
            .format(hex(alarm['code']), alarm['data'], alarm['type'], alarm['time'], alarm['name']))
'''

# read IO:


group = 1 # general purpose input so 1 
stBit =1
var = robot.Variable(robot.VarType.IO, group)  
robot.read_variable(var)
print(var.val)
print((var.val >> stBit) & 1)


#set IO  - je potrebni preko joba  ( ne da se preko write_variable ker ni dovoljenja)

robot.select_job('GRIP_O')
robot.play_job()   

time.sleep(1)

robot.select_job('GRIP_C')
robot.play_job()   

time.sleep(1)


sys.exit()


# pisanje v INTEGER  (tip , stevilka , vrednost  )
var = robot.Variable(robot.VarType.INTEGER, 4, 5) # ON
robot.write_variable(var)



# pisanje v DOUBLE  (tip , stevilka , vrednost  )
var = robot.Variable(robot.VarType.DOUBLE, 9, 5) # ON
robot.write_variable(var)

# pisanje v REAL  (tip , stevilka , vrednost  )
var = robot.Variable(robot.VarType.REAL, 4, 5.2) # ON
robot.write_variable(var)

# pisanje v STRING  (tip , stevilka , vrednost  )
var = robot.Variable(robot.VarType.STRING, 4, "DA") # ON
robot.write_variable(var)

# branje INTEGER  4 
var = robot.Variable(robot.VarType.INTEGER, 4)  
robot.read_variable(var)
print(var.val)


print(robot.read_executing_job_info(status)) 
def move_complete():
    status = {}
     # se se robot premika je vrednost TRUE drugace fallse 
    if robot.ERROR_SUCCESS == robot.get_status(status):
        if status['running'] != True:
            return True
        
        else:
            return False
    return False




#polozaj robota  
pos_info = {}
robot_no = 1
if robot.ERROR_SUCCESS == robot.read_position(pos_info, robot_no):
    x, y, z, rx, ry, rz, re = pos_info['pos']
    str = "CURRENT POSITION\n" +\
            "COORDINATE {:12s} TOOL:{:02d}\n".format('ROBOT', pos_info['tool_no']) +\
            "R{} :X     {:4d}.{:03d} mm       Rx   {:4d}.{:04d} deg.\n".format(robot_no,
                x // 1000, x % 1000, rx // 10000, rx % 10000) +\
            "    Y     {:4d}.{:03d} mm       Ry   {:4d}.{:04d} deg.\n".format(
                y // 1000, y % 1000, ry // 10000, ry % 10000) +\
            "    Z     {:4d}.{:03d} mm       Rz   {:4d}.{:04d} deg.\n".format(
                z // 1000, z % 1000, rz // 10000, rz % 10000) +\
            "                            Re   {:4d}.{:04d} deg.\n".format(
                re // 10000, re % 10000)
print(str)           
print(pos_info['pos'])
 

#joint premik 
pos = (285322, -90436, 828644, 627561, -685637, -572033, 0)
robot.one_move(robot.MOVE_TYPE_JOINT_ABSOLUTE_POS, robot.MOVE_COORDINATE_SYSTEM_BASE, robot.MOVE_SPEED_CLASS_MILLIMETER, 1000, pos,tool_no=0,user_coor_no=0)
while(move_complete() != True):
    pass

# linearni  premik 
pos = (285317, -497481, 346729, 611456, -694230, -557122, 0)
robot.one_move(robot.MOVE_TYPE_LINEAR_ABSOLUTE_POS, robot.MOVE_COORDINATE_SYSTEM_BASE, robot.MOVE_SPEED_CLASS_MILLIMETER, 1000, pos,tool_no=0)
while(move_complete() != True):
    pass



#MOVE_TYPE_JOINT_ABSOLUTE_POS
# max hitrost je omejena 
"""

#joint premik 
pos = (285322, -90436, 828644, 627561, -685637, -572033, 0)
robot.one_move(robot.MOVE_TYPE_JOINT_ABSOLUTE_POS, robot.MOVE_COORDINATE_SYSTEM_BASE, robot.MOVE_SPEED_CLASS_MILLIMETER, 1000, pos,tool_no=0)
while(move_complete() != True):
    pass

# linearni  premik 
pos = (285317, -497481, 346729, 611456, -694230, -557122, 0)
robot.one_move(robot.MOVE_TYPE_LINEAR_ABSOLUTE_POS, robot.MOVE_COORDINATE_SYSTEM_BASE, robot.MOVE_SPEED_CLASS_MILLIMETER, 1000, pos,tool_no=0)
while(move_complete() != True):
    pass

"""
"""
# premik po tockah 
status = {}
if robot.ERROR_SUCCESS == robot.get_status(status):
    if not status['servo_on']:
        robot.switch_power(robot.POWER_TYPE_SERVO, robot.POWER_SWITCH_ON)
stops = [ (285322, -90436, 828644, 627561, -685637, -572033, 0),
           (285317, -497481, 346729, 611456, -694230, -557122, 0),
             (285322, -90436, 828644, 627561, -685637, -572033, 0),
            (285317, -497481, 346729, 611456, -694230, -557122, 0)]
robot.move(None, robot.MOVE_TYPE_JOINT_ABSOLUTE_POS, robot.MOVE_COORDINATE_SYSTEM_ROBOT, robot.MOVE_SPEED_CLASS_PERCENT, 2500, stops)
"""



