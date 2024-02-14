
from tkinter import * 
from tkinter import colorchooser as cc
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
        self.quit.pack()
        self.color.pack()
        self.settings.pack()
    

  

window_w = r.winfo_screenwidth()//4
window_h = r.winfo_screenheight()//10

r.attributes('-type', 'dialog')
r.geometry(f'{window_w}x{window_h}') 


main_box = Frame(r, height=window_h, width=window_w-50)
main_box.pack(side='top', anchor='nw', expand=YES)

wid = main_box.winfo_id()
os.system(f'xterm -into %d -fg white -bg black -geometry {window_w-50}x{window_h} -sb &' % wid)

#settings = Button(r, image=PhotoImage(file='./settings.png'), command=quit)
#settings.pack()
#color = Button(main_box, text="color", command=color)
#color.pack(side=TOP, anchor=NE)



r.mainloop()  