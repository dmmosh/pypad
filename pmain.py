from tkinter import *  # tkinter
from tkinter.font import Font # imports font
from pynput.keyboard import Key, Controller # imports key and controller
import pickle
import mouse
import os # imports os


'''
SOURCE CODE

REQUIREMENTS:
xterm

NOTE:
the final build will be a compiled, polished executable
will probably run faster too
make sure to repurpose the directories for a linux executable in /usr/bin rather than the project dir


python file bug:
python script doesnt close automatically when typing quit()/exit() or pressing num lock
compiled file doesnt have the problem
'''
#TODO: change to '/usr/share'
dir = '/usr/share/pypad'

# ROOT WINDOW
r = Tk() 


# FUNCTIONS

# quits the program
def quit(window):
    window.destroy()


# gets output of a system command
def sys(cmd:str):
    return os.popen(cmd).read()

# opens new window
def new_window(title:str, geometry:str) -> Toplevel:
    out = Toplevel(r)
    out.title(title)
    out.geometry(geometry)
    out.attributes('-type', 'dialog')
    return out

# makes a button
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


# color window class
class settings:

    def __init__(self):
        # SETTINGS WINDOW ITSELF
        self.color = new_window('colors', '500x800')
        self.color.config(background=var['color_bg'])
        #color.bind('<Num_Lock>', lambda: quit(color))
        self.color.bind('<Escape>', lambda event:quit(self.color))


        # BUTTONS OPTIONS 
        self.bottom_btn = Frame(self.color, 
                                bg=var['color_bg'])
        self.bottom_btn.pack(side=BOTTOM)
        self.top_btn = Frame(self.color, 
                             bg=var['color_bg'])
        self.top_btn.pack(side=TOP)

        # BOTTOM BUTTONS
        self.save = make_btn(window=self.bottom_btn, 
                             height=10, 
                             text='save',
                             command=lambda:quit(self.color))
        self.cancel = make_btn(window=self.bottom_btn, 
                               text='cancel', 
                               command=lambda:quit(self.color))
        self.default = make_btn(window=self.bottom_btn, 
                                text='default',
                                command=lambda:quit(self.color))
        
        # packs bottom buttons
        self.save.pack(side=LEFT, padx=10, pady=10)
        self.default.pack(side=RIGHT, padx=10, pady=10)
        self.cancel.pack(padx=10, pady=10)


        # ALL SETTINGS BUTTONS (will pack later)
        
        # RESOLUTION BUTTONS


        # THEME BUTTONS


    def resolution(self):
        pass

    def theme(self):
        pass

    def save(self):
        pass


    

# COMPUTER INFORMATION
width, height = r.winfo_screenwidth(), r.winfo_screenheight() # gets width and height of the computer
#colors = pd.read_excel(dir+"/data.xlsx") #reads the excel sheet of colors
#print(colors) # debug


var = pickle.load(open(dir+'/var.obj', 'rb'))

#pickle.dump(var, open('pypad/var.obj', 'wb')) # pickles
#NOTE: pickle doesnt support tkinter,

var['global_font'] = Font(family=var['font'],  # sets global font to the font size as a font object
                          size=var['font_size'])




# terminal buttons frame
term_btn = Frame(r)
term_btn.pack(side=RIGHT, anchor=NE)


btn = {
    'quit': make_btn(window=term_btn,
                     command=lambda: quit(r),
                     text='➥',
                     font=Font(size=20)), #quit button

    'settings': make_btn(window=term_btn,
                         command=lambda:settings(), 
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
term.pack(side=LEFT, anchor=NW, expand=TRUE)
term.bind('<Num_Lock>', lambda event: quit(r))
term.focus_set()
wid = term.winfo_id()

# terminal widget
# python runs libraries.py and automatically opens afterwards
os.system(f"xterm -fa \'{var['font']}\' -fs {var['font_size']} -rightbar -into {wid} -geometry {var['win_h']}x{var['win_w']-50} -bg {var['color_bg']} -fg {var['color_fg']} -sb -e 'clear && /usr/bin/python -q -i {dir}/libraries.py && exit' &")


if var['auto_cursor'] == True:
    r.update()
    mouse.move(term.winfo_rootx()+30, term.winfo_rooty()+30) # moves the mouse

term_btn = Frame(r, height=var['win_h'], width=50)
term_btn.pack(side=RIGHT)

btn['settings'].pack(anchor=N)
btn['quit'].pack(anchor=N)

r.mainloop()  
