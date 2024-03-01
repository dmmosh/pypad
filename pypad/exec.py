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
    quit()

def test():
    print("fdkjlk")

try:
    from pynput.keyboard import Key, Listener, GlobalHotKeys
except ModuleNotFoundError:
    print("PYNPUT NOT FOUND. Quick escape not set. Consider typing \"os.system(\"pip install pynput\")\"")
except:
    print("SOMETHING ELSE WENT WRONG.")
else:
    def on_press(key):
        if key == Key.num_lock:
            exit()
        
    #listener = Listener( on_press=on_press)

    # starts the listener
    #listener.start()

    GlobalHotKeys({
        '<num_lock>+h': test
    }).start()