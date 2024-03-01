import pickle 
import os
import sys 


def quit():
    os.system("pkill -9 -f pypad") #kills the pypad executable
    sys.exit()

def exit():
    os.system("pkill -9 -f pypad") #kills the pypad executable
    sys.exit()


pickle.dump(quit, open('pypad/fun.obj', 'wb'))
pickle.dump(exit, open('pypad/fun.obj', 'wb'))

#quit = pickle.load(open('pypad/var.obj', 'rb'))
#exit = pickle.load(open('pypad/var.obj', 'rb'))