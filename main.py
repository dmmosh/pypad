
from tkinter import * 
from tkinter import messagebox as ms
from tkinter.simpledialog import askstring


  
# root window, make it hidden
# ms only
root = Tk() 
root.geometry("20x20") 
root.withdraw()
import os

  
w = Label(root, text ='GeeksForGeeks', font = "50")  
w.pack() 
  

name = askstring('Name', 'What is your name?')

ms.showinfo('Hello!', 'Hi, {}'.format(name))

'''
ms.showinfo("showinfo", "Information") 
  
ms.showwarning("showwarning", "Warning") 
  
ms.showerror("showerror", "Error") 
  
ms.askquestion("askquestion", "Are you sure?") 
  
ms.askokcancel("askokcancel", "Want to continue?") 
  
ms.askyesno("askyesno", "Find the value?") 
  
ms.askretrycancel("askretrycancel", "Try again?")   
  
'''

#root.mainloop()  
root.destroy()