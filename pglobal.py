from tkinter import *  # tkinter
from tkinter import messagebox as mb
from tkinter.font import Font # imports font
from tkinter.ttk import Combobox
from pynput.keyboard import Key, Controller # imports key and controller
import pidfile as pf # checks if program is running
from os.path import exists
from psutil import pid_exists, Process, pids
import pickle
from mouse import move
import sys
import os # imports os
from os import environ

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


# COMPUTER INFORMATION
width, height = r.winfo_screenwidth(), r.winfo_screenheight() # gets width and height of the computer
#colors = pd.read_excel(dir_loc+"/data.xlsx") #reads the excel sheet of colors
#print(colors) # debug

var = pickle.load(open(dir_loc+'/var.obj', 'rb'))
var['global_font'] = Font(family=var['font'],  # sets global font to the font size as a font object
                        size=var['font_size'])