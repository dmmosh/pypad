
from tkinter import * 
from tkinter import colorchooser as cc
from tkterm import Terminal
from numpy import array as arr

import os


'''
SOURCE CODE

clear && /usr/bin/python -q

'''

# ROOT WINDOW
r = Tk() 


def quit():
    r.destroy()

def color():
    return cc.askcolor(title='background color:')

    
btn = {
    'quit': Button(r, text='quit', command=quit),
    'color': Button(r, text='color', command=color),
    'settings': Button(r, image=PhotoImage(file='./settings.png'), command=quit)
}

var = {
    'win_w': r.winfo_screenwidth()//4,
    'win_h': r.winfo_screenheight()//10,
    'color_bg': 'black',
    'color_fg': 'white',
    'loc_x': 100,
    'loc_y': 10
}


r.attributes('-type', 'dialog')
r.geometry(f"{ var['win_w'] }x{ var['win_h'] }+{ var['loc_x'] }+{ var['loc_y'] }") 
#r.wm_maxsize(width=win_w*2, height=win_h)
#r.wm_minsize(width=win_w//4, height=win_h)

term = Frame(r, height=var['win_h'], width=var['win_w']-50)
term.pack(side=LEFT, anchor=NW, expand=YES)
wid = term.winfo_id()
os.system(f"xterm -rightbar -into %d -geometry {var['win_h']}x{var['win_w']-50} -bg {var['color_bg']} -fg {var['color_fg']} -sb &" % wid)

#settings = Button(r, image=PhotoImage(file='./settings.png'), command=quit)
#settings.pack()
#set_img = PhotoImage(file='settings.png')


settings = Button(r, text='fdsf', command=quit)
settings.pack(side=RIGHT, anchor=NE)


r.mainloop()  