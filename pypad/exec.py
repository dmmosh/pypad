import sys
import os
#from numpy import *

from math import *

libraries = []

# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    os.system("pkill -9 -f pypad") #kills the pypad executable

    sys.exit()

def exit():
    os.system("pkill -9 -f pypad") #kills the pypad executable
    sys.exit()


# MAKES SURE THAT PYNPUT IS INSTALLED 
# if not, can't execute fast num lock exit
try:
    from pynput.keyboard import Key, Listener, KeyCode
except:
    print("Pynput not found. Quick Num lock escape not possible. Consider installing pynput by typing \"pip install pynput\"")
else:
    def on_press(key):
        if key == Key.num_lock:
            exit()
    # keeps the listener on
    listener = Listener( on_press=on_press)

    # starts the listener
    listener.start()



