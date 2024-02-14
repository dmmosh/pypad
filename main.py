
from tkinter import * 
from tkinter import colorchooser as cc

import os

# ROOT WINDOW
r = Tk() 

def quit():
    r.destroy()

def color():
    return cc.askcolor(title="background color:")


  

window_w = r.winfo_screenwidth()//4
window_h = r.winfo_screenheight()//10

r.attributes('-type', 'dialog')
r.geometry(f'{window_w}x{window_h}') 


termf = Frame(r, height=window_w, width=window_h)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system(f'xterm -into %d -fg white -bg black -geometry {window_w}x{window_h} -sb &' % wid)


button = Button(r, text="quit", command=quit)
button.pack()


r.mainloop()  