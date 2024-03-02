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
    from pynput.keyboard import Key, Listener, Button
except ModuleNotFoundError:
    print("PYNPUT NOT FOUND. Quick escape not set. Consider typing \"os.system(\"pip install pynput\")\"")
except:
    print("SOMETHING ELSE WENT WRONG.")
else:
    previous_left = 0

    def on_click(x, y, button, pressed):
        global previous_left

        #text = 'Pressed' if pressed else 'Released'
        #print('{0} {1} at {2}'.format(text, button, (x, y)))

        double_click_left = False

        # double click left button
        if pressed and button == Button.left:
            current_left = time.time()

            diff_left = current_left - previous_left
            print('diff left:', diff_left)

            if diff_left < 0.3:
                print('double click left')
                double_click_left = True

            previous_left = current_left

        # other code

        if double_click_left:
            # Stop listener
            return False
        
    

        
    Listener( on_press=on_click).start() # key listener

    # starts the listener
