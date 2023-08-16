import tkinter as tk
from tkinter import *
import tkinter.font as font
 
# creating window
window = tk.Tk()
frame= Frame (window)
frame.pack()
 
# setting attribute
window.title("Air Canvas")


width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d"%(900,600))

leftbutton=Button(frame,text="Single Hand Recognition", height=600,width=60)
leftbutton.pack(side=LEFT)

rightbutton=Button(frame,text="Multiple Hand Recognition", height=600,width=60)
rightbutton.pack(side=RIGHT)
 
window.mainloop()