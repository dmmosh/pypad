import os
import sys
from pynput import keyboard as key, mouse
from tkinter import * 
from tkinter.font import Font # imports font
from tkinter.ttk import Combobox
import pickle


r = Tk()

# TERMINAL WIDGET  
term = Frame(r)
term.pack(side=LEFT, expand=TRUE, fill=BOTH)
term.focus_set()
wid = term.winfo_id()

r.mainloop()