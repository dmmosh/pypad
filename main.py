
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




width, height = r.winfo_screenwidth(), r.winfo_screenheight()



    
btn = {
    'quit': Button(r, text='quit', command=quit),
    'color': Button(r, text='color', command=color),
    'settings': Button(r, image=PhotoImage(file='./settings.png'), command=quit)
}

var = {
    'win_w': width//6, # window width
    'win_h': height//10, #window height
    'color_bg': 'black', #default color for background
    'color_fg': 'white', # default color for text
    'loc_x': width-(int(width/5.7)), # x coordinate for the terminal window
    'loc_y': height -(int(height/6)) # y coordinate for the terminal window
}
#var['loc_x'] = (r.winfo_screenwidth()//2) - (var['win_w']//2)
#var['loc_y'] = (r.winfo_screenheight()//2) - (var['win_h']//2)

r.attributes('-type', 'dialog')
r.geometry(f"{ var['win_w'] }x{ var['win_h'] }+{ var['loc_x'] }+{ var['loc_y'] }") 
#r.wm_maxsize(width=win_w*2, height=win_h)
#r.wm_minsize(width=win_w//4, height=win_h)

term = Frame(r, height=var['win_h'], width=var['win_w']-50)
term.pack(side=LEFT, anchor=NW, expand=YES)
wid = term.winfo_id()
os.system(f"xterm -rightbar -into %d -geometry {var['win_h']}x{var['win_w']-50} -fs 30 -bg {var['color_bg']} -fg {var['color_fg']} -sb &" % wid)

#settings = Button(r, image=PhotoImage(file='./settings.png'), command=quit)
#settings.pack()
#set_img = PhotoImage(file='settings.png')


settings = Button(r, text='fdsf', command=quit)
settings.pack(side=RIGHT, anchor=NE)

r.mainloop()  