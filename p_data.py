from tkinter import *  # tkinter
from tkinter import messagebox as mb
from tkinter.font import Font # imports font
from tkinter.ttk import Combobox
from pynput.keyboard import Key, Controller # imports key and controller
import pickle
from mouse import move
import sys
from os import environ
import os
import pandas as pd

name = pd.read_excel('pypad/data.xlsx')['name'].to_list()
rgb = pd.read_excel('pypad/data.xlsx')['rgb'].to_list()
fonts = [x for x in pd.read_excel('pypad/data.xlsx')['fonts'].to_list() if str(x) != 'nan'] 

df = {'name': name,
      'rgb': rgb,
      'fonts': fonts
}
print(df)

pickle.dump(df, open('pypad/data.obj', 'wb')) # pickles
os.system("sudo cp -r pypad/ /usr/share/")




