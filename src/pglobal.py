import sys
import os
from tkinter import * 
from tkinter.font import Font # imports font
from tkinter.ttk import Combobox


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from ..pypad._vendor.pynput import keyboard as key, mouse

import pickle
# GLOBAL VARIABLES
'''
NOTE: to change these, call pglobal.[variable]
'''
global dir_loc  # absolute helper files directory
global r # root window
global var # variable dict 
global width # window width
global height # window height
global real_width # absolute width, for multi-monitor
global real_height # absolute height, for multi-monitor
global mouse_c # mouse controller
global key_c # key controller

# ROOT WINDOW
r = Tk() 
# dir_locECTORY OF HELPER FILES
dir_loc = '/usr/share/pypad'
mouse_c = mouse.Controller()
key_c = key.Controller()
real_width = r.winfo_screenwidth()
real_height = r.winfo_screenheight()


def quit_all(arg=None):
    os.system("pkill -9 -f pypad")
    r.destroy()

# COMPUTER INFORMATION
res = str(os.popen("(xrandr  | grep \* | cut -d' ' -f4) | head -n 1").read()).replace('\n', '').split('x') # gets the resolution of current screen (in string form)
width, height = int(res[0]), int(res[1]) # gets width and height of the computer
#colors = pd.read_excel(dir_loc+"/data.xlsx") #reads the excel sheet of colors
#print(colors) # debug

var = pickle.load(open(dir_loc+'/var.obj', 'rb'))
var['global_font'] = Font(family=var['font'],  # sets global font to the font size as a font object
                        size=var['font_size'])


r.attributes('-type', 'dialog') # makes it a floating window
r.geometry(f"{ var['win_w'] }x{ var['win_h'] }+{ var['loc_x'] }+{ var['loc_y'] }") # locks it in bottom right
r.title('pypad') # gives the title
r.config(background=var['color_bg'], cursor='arrow') # sets background color
r.bind('<Num_Lock>', quit_all) # assigns num lock as quit
r.minsize(width=200, height=100)