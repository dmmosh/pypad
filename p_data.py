from tkinter import *  # tkinter
from tkinter import messagebox as mb
from tkinter.font import Font # imports font
from tkinter.ttk import Combobox
from pynput.keyboard import Key, Controller # imports key and controller
import pickle
from mouse import move
import sys
import os # imports os
import pandas as pd

df = pd.read_excel('pypad/data.xlsx').to_dict()
print(df)

pickle.dump(df, open('pypad/data.obj', 'wb')) # pickles
os.system("sudo cp -r pypad/ /usr/share/")




