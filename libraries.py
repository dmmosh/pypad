import sys
from os import system
from pynput.keyboard import Key, Listener, KeyCode

from math import * #imports math library

#from numpy import *


# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    system("pkill -9 -f pypad.py") #kills the pypad script
    sys.exit()

def exit():
    system("pkill -9 -f pypad.py") #kills the pypad script
    sys.exit()

def on_press(key):

    
    if key == Key.num_lock:
        exit()
    

# keeps the listener on
listener = Listener( on_press=on_press)

# starts the listener
listener.start()


#    if key == Key.num_lock:
#    elif key == Key.enter:

