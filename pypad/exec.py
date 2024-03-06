from math import * 
from ._vendor import pynput as pn
#from numpy import *

# TRIES TO IMPORT SOME LIBRARIES

# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    import os
    import sys
    os.system("pkill -9 -f pypad") #kills the pypad executable
    sys.exit()

def exit():
    quit()

def on_click(key:pn.Key) -> None:
    if key == pn.Key.num_lock:
        quit()
        
        
# starts the listener
pn.Listener( on_press=on_click).start() # key listener

