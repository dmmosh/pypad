from putils import *


# LOAD VARIABLES
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
