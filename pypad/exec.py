import sys
import readline
import os
from math import * 
#from numpy import *

# TRIES TO IMPORT SOME LIBRARIES

# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    os.system("pkill -9 -f pypad") #kills the pypad executable
    
    sys.exit()

def exit():
    os.system("pkill -9 -f pypad") #kills the pypad executable
    sys.exit()

def on_press(key):
    if key == Key.num_lock:
        exit()
    

try:
    from pynput.keyboard import Key, Listener, KeyCode

    # keeps the listener on
    listener = Listener( on_press=on_press)

    # starts the listener
    listener.start()
except:
    print("PYNPUT NOT FOUND. Quick escape not set. Consider typing \"os.system(\"pip install pynput\")\"")