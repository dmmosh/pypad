from tkinter import *  # tkinter
from tkinter.font import Font # imports font
from pynput.keyboard import Key, Controller # imports key and controller
import dill
import os # imports os

from pmain import width
from pmain import height


'''
VARIABLE OBJECT
note: cant pickle tkinter objects

usually dont touch this but if something bad goes wrong..
here for backup
'''

var = {
    'win_w': width//6, # window width
    'win_h': height//10, #window height
    'loc_x': width-(int(width/5.7)), # x coordinate for the terminal window
    'loc_y': height -(int(height/6)), # y coordinate for the terminal window
    'hover_quit': False, #whether to quit when mouse goes out of box

    # theme settings
    'font': 'Source Code Pro,Source Code Pro Semibold', # terminal font
    'font_size': 17, # the font size
    'global_font': None, # will access element inside it, leave None rn
    'color_bg': 'Black', #default color for background
    'color_fg': 'White' # default color for text
    
}

