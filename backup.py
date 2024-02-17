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


