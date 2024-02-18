from pglobal import *

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


# ROOT WINDOW
r = Tk() 
# dir_locECTORY OF HELPER FILES
dir_loc = '/usr/share/pypad'


# COMPUTER INFORMATION
width, height = r.winfo_screenwidth(), r.winfo_screenheight() # gets width and height of the computer
#colors = pd.read_excel(dir_loc+"/data.xlsx") #reads the excel sheet of colors
#print(colors) # debug

var = load_var()

# OTHER FUNCTIONS / CLASSEES
# quits the program
def quit(window):
    window.destroy()

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

        self.all_colors = list(pickle.load(open(dir_loc+'/data.obj', 'rb'))['name']) # imports the colors
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
        try:
            pickle.dump(pickle.load(open(dir_loc + '/default_var.obj', 'rb')), open(dir_loc+'/var.obj', 'wb'))
        except:
            msg_box('Cannot save due to lacking permissions.\nTry running \"sudo chown $USER /usr/share/pypad/\"', width=700, height=150)
        else:
            
            if yes_or_no(message='Settings saved.\nRestart now?') == 1:
                quit(r)
                os.execl(sys.executable, sys.executable, *sys.argv)

