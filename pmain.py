
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



def settings_window(): # only imports the settings class if it's called
    import putils
    putils.settings()



# TERMINAL WIDGET  
term = Frame(gl.r,
             background=gl.var['color_bg'],
             width=var['win_w']-100,
             height=var['win_h'])
term.pack(side=LEFT, expand=TRUE, fill=BOTH)
term.bind('<Num_Lock>', gl.quit_all)
term.focus_set()
wid = term.winfo_id()

# terminal buttons frame
term_btn = Frame(gl.r, 
                 background=gl.var['color_bg'])
term_btn.pack(side=RIGHT, anchor=NE)


# convert screen units to pixels
pixel = PhotoImage(width=20, height=20)

btn = {
    'quit': Button(term_btn, 
                    text='➥', 
                    command=gl.quit_all,
                    font=Font(size=20),
                    highlightcolor=gl.var['color_fg'],
                    highlightthickness=2,
                    highlightbackground=gl.var['color_fg'],
                    activebackground=gl.var['color_fg'],
                    activeforeground=gl.var['color_bg'],
                    image=pixel,
                    width=20,
                    height=20,
                    compound='c',
                    bg=gl.var['color_bg'], 
                    fg=gl.var['color_fg']),
    
    'settings': Button(term_btn, 
                    text='⚙', 
                    command=lambda: settings_window(),
                    font=Font(size=20),
                    highlightcolor=gl.var['color_fg'],
                    highlightthickness=2,
                    highlightbackground=gl.var['color_fg'],
                    activebackground=gl.var['color_fg'],
                    activeforeground=gl.var['color_bg'],
                    image=pixel,
                    width=20,
                    height=20,
                    compound='c',
                    bg=gl.var['color_bg'], 
                    fg=gl.var['color_fg']),
}

# clears the history hidden file
open(os.environ['HOME']+ '/.pypad', "a").truncate(50)

# terminal widget
# python runs libraries.py and automatically opens afterwards
# puts process's pid as arg 1 (will be deleting later)
os.system(f"""xterm  \\
          -fa \'{gl.var['font']}\' \\
          -fs {gl.var['font_size']} \\
          -rightbar \\
          -into {wid} \\
          -bg {gl.var['color_bg']} \\
          -fg {gl.var['color_fg']} \\
          -sb -e 'clear && /usr/bin/python -q -i {gl.dir_loc}/exec.py 2>&1 | tee -a {os.environ['HOME']}/.pypad && exit' &
          """)

# if theres num lock in the system
if 'Num Lock:    off' in os.popen("xset -q | grep Caps").read():
    key_c.press(key.Key.num_lock) # script presses num lock


if gl.var['auto_cursor'] == True:
    gl.r.update()
    gl.mouse_c.move(-10000,-10000)
    gl.mouse_c.move(term.winfo_rootx()+30, term.winfo_rooty()+30) # moves the mouse

btn['settings'].pack(side=TOP, anchor=NW)
btn['quit'].pack(side=TOP, anchor=NW)

# updates width anf height if needed, recursively
def window_size():
    print(gl.r.winfo_width(), gl.r.winfo_height())
    print(gl.width, gl.height)
    print('TERMINAL INFO: ', term.winfo_width(), term.winfo_height())
    if (gl.r.winfo_width() != var['win_w']):
        var['win_w'] = gl.r.winfo_width()
        
        os.system('pkill xterm')
        os.system(f"xterm -fa \'{gl.var['font']}\' -fs {gl.var['font_size']} -rightbar -into {wid} -bg {gl.var['color_bg']} -fg {gl.var['color_fg']} -sb -e 'clear && /usr/bin/python -q -i {gl.dir_loc}/exec.py && exit' &")


    gl.r.after(1000,window_size)

gl.r.after(1000,window_size) # calls the infinite check
gl.r.mainloop()  


