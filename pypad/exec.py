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

def on_activate():
    '''Defines what happens on press of the hotkey'''
    k.type('Kind regards, John Smith, Sales Manager.')

def for_canonical(hotkey):
    '''Removes any modifier state from the key events 
    and normalises modifiers with more than one physical button'''
    return lambda k: hotkey(k.Listener.canonical(k))

'''Creating the hotkey'''
hotkey = k.HotKey(
k.HotKey.parse('<shift>+k'), 
on_activate)

    
try:
    from pynput import keyboard as k

    # keeps the listener on
    k.Listener( on_press=key_press).start()
    
    with k.Listener(
            on_press=for_canonical(hotkey.press),
            on_release=for_canonical(hotkey.release)) as listener:
        listener.join()


except:
    print("PYNPUT NOT FOUND. Quick escape not set. Consider typing \"os.system(\"pip install pynput\")\"")

