        self.sudo_pop = Toplevel(self.color)
        self.sudo_pop.geometry('400x300')
        self.sudo_pop.config(background=var['color_bg'])
        self.sudo_pop.attributes('-type', 'dialog') # makes it a floating window

        text(self.sudo_pop, 'Sudo access required.').pack(anchor=W, padx=7, pady=7)
        text(self.sudo_pop, 'Password:').pack(anchor=W, padx=7, pady=7)
        self.sudo_entry = Entry(self.sudo_pop, width = 150, font=var['global_font'], show='*')
        self.sudo_entry.pack(anchor=W, padx=7, pady=7)

        self.sudo_options = Frame(self.sudo_pop, bg=var['color_bg'])
        self.sudo_options.pack(side=BOTTOM)

        self.ok = make_btn(self.sudo_options, text='okie dokie ✓', command=lambda:self.get_sudo(self.sudo_entry.get()))
        self.cancel = make_btn(self.sudo_options, text='cancel X', command=lambda: quit(self.sudo_pop))

        self.cancel.pack(side= RIGHT, padx=7, pady=7)
        self.ok.pack(side=LEFT, padx=7, pady=7) 

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


    def set(input: bool):
        out = input


    # ok and cancel buttons
    ok = make_btn(options, text='okie dokie ✓', command=lambda: set(1))
    cancel = make_btn(options, text='cancel X', command=lambda: set(0))

    ok.pack(side=LEFT, padx=7, pady=7) 
    cancel.pack(side= RIGHT, padx=7, pady=7)
    
    out = -1 
    window.wait_variable(out)
    print(out)

    quit(box)
    return out

