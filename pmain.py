from tkinter import *  # tkinter
from tkinter import messagebox as mb
from tkinter.font import Font # imports font
from tkinter.ttk import Combobox
from pynput.keyboard import Key, Controller # imports key and controller
import pickle
from mouse import move
import sys
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
global dir 
dir = '/usr/share/pypad'

# ROOT WINDOW
global r
r = Tk() 


# FUNCTIONS

# quits the program
def quit(window):
    window.destroy()

# loads the variables
def load_var():
    global var
    var = pickle.load(open(dir+'/var.obj', 'rb'))
    #pickle.dump(var, open('pypad/var.obj', 'wb')) # pickles
    #NOTE: pickle doesnt support tkinter,

    var['global_font'] = Font(family=var['font'],  # sets global font to the font size as a font object
                          size=var['font_size'])

# dumps the variables
def dump_var():
    pickle.dump(var, open(dir+'/var.obj', 'wb'))


# gets output of a system command
def sys_out(cmd:str):
    return os.popen(cmd).read()

# makes a new text object
def text(window=r, input:str = "", width=None, height=None) -> Text:
    out = Label(window, 
                 font=var['global_font'], 
                 text=input,
                 background=var['color_bg'],
                 foreground=var['color_fg'])
    if width:
        out.config(width=width)
    if height:
        out.config(height=height)

    return out

# opens new window
def new_window(title:str, geometry:str) -> Toplevel:
    out = Toplevel(r)
    out.title(title)
    out.geometry(geometry)
    out.attributes('-type', 'dialog')
    return out


# error message
def msg_box(message:str = "Error", title:str = 'ERROR', width:int = 300, height:int = 200):
    box = Toplevel(r)
    box.geometry(f'{width}x{height}')
    box.config(background=var['color_bg'])
    box.attributes('-type', 'dialog') # makes it a floating window
    box.bind('<Escape>', lambda event:quit(box))
    box.title(title)

    text(window=box, input=message, width=width).pack()

    ok = make_btn(box, text='okie dokie ✓', command=lambda:quit(box))

    ok.pack(side=BOTTOM, padx=7, pady=7) 

# yes or no prompt
def yes_or_no(window = r, message:str = "Yes or no?", width:int = 300, height:int = 200) -> int:
    box = Toplevel(window, background=var['color_bg'])
    box.geometry(f'{width}x{height}')
    box.attributes('-type', 'dialog') # makes it a floating window
    box.bind('<Escape>', lambda event:quit(box))
    box.title('Yes or no?')

    var['global_font'] = Font(family=var['font'],   # have to set the font manually, resets in the saving process
                            size=var['font_size'])

    # have to manually make the text because it resets
    text(box, message).pack(side=TOP)
    

    # options frame
    options = Frame(box, bg=var['color_bg'])
    options.pack(side=BOTTOM)



    # ok and cancel buttons
    ok = make_btn(options, text='okie dokie ✓', command=lambda: out.set(1))
    cancel = make_btn(options, text='cancel X', command=lambda: out.set(0))

    ok.pack(side=LEFT, padx=7, pady=7) 
    cancel.pack(side= RIGHT, padx=7, pady=7)
    
    out = IntVar(value=-1)

    window.wait_variable(out)


    quit(box)
    return out.get()


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
        self.settings = new_window('colors', '500x800')
        self.settings.config(background=var['color_bg'])
        #color.bind('<Num_Lock>', lambda: quit(color))
        self.settings.bind('<Escape>', lambda event:quit(self.settings))
        self.settings.title('Settings')

        # FRAMES
        self.bottom_btn = Frame(self.settings, bg=var['color_bg'])
        self.bottom_btn.pack(side=BOTTOM)

        self.top_btn = Frame(self.settings, bg=var['color_bg'])
        self.top_btn.pack(side=TOP)

        self.options = Frame(self.settings, bg=var['color_bg'])
        self.options.pack()

        # BOTTOM BUTTONS
        self.save_btn = make_btn(window=self.bottom_btn, 
                             text='save ✓',
                             command=lambda:self.save())
        self.cancel_btn = make_btn(window=self.bottom_btn, 
                               text='cancel X', 
                               command=lambda:quit(self.settings))
        self.default_btn = make_btn(window=self.bottom_btn, 
                                text='default ⟳',
                                command=lambda:self.default())
        
        # TOP BUTTONS
        self.theme_btn = make_btn(window=self.top_btn, 
                             text='theme ↓',
                             command=lambda:self.theme())
        self.resolution_btn = make_btn(window=self.top_btn, 
                             text='resolution ↓',
                             command=lambda:self.resolution())
        
        
        # PACKS BOTTOM BUTTONS
        self.save_btn.pack(side=LEFT, padx=7, pady=7)
        self.default_btn.pack(side=RIGHT, padx=7, pady=7)
        self.cancel_btn.pack(padx=7, pady=7)

        # PACKS TOP BUTTONS
        self.theme_btn.pack(side=LEFT, padx=7, pady=7)
        self.resolution_btn.pack(side=RIGHT, padx=7, pady=7)

        # ALL SETTINGS BUTTONS (will pack later)
        
        # RESOLUTION BUTTONS




        # THEME BUTTONS

        self.all_colors = list(pickle.load(open(dir+'/data.obj', 'rb'))['name']) # imports the colors
        #print(self.all_colors)
        self.drop_bg = Combobox(self.options, 
                                values=self.all_colors, 
                                font=var['global_font'],
                                background=var['color_fg'],
                                foreground=var['color_bg'])
        self.drop_bg.current(self.all_colors.index(var['color_bg']))
        self.drop_bg.pack(anchor=W)


    # SAVES ALL THE VALUES
    def save(self):
        # if python throws an exception error
        try:
            var['color_bg'] = self.all_colors[self.drop_bg.current()]
            var['global_font'] = None # cant pickle tkinter objects
            dump_var()
        except:
            msg_box('Cannot save due to lacking permissions.\nTry running \"sudo chown $USER /usr/share/pypad/\"', width=700, height=150)
        else:

            if yes_or_no(message='Settings saved.\nRestart now?') == 1:
                quit(r)
                os.execl(sys.executable, sys.executable, *sys.argv)
            


    #DEFAULTS ALL THE VALUES
    def default(self):
        # try putting all values to default
        try:
            var = {
            # resolution, general settings
            'win_w': width//6, # window width
            'win_h': height//10, #window height
            'loc_x': width-(int(width/5.7)), # x coordinate for the terminal window
            'loc_y': height -(int(height/6)), # y coordinate for the terminal window
            'hover_quit': False, #whether to quit when mouse goes out of box
            'auto_cursor': True,
            # theme settings
            'font': 'Source Code Pro,Source Code Pro Semibold', # terminal font
            'font_size': 17, # the font size
            'global_font': None, # will access element inside it, leave None rn
            'color_bg': 'Black', #default color for background
            'color_fg': 'White' # default color for text
            }
            dump_var()
        # error cant serialize
        except:
            msg_box('Cannot default due to lacking permissions.\nTry running \"sudo chown $USER /usr/share/pypad/\"', width=700, height=150)
        else:
            if yes_or_no(message='Settings defaulted.\nRestart now?') == 1:
                quit(r)
                os.execl(sys.executable, sys.executable, *sys.argv)




    

# COMPUTER INFORMATION
width, height = r.winfo_screenwidth(), r.winfo_screenheight() # gets width and height of the computer
#colors = pd.read_excel(dir+"/data.xlsx") #reads the excel sheet of colors
#print(colors) # debug

load_var()




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
if 'Num Lock:    off' in sys_out("xset -q | grep Caps"):
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
    move(term.winfo_rootx()+30, term.winfo_rooty()+30) # moves the mouse

term_btn = Frame(r, height=var['win_h'], width=50)
term_btn.pack(side=RIGHT)

btn['settings'].pack(anchor=N)
btn['quit'].pack(anchor=N)

r.mainloop()  
