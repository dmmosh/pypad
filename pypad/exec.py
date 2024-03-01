from math import * 
#from numpy import *

# TRIES TO IMPORT SOME LIBRARIES

# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    import os
    import sys
    os.system("pkill -9 -f pypad") #kills the pypad executable
    os.system("pkill -9 -f pmain.py") #kills the pypad executable
    sys.exit()

def exit():
    quit()


try:
    from pynput.keyboard import Key, Listener
except ModuleNotFoundError:
    print("PYNPUT NOT FOUND. Quick escape not set. Consider typing \"os.system(\"pip install pynput\")\"")
except:
    print("SOMETHING ELSE WENT WRONG.")
else:
    def on_press(key):
        if key == Key.num_lock:
            exit()
        
    Listener( on_press=on_press).start() # key listener

    # starts the listener
