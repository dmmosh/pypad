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

    
try:
    from pynput.keyboard import Controller, Listener, HotKey, Key

except:
    print("PYNPUT NOT FOUND. Quick escape not set. Consider typing \"os.system(\"pip install pynput\")\"")
else: 
    c = Controller()


def press_callback():
    try:
        c.release(Key.shift)  # update - undo the shift, otherwise all type will be Uppercase
        c.press(Key.backspace)  # update - Undo the K of the shift-k
        c.type("Kind regards ")
    except AttributeError:
        pass


    def for_canonical(f):
        return lambda k: f(l.canonical(k))


    hk = HotKey(HotKey.parse('<shift>+k'), on_activate=press_callback)

    with Listener(on_press=for_canonical(hk.press), on_release=for_canonical(hk.release)) as l:
        l.join()
    # keeps the listener on
    Listener( on_press=key_press).start()

    


