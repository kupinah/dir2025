#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#    Dec 03, 2019 10:53:51 AM CST  platform: Windows NT

from fs100 import FS100
import os
import threading
import time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import pendant_support


def destroy_root():
    global w, root
    root.destroy()

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    root.protocol("WM_DELETE_WINDOW", destroy_root)
    w = top
    pendant_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    pendant_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Microsoft JhengHei UI} -size 9 -weight "  \
            "normal -slant roman -underline 0 -overstrike 0"

        if __name__ == '__main__':
            top.geometry("724x516+576+207")
            top.title("New Toplevel")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")

        self.position_text = tk.Text(top)
        self.position_text.place(relx=0.221, rely=0.155, relheight=0.388
                , relwidth=0.558)
        self.position_text.configure(background="white")
        self.position_text.configure(font="-family {Monospace} -size 10")
        if os.name == 'nt':
            self.position_text.configure(font="-family {Consolas} -size 11")
        self.position_text.configure(foreground="black")
        self.position_text.configure(highlightbackground="#d9d9d9")
        self.position_text.configure(highlightcolor="black")
        self.position_text.configure(insertbackground="black")
        self.position_text.configure(selectbackground="#c4c4c4")
        self.position_text.configure(selectforeground="black")
        self.position_text.configure(state='disabled')
        self.position_text.configure(width=404)
        self.position_text.configure(wrap="word")

        self.X_minus = tk.Button(top)
        self.X_minus.place(relx=0.028, rely=0.155, height=31, width=60)
        self.X_minus.configure(activebackground="#ececec")
        self.X_minus.configure(activeforeground="#000000")
        self.X_minus.configure(background="#d9d9d9")
        self.X_minus.configure(disabledforeground="#a3a3a3")
        self.X_minus.configure(foreground="#000000")
        self.X_minus.configure(highlightbackground="#d9d9d9")
        self.X_minus.configure(highlightcolor="black")
        self.X_minus.configure(pady="0")
        self.X_minus.configure(text='''X-''')

        self.X_plus = tk.Button(top)
        self.X_plus.place(relx=0.124, rely=0.155, height=31, width=60)
        self.X_plus.configure(activebackground="#ececec")
        self.X_plus.configure(activeforeground="#000000")
        self.X_plus.configure(background="#d9d9d9")
        self.X_plus.configure(disabledforeground="#a3a3a3")
        self.X_plus.configure(foreground="#000000")
        self.X_plus.configure(highlightbackground="#d9d9d9")
        self.X_plus.configure(highlightcolor="black")
        self.X_plus.configure(pady="0")
        self.X_plus.configure(text='''X+''')

        self.Y_plus = tk.Button(top)
        self.Y_plus.place(relx=0.124, rely=0.252, height=31, width=60)
        self.Y_plus.configure(activebackground="#ececec")
        self.Y_plus.configure(activeforeground="#000000")
        self.Y_plus.configure(background="#d9d9d9")
        self.Y_plus.configure(disabledforeground="#a3a3a3")
        self.Y_plus.configure(foreground="#000000")
        self.Y_plus.configure(highlightbackground="#d9d9d9")
        self.Y_plus.configure(highlightcolor="black")
        self.Y_plus.configure(pady="0")
        self.Y_plus.configure(text='''Y+''')

        self.Y_minus = tk.Button(top)
        self.Y_minus.place(relx=0.028, rely=0.252, height=31, width=60)
        self.Y_minus.configure(activebackground="#ececec")
        self.Y_minus.configure(activeforeground="#000000")
        self.Y_minus.configure(background="#d9d9d9")
        self.Y_minus.configure(disabledforeground="#a3a3a3")
        self.Y_minus.configure(foreground="#000000")
        self.Y_minus.configure(highlightbackground="#d9d9d9")
        self.Y_minus.configure(highlightcolor="black")
        self.Y_minus.configure(pady="0")
        self.Y_minus.configure(text='''Y-''')

        self.Z_plus = tk.Button(top)
        self.Z_plus.place(relx=0.124, rely=0.349, height=31, width=60)
        self.Z_plus.configure(activebackground="#ececec")
        self.Z_plus.configure(activeforeground="#000000")
        self.Z_plus.configure(background="#d9d9d9")
        self.Z_plus.configure(disabledforeground="#a3a3a3")
        self.Z_plus.configure(foreground="#000000")
        self.Z_plus.configure(highlightbackground="#d9d9d9")
        self.Z_plus.configure(highlightcolor="black")
        self.Z_plus.configure(pady="0")
        self.Z_plus.configure(text='''Z+''')

        self.Z_minus = tk.Button(top)
        self.Z_minus.place(relx=0.028, rely=0.349, height=31, width=60)
        self.Z_minus.configure(activebackground="#ececec")
        self.Z_minus.configure(activeforeground="#000000")
        self.Z_minus.configure(background="#d9d9d9")
        self.Z_minus.configure(disabledforeground="#a3a3a3")
        self.Z_minus.configure(foreground="#000000")
        self.Z_minus.configure(highlightbackground="#d9d9d9")
        self.Z_minus.configure(highlightcolor="black")
        self.Z_minus.configure(pady="0")
        self.Z_minus.configure(text='''Z-''')

        self.E_plus = tk.Button(top)
        self.E_plus.place(relx=0.124, rely=0.446, height=31, width=60)
        self.E_plus.configure(activebackground="#ececec")
        self.E_plus.configure(activeforeground="#000000")
        self.E_plus.configure(background="#d9d9d9")
        self.E_plus.configure(disabledforeground="#a3a3a3")
        self.E_plus.configure(foreground="#000000")
        self.E_plus.configure(highlightbackground="#d9d9d9")
        self.E_plus.configure(highlightcolor="black")
        self.E_plus.configure(pady="0")
        self.E_plus.configure(text='''E+''')

        self.E_minus = tk.Button(top)
        self.E_minus.place(relx=0.028, rely=0.446, height=31, width=60)
        self.E_minus.configure(activebackground="#ececec")
        self.E_minus.configure(activeforeground="#000000")
        self.E_minus.configure(background="#d9d9d9")
        self.E_minus.configure(disabledforeground="#a3a3a3")
        self.E_minus.configure(foreground="#000000")
        self.E_minus.configure(highlightbackground="#d9d9d9")
        self.E_minus.configure(highlightcolor="black")
        self.E_minus.configure(pady="0")
        self.E_minus.configure(text='''E-''')

        self.Rx_minus = tk.Button(top)
        self.Rx_minus.place(relx=0.787, rely=0.155, height=31, width=60)
        self.Rx_minus.configure(activebackground="#ececec")
        self.Rx_minus.configure(activeforeground="#000000")
        self.Rx_minus.configure(background="#d9d9d9")
        self.Rx_minus.configure(disabledforeground="#a3a3a3")
        self.Rx_minus.configure(foreground="#000000")
        self.Rx_minus.configure(highlightbackground="#d9d9d9")
        self.Rx_minus.configure(highlightcolor="black")
        self.Rx_minus.configure(pady="0")
        self.Rx_minus.configure(text='''Rx-''')

        self.Rx_plus = tk.Button(top)
        self.Rx_plus.place(relx=0.884, rely=0.155, height=31, width=60)
        self.Rx_plus.configure(activebackground="#ececec")
        self.Rx_plus.configure(activeforeground="#000000")
        self.Rx_plus.configure(background="#d9d9d9")
        self.Rx_plus.configure(disabledforeground="#a3a3a3")
        self.Rx_plus.configure(foreground="#000000")
        self.Rx_plus.configure(highlightbackground="#d9d9d9")
        self.Rx_plus.configure(highlightcolor="black")
        self.Rx_plus.configure(pady="0")
        self.Rx_plus.configure(text='''Rx+''')

        self.Ry_minus = tk.Button(top)
        self.Ry_minus.place(relx=0.787, rely=0.252, height=31, width=60)
        self.Ry_minus.configure(activebackground="#ececec")
        self.Ry_minus.configure(activeforeground="#000000")
        self.Ry_minus.configure(background="#d9d9d9")
        self.Ry_minus.configure(disabledforeground="#a3a3a3")
        self.Ry_minus.configure(foreground="#000000")
        self.Ry_minus.configure(highlightbackground="#d9d9d9")
        self.Ry_minus.configure(highlightcolor="black")
        self.Ry_minus.configure(pady="0")
        self.Ry_minus.configure(text='''Ry-''')

        self.Ry_plus = tk.Button(top)
        self.Ry_plus.place(relx=0.884, rely=0.252, height=31, width=60)
        self.Ry_plus.configure(activebackground="#ececec")
        self.Ry_plus.configure(activeforeground="#000000")
        self.Ry_plus.configure(background="#d9d9d9")
        self.Ry_plus.configure(disabledforeground="#a3a3a3")
        self.Ry_plus.configure(foreground="#000000")
        self.Ry_plus.configure(highlightbackground="#d9d9d9")
        self.Ry_plus.configure(highlightcolor="black")
        self.Ry_plus.configure(pady="0")
        self.Ry_plus.configure(text='''Ry+''')

        self.Rz_minus = tk.Button(top)
        self.Rz_minus.place(relx=0.787, rely=0.349, height=31, width=60)
        self.Rz_minus.configure(activebackground="#ececec")
        self.Rz_minus.configure(activeforeground="#000000")
        self.Rz_minus.configure(background="#d9d9d9")
        self.Rz_minus.configure(disabledforeground="#a3a3a3")
        self.Rz_minus.configure(foreground="#000000")
        self.Rz_minus.configure(highlightbackground="#d9d9d9")
        self.Rz_minus.configure(highlightcolor="black")
        self.Rz_minus.configure(pady="0")
        self.Rz_minus.configure(text='''Rz-''')

        self.Rz_plus = tk.Button(top)
        self.Rz_plus.place(relx=0.884, rely=0.349, height=31, width=60)
        self.Rz_plus.configure(activebackground="#ececec")
        self.Rz_plus.configure(activeforeground="#000000")
        self.Rz_plus.configure(background="#d9d9d9")
        self.Rz_plus.configure(disabledforeground="#a3a3a3")
        self.Rz_plus.configure(foreground="#000000")
        self.Rz_plus.configure(highlightbackground="#d9d9d9")
        self.Rz_plus.configure(highlightcolor="black")
        self.Rz_plus.configure(pady="0")
        self.Rz_plus.configure(text='''Rz+''')

        self.speed = tk.Scale(top, from_=0.0, to=2.0)
        self.speed.place(relx=0.304, rely=0.64, relwidth=0.301, relheight=0.0
                , height=23, bordermode='ignore')
        self.speed.configure(activebackground="#ececec")
        self.speed.configure(background="#d9d9d9")
        self.speed.configure(font=font9)
        self.speed.configure(foreground="#000000")
        self.speed.configure(highlightbackground="#d9d9d9")
        self.speed.configure(highlightcolor="black")
        self.speed.configure(orient="horizontal")
        self.speed.configure(showvalue="0")
        self.speed.configure(tickinterval="1.0")
        self.speed.configure(troughcolor="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.221, rely=0.63, height=25, width=53)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Speed:''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.318, rely=0.678, height=25, width=203)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''1                    5                    10''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.221, rely=0.678, height=25, width=57)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''(deg/s)''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.214, rely=0.581, height=25, width=67)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''(mm/s)''')

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.318, rely=0.591, height=25, width=203)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''1                   10                   50''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.0, rely=0.078, height=25, width=173)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Max. 90mm per move''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.773, rely=0.078, height=25, width=163)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Max. 18deg per move''')

        self.reset_alarm = tk.Button(top)
        self.reset_alarm.place(relx=0.622, rely=0.562, height=101, width=120)
        self.reset_alarm.configure(activebackground="#ececec")
        self.reset_alarm.configure(activeforeground="#000000")
        self.reset_alarm.configure(background="#d9d9d9")
        self.reset_alarm.configure(disabledforeground="#a3a3a3")
        self.reset_alarm.configure(foreground="#000000")
        self.reset_alarm.configure(highlightbackground="#d9d9d9")
        self.reset_alarm.configure(highlightcolor="black")
        self.reset_alarm.configure(pady="0")
        self.reset_alarm.configure(text='''RESET ALARM''')

        # manual added
        self.robot = FS100('172.16.0.1')
        self.stop_sign = threading.Semaphore()

        self.position_text.bind("<<update>>", self.update_pos_ui)
        self.X_plus.bind("<Button-1>", self.start_move)
        self.X_plus.bind("<ButtonRelease-1>", self.stop_move)
        self.X_minus.bind("<Button-1>", self.start_move)
        self.X_minus.bind("<ButtonRelease-1>", self.stop_move)
        self.Y_plus.bind("<Button-1>", self.start_move)
        self.Y_plus.bind("<ButtonRelease-1>", self.stop_move)
        self.Y_minus.bind("<Button-1>", self.start_move)
        self.Y_minus.bind("<ButtonRelease-1>", self.stop_move)
        self.Z_plus.bind("<Button-1>", self.start_move)
        self.Z_plus.bind("<ButtonRelease-1>", self.stop_move)
        self.Z_minus.bind("<Button-1>", self.start_move)
        self.Z_minus.bind("<ButtonRelease-1>", self.stop_move)
        self.E_plus.bind("<Button-1>", self.start_move)
        self.E_plus.bind("<ButtonRelease-1>", self.stop_move)
        self.E_minus.bind("<Button-1>", self.start_move)
        self.E_minus.bind("<ButtonRelease-1>", self.stop_move)
        self.Rx_plus.bind("<Button-1>", self.start_move)
        self.Rx_plus.bind("<ButtonRelease-1>", self.stop_move)
        self.Rx_minus.bind("<Button-1>", self.start_move)
        self.Rx_minus.bind("<ButtonRelease-1>", self.stop_move)
        self.Ry_plus.bind("<Button-1>", self.start_move)
        self.Ry_plus.bind("<ButtonRelease-1>", self.stop_move)
        self.Ry_minus.bind("<Button-1>", self.start_move)
        self.Ry_minus.bind("<ButtonRelease-1>", self.stop_move)
        self.Rz_plus.bind("<Button-1>", self.start_move)
        self.Rz_plus.bind("<ButtonRelease-1>", self.stop_move)
        self.Rz_minus.bind("<Button-1>", self.start_move)
        self.Rz_minus.bind("<ButtonRelease-1>", self.stop_move)
        self.reset_alarm.configure(command=self.on_reset_alarm)

        # display the robot position on screen
        self.position_text.after(50, lambda dlg: dlg.position_text.event_generate("<<update>>"), self)
        # set 'reset alarm' button state
        self.is_alarmed()

    def on_reset_alarm(self):
        self.robot.reset_alarm(FS100.RESET_ALARM_TYPE_ALARM)
        time.sleep(0.1)
        # reflect the ui
        self.is_alarmed()

    def update_pos_ui(self, event):
        pos_info = {}
        robot_no = 1
        if FS100.ERROR_SUCCESS == self.robot.read_position(pos_info, robot_no):
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
            event.widget.configure(state='normal')
            event.widget.delete('1.0', tk.END)
            event.widget.insert('1.0', str)
            event.widget.configure(state='disabled')

    def update_pos(self):
        while self.stop_sign.acquire(blocking=False):
            self.position_text.event_generate("<<update>>")
            self.stop_sign.release()
            # let button up take effect
            time.sleep(0.02)

    def is_alarmed(self):
        alarmed = False
        status = {}
        if FS100.ERROR_SUCCESS == self.robot.get_status(status):
            alarmed = status['alarming']
        if alarmed:
            self.reset_alarm.configure(state='normal')
        else:
            self.reset_alarm.configure(state='disabled')
        return alarmed

    def start_move(self, event):
        MAX_XYZ = 90000
        MAX_R_XYZE = 180000
        SPEED_XYZ = (10, 100, 500)
        SPEED_R_XYZE = (10, 50, 100)
        x, y, z, rx, ry, rz, re = 0, 0, 0, 0, 0, 0, 0

        axis = event.widget.cget("text")
        if axis == 'X+':
            x = MAX_XYZ
        elif axis == 'X-':
            x = -MAX_XYZ
        elif axis == 'Y+':
            y = MAX_XYZ
        elif axis == 'Y-':
            y = -MAX_XYZ
        elif axis == 'Z+':
            z = MAX_XYZ
        elif axis == 'Z-':
            z = -MAX_XYZ
        elif axis == 'Rx+':
            rx = MAX_R_XYZE
        elif axis == 'Rx-':
            rx = -MAX_R_XYZE
        elif axis == 'Ry+':
            ry = MAX_R_XYZE
        elif axis == 'Ry-':
            ry = -MAX_R_XYZE
        elif axis == 'Rz+':
            rz = MAX_R_XYZE
        elif axis == 'Rz-':
            rz = -MAX_R_XYZE
        elif axis == 'E+':
            re = MAX_R_XYZE
        elif axis == 'E-':
            re = -MAX_R_XYZE

        if x != 0 or y != 0 or z != 0:
            speed_class = FS100.MOVE_SPEED_CLASS_MILLIMETER
            speed = SPEED_XYZ[self.speed.get()]
        else:
            speed_class = FS100.MOVE_SPEED_CLASS_DEGREE
            speed = SPEED_R_XYZE[self.speed.get()]
        pos = (x, y, z, rx, ry, rz, re)

        status = {}
        if FS100.ERROR_SUCCESS == self.robot.get_status(status):
            if not status['servo_on']:
                self.robot.switch_power(FS100.POWER_TYPE_SERVO, FS100.POWER_SWITCH_ON)

        self.pos_updater = threading.Thread(target=self.update_pos)
        if FS100.ERROR_SUCCESS == self.robot.one_move(FS100.MOVE_TYPE_LINEAR_INCREMENTAL_POS,
                                                      FS100.MOVE_COORDINATE_SYSTEM_ROBOT, speed_class, speed, pos):
            time.sleep(0.1)  # robot may not update the status
            if not self.is_alarmed():
                self.pos_updater.start()

    def stop_move(self, event):
        self.stop_sign.acquire()

        while self.pos_updater.is_alive():
            pass

        self.robot.switch_power(FS100.POWER_TYPE_HOLD, FS100.POWER_SWITCH_ON)
        # a hold off in case we switch to teach/play mode
        self.robot.switch_power(FS100.POWER_TYPE_HOLD, FS100.POWER_SWITCH_OFF)

        # the position of robot in still
        self.position_text.event_generate("<<update>>")

        self.stop_sign.release()


if __name__ == '__main__':
    vp_start_gui()
