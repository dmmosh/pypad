
from tkinter import * 
from tkinter import messagebox as ms
from tkinter.simpledialog import askstring


  
# root window, make it hidden
# ms only
r = Tk() 
r.geometry("20x20") 
r.attributes('-type', 'dialog')

def quit():
    r.destroy()

button = Button(r, text="quit", command=quit())
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