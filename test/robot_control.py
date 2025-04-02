import time
import lib.robot as robotComm

robot = robotComm.HC10('172.16.0.1')

def robot_init():
    

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


def read_IO():
    
    group = 1 # general purpose  input   so 1 
    #stBit =1
    var = robot.Variable(robot.VarType.IO, group)  
    robot.read_variable(var)
    print(var.val)
    #print((var.val >> stBit) & 1)
    return var.val


def set_IO():
    pass


def execute_job(name):
    robot.select_job(name)
    robot.play_job()

# format = "mm_deg" za koordinate v mm, deg
def current_position(format="a") -> tuple:
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
        
        x_mm = x // 1000 + x % 1000
        rx_deg = rx // 10000 + rx % 10000

        y_mm = y // 1000 + y % 1000
        ry_deg = ry // 10000 + ry % 10000

        z_mm = z // 1000 + z % 1000
        rz_deg = rz // 10000 + rz % 10000

        coords = (x, y, z, rx, ry, rz)
        coords_mm = (x_mm, y_mm, z_mm, rx_deg, ry_deg, rz_deg)
    else:
        print(robot.ERROR_SUCCESS)

    print(str)           
    print(pos_info['pos'])

    if format == "mm_deg":
        return coords_mm
    else:
        return coords

def moveJ(target_pos, speed=1000):
    pos = target_pos    #(285322, -90436, 828644, 627561, -685637, -572033, 0)
    robot.one_move(robot.MOVE_TYPE_JOINT_ABSOLUTE_POS, robot.MOVE_COORDINATE_SYSTEM_BASE, robot.MOVE_SPEED_CLASS_MILLIMETER, speed, pos,tool_no=0,user_coor_no=0)

def moveL(target_pos, speed=1000):
    pos = target_pos    #(285317, -497481, 346729, 611456, -694230, -557122, 0)
    robot.one_move(robot.MOVE_TYPE_LINEAR_ABSOLUTE_POS, robot.MOVE_COORDINATE_SYSTEM_BASE, robot.MOVE_SPEED_CLASS_MILLIMETER, speed, pos,tool_no=0)

def move_complete():
    status = {}
     # se se robot premika je vrednost TRUE drugace fallse 
    if robot.ERROR_SUCCESS == robot.get_status(status):
        if status['running'] != True:
            return True
        
        else:
            return False
    return False