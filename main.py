
from tkinter import * 
from tkinter import colorchooser as cc

import os

# ROOT WINDOW
r = Tk() 

def quit():
    r.destroy()

def color():
    return cc.askcolor(title="background color:")

class btn:
    def __init__(self) -> None:
        self.quit = Button(r, text="quit", command=quit)
        self.color = Button(r, text="color", command=color)
        self.settings = Button(r, image=PhotoImage(file='./settings.png'), command=quit)
  

window_w = r.winfo_screenwidth()//4
window_h = r.winfo_screenheight()//10

r.attributes('-type', 'dialog')
r.geometry(f'{window_w}x{window_h}') 


termf = Frame(r, height=window_h, width=window_w-50)

termf.pack(side='left', expand=YES)
wid = termf.winfo_id()
os.system(f'xterm -into %d -fg white -bg black -geometry {window_w}x{window_h} -sb &' % wid)


btn_quit = Button(r, text="quit", command=quit)


btn_quit.pack()


r.mainloop()  