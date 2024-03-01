import sys
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

# key press 
def key_press(key):
    if key == k.Key.num_lock:
        exit()

def backspace():
    print("BACKSPACE ON")

try:
    from pynput import keyboard as k

    # keeps the listener on
    k.Listener( on_press=key_press).start()
    k.GlobalHotKeys({
        '<ctrl>+h': backspace
    }).join()

except:
    print("PYNPUT NOT FOUND. Quick escape not set. Consider typing \"os.system(\"pip install pynput\")\"")

