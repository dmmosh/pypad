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

print("fdkdjsfl")
try:
    from pynput.keyboard import Key, Listener, HotKey
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

    def on_activate():
        print('Global hotkey activated!')

    def for_canonical(f):
        return lambda k: f(l.canonical(k))

    hotkey = HotKey(
        HotKey.parse('<ctrl>+<alt>+h'),
        on_activate)
    with Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as l:
        l.join()