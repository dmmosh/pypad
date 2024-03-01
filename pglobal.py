from tkinter import *  # tkinter
from tkinter.font import Font # imports font
from tkinter.ttk import Combobox
from pynput.keyboard import Key, Controller # imports key and controller
import pidfile as pf # checks if program is running
from os.path import exists
import pickle
from mouse import move
import sys
from os import environ
import os # imports os

# GLOBAL VARIABLES
'''
NOTE: to change these, call pglobal.[variable]
'''
global dir_loc 
global r
global var
global width
global height

# ROOT WINDOW
r = Tk() 
# dir_locECTORY OF HELPER FILES
dir_loc = '/usr/share/pypad'

def quit_all():
    os.system("pkill -9 -f pypad")
    r.quit()
    r.destroy()

# COMPUTER INFORMATION
width, height = r.winfo_screenwidth(), r.winfo_screenheight() # gets width and height of the computer
#colors = pd.read_excel(dir_loc+"/data.xlsx") #reads the excel sheet of colors
#print(colors) # debug

var = pickle.load(open(dir_loc+'/var.obj', 'rb'))
var['global_font'] = Font(family=var['font'],  # sets global font to the font size as a font object
                        size=var['font_size'])


r.attributes('-type', 'dialog') # makes it a floating window
r.geometry(f"{ var['win_w'] }x{ var['win_h'] }+{ var['loc_x'] }+{ var['loc_y'] }") # locks it in bottom right
r.title('pypad') # gives the title
r.config(background=var['color_bg'], cursor='arrow') # sets background color
r.bind('<Num_Lock>', lambda event: quit_all()) # assigns num lock as quit
r.minsize(width=200, height=100)