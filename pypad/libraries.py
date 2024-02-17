import sys
from pynput.keyboard import Key, Listener, KeyCode
import os
from math import * 
#from numpy import *


# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    os.system("pkill -9 -f pypad && pkill -9 -f pmain.py") #kills the pypad executable

    sys.exit()

def exit():
    os.system("pkill -9 -f pypad && pkill -9 -f pmain.py") #kills the pypad executable
    sys.exit()

def on_press(key):
    if key == Key.num_lock:
        exit()
    

# keeps the listener on
listener = Listener( on_press=on_press)

# starts the listener
listener.start()



