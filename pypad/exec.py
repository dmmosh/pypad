from math import * 
import sys
from time import sleep, time
sys.path.append('/usr/share/pypad/')
from _vendor.pynput.keyboard import Key, Listener
#from numpy import *

# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    import os
    os.system("pkill -9 -f pypad") #kills the pypad executable
    sys.exit()

def exit():
    quit()

# checks for a double num lock press
time_pass = 0
def on_click(key:Key) -> None:
    global time_pass
    if key == Key.num_lock:
        diff = time()-time_pass
        if (diff < 0.5):
                #print(time_pass, time())
                quit()
        else:
            time_pass = time()
        
# starts the listener
Listener( on_press=on_click).start() # key listener

