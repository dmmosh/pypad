
from tkinter import * 
from tkinter import colorchooser as cc
from tkinter.font import Font
from tkterm import Terminal
from pynput.keyboard import Key, Controller
import pandas as pd
import os


'''
SOURCE CODE

clear && /usr/bin/python -q
X11
NOTE:
the final build will be a compiled, polished executable
will probably run faster too
make sure to repurpose the directories for a linux executable in /usr/bin rather than the project dir

'''

# ROOT WINDOW
r = Tk() 



# FUNCTIONS

# quits the program
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
                  highlightcolor=var['color_fg'],
                  highlightthickness=2,
                  highlightbackground=var['color_fg'],
                  activebackground=var['color_fg'],
                  activeforeground=var['color_bg'],
                  
                  bg=var['color_bg'], 
                  fg=var['color_fg'])
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
        out.config(font=var['global_font'])
    
    return out


# opens the color window
def color_window():
    color = new_window('colors', '300x400')
    color.config(background=var['color_bg'])
    #color.bind('<Num_Lock>', lambda: quit(color))
    color.bind('<Escape>', lambda event:quit(color))



    buttons = Frame(color, bg=var['color_bg'])
    buttons.pack(side=BOTTOM)

    save = make_btn(window=buttons, text='save', command=lambda:quit(color))
    save.pack(side=LEFT, padx=10, pady=10)

    cancel = make_btn(window=buttons, text='cancel', command=lambda:quit(color))
    cancel.pack(side=RIGHT, padx=10, pady=10)

    
    

# COMPUTER INFORMATION
dir = os.path.dirname(os.path.realpath(__file__))
width, height = r.winfo_screenwidth(), r.winfo_screenheight() # gets width and height of the computer
#colors = pd.read_excel(dir+"/data.xlsx") #reads the excel sheet of colors
#print(colors) # debug

print(os.system("pwd"))

var = {
    'win_w': width//6, # window width
    'win_h': height//10, #window height
    'loc_x': width-(int(width/5.7)), # x coordinate for the terminal window
    'loc_y': height -(int(height/6)), # y coordinate for the terminal window
    'hover_quit': False, #whether to quit when mouse goes out of box



    # theme settings
    'font': 'Source Code Pro,Source Code Pro Semibold', # terminal font
    'font_size': 17, # the font size
    'global_font': None, # will access element inside it, leave None rn
    'color_bg': colors.at[0,'name'], #default color for background
    'color_fg': colors.at[15,'name'] # default color for text
    
}
var['global_font'] = Font(family=var['font'],  # sets global font to the font size as a font object
                          size=var['font_size'])


# terminal buttons frame
term_btn = Frame(r)
term_btn.pack(side=RIGHT, anchor=NE)


btn = {
    'quit': make_btn(command=lambda: quit(r),
                     text='➥',
                     font=Font(size=20)), #quit button

    'settings': make_btn(command=lambda:color_window(), 
                         text='⚙',
                         font=Font(size=20)) #settings button
}

# assigns attributes to root window 
r.attributes('-type', 'dialog') # makes it a floating window
r.geometry(f"{ var['win_w'] }x{ var['win_h'] }+{ var['loc_x'] }+{ var['loc_y'] }") # locks it in bottom right
r.title('pypad') # gives the title
r.config(background=var['color_bg']) # sets background color
r.bind('<Num_Lock>', lambda event: quit(r)) # assigns num lock as quit


# if theres num lock in the system
if 'Num Lock:    off' in sys("xset -q | grep Caps"):
    Controller().press(Key.num_lock) # script presses num lock

# if hover quit is on
if var['hover_quit']:
    r.bind('<Leave>', lambda event: quit(r))


# TERMINAL WIDGET 
term = Frame(r, height=var['win_h'], width=var['win_w']-50)
term.pack(side=LEFT, anchor=NW)
term.focus_set()
wid = term.winfo_id()

# terminal widget
# python runs libraries.py and automatically opens afterwards
os.system(f"xterm -fa \'{var['font']}\' -fs {var['font_size']} -rightbar -into {wid} -geometry {var['win_h']}x{var['win_w']-50} -bg {var['color_bg']} -fg {var['color_fg']} -sb -e 'clear && /usr/bin/python -q -i {dir}/libraries.py && exit' &")




btn['settings'].pack(anchor=NE)
btn['quit'].pack(anchor=E)

r.mainloop()  
