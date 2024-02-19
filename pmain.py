import pglobal as gl
from pglobal import *

'''
SOURCE CODE

DEPENDENCIES:
xterm (no terminal without it)
pynput (will raise a warning if you dont have it) (for num lock fast quit)

NOTE:
the compiled executable will work as intended


BUG with uncompiled files:

ONLY UNCOMPILED VERSION EXPERIENCES THESE!!!
COMPILED EXECUTABLE RUNS WITHOUT ISSUES!!
i dont recommend running the program through python because of these issues

1. num lock doesnt automatically close the program when running through python
2. the program is closed, but the xterm client isnt. this eventually leads to a 
    "maximum number of clients reached" error. 
    to fix this, type 'killall python', killing all python xterm clients

'''

from putils import make_btn, quit_all  # imports make button function

def settings_window(): # only imports the settings class if it's called
    from putils import settings
    settings()




# terminal buttons frame
term_btn = Frame(gl.r)
term_btn.pack(side=RIGHT, anchor=NE)


btn = {
    'quit': make_btn(window=term_btn,
                     command=lambda: quit_all(),
                     text='➥',
                     font=Font(size=20)), #quit button

    'settings': make_btn(window=term_btn,
                         command=lambda:settings_window(), 
                         text='⚙',
                         font=Font(size=20)) #settings button
}

# assigns attributes to root window 
gl.r.attributes('-type', 'dialog') # makes it a floating window
gl.r.geometry(f"{ gl.var['win_w'] }x{ gl.var['win_h'] }+{ gl.var['loc_x'] }+{ gl.var['loc_y'] }") # locks it in bottom right
gl.r.title('pypad') # gives the title
gl.r.config(background=gl.var['color_bg']) # sets background color
gl.r.bind('<Num_Lock>', lambda event: quit_all()) # assigns num lock as quit


# if theres num lock in the system
if 'Num Lock:    off' in os.popen("xset -q | grep Caps").read():
    Controller().press(Key.num_lock) # script presses num lock

# if hover quit is on
if gl.var['hover_quit']:
    gl.r.bind('<Leave>', lambda event: quit_all())


# TERMINAL WIDGET  
term = Frame(gl.r, height=gl.var['win_h'], width=gl.var['win_w']-50)
term.pack(side=LEFT, anchor=NW, expand=TRUE)
term.bind('<Num_Lock>', lambda event: quit_all())
term.focus_set()
wid = term.winfo_id()

# terminal widget
# python runs libraries.py and automatically opens afterwards
# puts process's pid as arg 1 (will be deleting later)
os.system(f"xterm -fa \'{gl.var['font']}\' -fs {gl.var['font_size']} -rightbar -into {wid} -bg {gl.var['color_bg']} -fg {gl.var['color_fg']} -sb -e 'clear && /usr/bin/python -q -i {gl.dir_loc}/exec.py && exit' &")



if gl.var['auto_cursor'] == True:
    gl.r.update()
    move(term.winfo_rootx()+30, term.winfo_rooty()+30) # moves the mouse

term_btn = Frame(gl.r, height=gl.var['win_h'], width=50)
term_btn.pack(side=RIGHT)

btn['settings'].pack(anchor=N)
btn['quit'].pack(anchor=N)

gl.r.mainloop()  
