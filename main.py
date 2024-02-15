
from tkinter import * 
from tkinter import colorchooser as cc
from tkterm import Terminal
from numpy import array as arr

import os


'''
SOURCE CODE

clear && /usr/bin/python -q
X11

'''

# ROOT WINDOW
r = Tk() 


# FUNCTIONS
def quit(any):
    r.destroy()

def color():
    return cc.askcolor(title='background color:')

def sys(input:str) ->str:
    return os.popen(input).read()



dir = sys('pwd')

width, height = r.winfo_screenwidth(), r.winfo_screenheight()




var = {
    'win_w': width//6, # window width
    'win_h': height//10, #window height
    'color_bg': 'black', #default color for background
    'color_fg': 'white', # default color for text
    'loc_x': width-(int(width/5.7)), # x coordinate for the terminal window
    'loc_y': height -(int(height/6)), # y coordinate for the terminal window

    'hover_quit': False #whether to quit when mouse goes out of box
}

img = {
    'settings': PhotoImage(file='./settings.png', width=20, height=20)
}
    
btn = {
    'quit': Button(r, text='quit', command=quit),
    'color': Button(r, text='color', command=color),
    'settings': Button(r, image=img['settings'], command=quit)
}
#var['loc_x'] = (r.winfo_screenwidth()//2) - (var['win_w']//2)
#var['loc_y'] = (r.winfo_screenheight()//2) - (var['win_h']//2)

r.attributes('-type', 'dialog')
r.geometry(f"{ var['win_w'] }x{ var['win_h'] }+{ var['loc_x'] }+{ var['loc_y'] }") 
r.title('pypad')

if var['hover_quit']:
    r.bind('<Leave>', quit)

term = Frame(r, height=var['win_h'], width=var['win_w']-50)
#term = Text(r, height=var['win_h'], width=var['win_w']-50)
term.pack(side=LEFT, anchor=NW)
wid = term.winfo_id()

os.system(f"xterm -fa 'Monospace' -fs 17 -rightbar -into {wid} -geometry {var['win_h']}x{var['win_w']-50} -bg {var['color_bg']} -fg {var['color_fg']} -sb -e 'clear && /usr/bin/python -q && exit' &")


    
#settings = Button(r, image=PhotoImage(file='./settings.png'), command=quit)
#settings.pack()
#set_img = PhotoImage(file='settings.png')

btn['settings'].pack(side=RIGHT, anchor=NE)

r.mainloop()  
