from pglobal import *
import pglobal as gl


'''
SOURCE CODE

REQUIREMENTS:
xterm

NOTE:
the final build will be a compiled, polished executable
will probably run faster too
make sure to repurpose the dir_locectories for a linux executable in /usr/bin rather than the project dir_loc


python file bug:
python script doesnt close automatically when typing quit()/exit() or pressing num lock
compiled file doesnt have the problem
'''

def load_var():
    # GLOBAL VARIABLES
    var = pickle.load(open(dir_loc + '/var.obj', 'rb'))
    #pickle.dump(var, open('pypad/var.obj', 'wb')) # pickles
    #NOTE: pickle doesnt support tkinter,
    var['global_font'] = Font(family=var['font'],  # sets global font to the font size as a font object
                              size=var['font_size'])

# dumps the variables
def dump_var():
    var['global_font'] = None
    pickle.dump(var, open(dir_loc+'/var.obj', 'wb'))

# OTHER FUNCTIONS / CLASSEES
# quits the program
def quit(window):
    window.destroy()

# gets output of a system command
def sys_out(cmd:str):
    return os.popen(cmd).read()

# makes a new text object
def text(window=gl.r, input:str = "", width=None, height=None) -> Text:
    out = Label(window, 
                 font=gl.var['global_font'], 
                 text=input,
                 background=gl.var['color_bg'],
                 foreground=gl.var['color_fg'])
    if width:
        out.config(width=width)
    if height:
        out.config(height=height)

    return out

# opens new window
def new_window(title:str, geometry:str) -> Toplevel:
    out = Toplevel(gl.r)
    out.title(title)
    out.geometry(geometry)
    out.attributes('-type', 'dialog')
    return out


# error message
def msg_box(message:str = "Error", title:str = 'ERROR', width:int = 300, height:int = 200):
    box = Toplevel(gl.r)
    box.geometry(f'{width}x{height}')
    box.config(background=gl.var['color_bg'])
    box.attributes('-type', 'dialog') # makes it a floating window
    box.bind('<Escape>', lambda event:quit(box))
    box.title(title)

    text(window=box, input=message, width=width).pack()

    ok = make_btn(box, text='okie dokie ✓', command=lambda:quit(box))

    ok.pack(side=BOTTOM, padx=7, pady=7) 

# yes or no prompt
def yes_or_no(window = gl.r, message:str = "Yes or no?", width:int = 300, height:int = 200) -> int:
    box = Toplevel(window, background=gl.var['color_bg'])
    box.geometry(f'{width}x{height}')
    box.attributes('-type', 'dialog') # makes it a floating window
    box.bind('<Escape>', lambda event:quit(box))
    box.title('Yes or no?')

    gl.var['global_font'] = Font(family=gl.var['font'],   # have to set the font manually, resets in the saving process
                            size=gl.var['font_size'])

    # have to manually make the text because it resets
    text(box, message).pack(side=TOP)
    

    # options frame
    options = Frame(box, bg=gl.var['color_bg'])
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
def make_btn(window=gl.r, text="", command=lambda:quit(), font=None, image=None, width =None, height =None):
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
    if width and gl.height :
        out.config(width=width)
        out.config(height=gl.height)
    
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


# color window class
class settings:

    def __init__(self):
        # SETTINGS WINDOW ITSELF
        self.settings = new_window('colors', '500x800')
        self.settings.config(background=gl.var['color_bg'])
        #color.bind('<Num_Lock>', lambda: quit(color))
        self.settings.bind('<Escape>', lambda event:quit(self.settings))
        self.settings.title('Settings')

        # FRAMES
        self.bottom_btn = Frame(self.settings, bg=gl.var['color_bg'])
        self.bottom_btn.pack(side=BOTTOM)

        self.top_btn = Frame(self.settings, bg=gl.var['color_bg'])
        self.top_btn.pack(side=TOP)

        self.options = Frame(self.settings, bg=gl.var['color_bg'])
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

        self.all_colors = list(pickle.load(open(gl.dir_loc+'/data.obj', 'rb'))['name']) # imports the colors
        #print(self.all_colors)
        self.drop_bg = Combobox(self.options, 
                                values=self.all_colors, 
                                font=gl.var['global_font'],
                                background=gl.var['color_fg'],
                                foreground=gl.var['color_bg'])
        self.drop_bg.current(self.all_colors.index(gl.var['color_bg']))
        self.drop_bg.pack(anchor=W)


    # SAVES ALL THE VALUES
    def save(self):
        # if python throws an exception error
        try:
            gl.var['color_bg'] = self.all_colors[self.drop_bg.current()]
            gl.var['global_font'] = None # cant pickle tkinter objects
            dump_var()
        except:
            msg_box('Cannot save due to lacking permissions.\nTry running \"sudo chown $USER /usr/share/pypad/\"', width=700, height=150)
        else:

            if yes_or_no(message='Settings saved.\nRestart now?') == 1:
                quit(gl.r)
                os.execl(sys.executable, sys.executable, *sys.argv)
            


    #DEFAULTS ALL THE VALUES
    def default(self):
        try:
            pickle.dump(pickle.load(open(gl.dir_loc + '/default_var.obj', 'rb')), open(gl.dir_loc+'/var.obj', 'wb'))
        except:
            msg_box('Cannot save due to lacking permissions.\nTry running \"sudo chown $USER /usr/share/pypad/\"', width=700, height=150)
        else:
            
            if yes_or_no(message='\nSettings saved.\nRestart now?') == 1:
                quit(gl.r)
                os.execl(sys.executable, sys.executable, *sys.argv)

