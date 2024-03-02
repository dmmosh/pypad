from math import * 
import time
#from numpy import *

# TRIES TO IMPORT SOME LIBRARIES

# QUIT AND EXIT FUNCTION OVERRIDE
#TODO: change what this closes
def quit():
    import os
    import sys
    os.system("pkill -9 -f pypad") #kills the pypad executable
    os.system("pkill -9 -f pmain.py") #kills the pypad file, REMOVE AFTER DEBUG
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
        global double_num
        if(double_num >= 2):
            print("JLDSJLDFH")
            quit()
        
        if key == Key.num_lock:
            print("NUM LOCK")
            double_num+=1
            time.sleep(1)
            double_num=0
        
    Listener( on_press=on_press).start() # key listener

    # starts the listener
