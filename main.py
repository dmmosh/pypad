
from tkinter import * 
from tkinter import messagebox as ms
from tkinter.simpledialog import askstring
import os




  
# ROOT WINDOW
r = Tk() 

window_w = r.winfo_screenwidth()//2
window_h = r.winfo_screenheight()//2

r.attributes('-type', 'dialog')
r.geometry(str(window_w)+'x'+str(window_h)) 

def quit():
    r.destroy()

termf = Frame(r, height=window_w, width=window_h)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry {}x{} -sb &'.format(window_w,window_h) % wid)

button = Button(r, text="quit", command=quit)
button.pack()
'''
ms.showinfo("showinfo", "Information") 
  
ms.showwarning("showwarning", "Warning") 
  
ms.showerror("showerror", "Error") 
  
ms.askquestion("askquestion", "Are you sure?") 
  
ms.askokcancel("askokcancel", "Want to continue?") 
  
ms.askyesno("askyesno", "Find the value?") 
  
ms.askretrycancel("askretrycancel", "Try again?")   
  
'''
r.mainloop()  