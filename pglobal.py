from tkinter import *  # tkinter
from tkinter import messagebox as mb
from tkinter.font import Font # imports font
from tkinter.ttk import Combobox
from pynput.keyboard import Key, Controller # imports key and controller
import pickle
from mouse import move
import sys
import os # imports os

# GLOBAL VARIABLES
global dir 
global r
global var
global width
global height

# ROOT WINDOW
r = Tk() 
# DIRECTORY OF HELPER FILES
dir = '/usr/share/pypad'


# COMPUTER INFORMATION
width, height = r.winfo_screenwidth(), r.winfo_screenheight() # gets width and height of the computer
#colors = pd.read_excel(dir+"/data.xlsx") #reads the excel sheet of colors
#print(colors) # debug

def load_var():
    # GLOBAL VARIABLES
    var = pickle.load(open(dir + '/var.obj', 'rb'))
    #pickle.dump(var, open('pypad/var.obj', 'wb')) # pickles
    #NOTE: pickle doesnt support tkinter,
    var['global_font'] = Font(family=var['font'],  # sets global font to the font size as a font object
                              size=var['font_size'])

# dumps the variables
def dump_var():
    var['global_font'] = None
    pickle.dump(var, open(dir+'/var.obj', 'wb'))

var = load_var()
