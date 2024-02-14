
from tkinter import * 
from tkinter import messagebox as ms
from tkinter.simpledialog import askstring
import os




  
# ROOT WINDOW
r = Tk() 

screen_w = r.winfo_screenwidth()
screen_h = r.winfo_screenheight()

r.attributes('-type', 'dialog')
r.geometry(str(screen_w//2)+'x'+str(screen_h//2)) 

def quit():
    r.destroy()

termf = Frame(r, height=400, width=500)

termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 40x20 -sb &' % wid)

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