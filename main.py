
from tkinter import * 
from tkinter import messagebox as ms
from tkinter.simpledialog import askstring
import os




  
# ROOT WINDOW
r = Tk() 

window_w = r.winfo_screenwidth()//4
window_h = r.winfo_screenheight()//10

r.attributes('-type', 'dialog')
r.geometry(f'{window_w}x{window_h}') 

def quit():
    r.destroy()

termf = Frame(r, height=window_w, width=window_h)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system(f'xterm -into %d  -geometry {window_w}x{window_h} -sb &' % wid)

button = Button(r, text="quit", command=quit)
button.pack()


r.mainloop()  