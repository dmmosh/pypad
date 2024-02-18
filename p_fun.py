from tkinter import *  # tkinter
from tkinter.font import Font # imports font
from pynput.keyboard import Key, Controller # imports key and controller
import dill
import os # imports os


dir = '/usr/share/pypad'

'''
FUNCTIONS IN PICKLE !!
'''


# any variables that need pickling
from pmain import gl.var

def quit(window):
    window.destroy()

def get_from_dict(input:dict, key):
    return input[key]

def sys(cmd:str):
    return os.popen(cmd).read()

# opens new window
def new_window(title:str, geometry:str) -> Toplevel:
    out = Toplevel(r)
    out.title(title)
    out.geometry(geometry)
    out.attributes('-type', 'dialog')
    return out


def make_btn(window=r, text="", command=lambda:quit(), font=None, image=None, width =None, height =None):
    out = Button(window, 
                  text=text, 
                  command=command, 
                  highlightcolor=gl.var['color_fg'],
                  highlightthickness=2,
                  highlightbackground=gl.var['color_fg'],
                  activebackground=gl.var['color_fg'],
                  activeforeground=gl.var['color_bg'],
                  
                  bg=gl.var['color_bg'], 
                  fg=gl.var['color_fg'])
    # if width and height are given
    if width and height :
        out.config(width=width)
        out.config(height=height)
    
    # if image is given
    if image:
        out.config(image=image)
    
    # if font is given
    if font:
        out.config(font=font)
    # if font isnt given (cant pass as default parameter)
    else:
        out.config(font=gl.var['global_font'])
    
    return out


# opens the color window
def settings_window():
    color = new_window('colors', '300x400')
    color.config(background=gl.var['color_bg'])
    #color.bind('<Num_Lock>', lambda: quit(color))
    color.bind('<Escape>', lambda event:quit(color))



    buttons = Frame(color, bg=gl.var['color_bg'])
    buttons.pack(side=BOTTOM)

    save = make_btn(window=buttons, text='save', command=lambda:quit(color))
    save.pack(side=LEFT, padx=10, pady=10)

    cancel = make_btn(window=buttons, text='cancel', command=lambda:quit(color))
    cancel.pack(side=RIGHT, padx=10, pady=10)

