import sys
import os
from pynput.keyboard import Key, Listener, KeyCode

import math
from math import sqrt
from math import e
from math import log
from math import log10
from math import log2
from math import factorial
from math import floor
from math import ceil
from math import isfinite
from math import cbrt
from math import sin
from math import pow
from math import cos
from math import tan
from math import pi
from math import degrees
from math import radians


# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    os.system("pkill -9 -f pypad.py") #kills the pypad script
    sys.exit()

def exit():
    os.system("pkill -9 -f pypad.py") #kills the pypad script
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

