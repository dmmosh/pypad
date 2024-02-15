
from tkinter import * 
from tkinter import colorchooser as cc
from tkterminal import Terminal
from numpy import array as arr

import os

# ROOT WINDOW
r = Tk() 


def quit():
    r.destroy()

def color():
    return cc.askcolor(title="background color:")

class buttons:
    def __init__(self):
        self.quit = Button(r, text="quit", command=quit)
        self.color = Button(r, text="color", command=color)
        self.settings = Button(r, image=PhotoImage(file='./settings.png'), command=quit)
    def pack_all(self):
        self.quit.pack(side=RIGHT, anchor=NE)
        self.color.pack(side=RIGHT, anchor=NE)
        self.settings.pack(side=RIGHT, anchor=NE)
    
  

window_w = r.winfo_screenwidth()//4
window_h = r.winfo_screenheight()//10

r.attributes('-type', 'dialog')
r.geometry(f'{window_w}x{window_h}') 


terminal = Terminal(pady=5, padx=5)
terminal.shell = True
terminal.pack(side=LEFT, anchor=NW)

#settings = Button(r, image=PhotoImage(file='./settings.png'), command=quit)
#settings.pack()
#set_img = PhotoImage(file='settings.png')


settings = Button(r, text="fdsf", command=quit)
settings.pack(side=RIGHT, anchor=NE)


r.mainloop()  