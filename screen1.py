import tkinter as tk
from tkinter import *
import tkinter.font as font
import sys
import subprocess
import os
 
# creating window
window = tk.Tk()
frame= Frame (window)
frame.pack()
 
# setting attribute
window.title("Air Canvas")

width= window.winfo_screenwidth()               
height= window.winfo_screenheight()               
window.geometry("%dx%d" % (900,1000))
 
# creating text label to display on window screen
label = tk.Label(window, font=("Times New Roman",55),text="Enjoy Canvas in Air!",bd=70)
label.pack()

def screen2():

    def whiteScreen():
        subprocess.run(["python","new.py"]);
    
    def multiHand():
        subprocess.run(["python","aircanvas.py"]);
    
    leftbutton=Button(frame,text="Single Hand Recognition", height=600,width=300,command=whiteScreen)
    leftbutton.pack(side=LEFT)

    
    rightbutton=Button(frame,text="Multiple Hand Recognition", height=600,width=250,command=multiHand)
    rightbutton.pack(side=RIGHT)

myfont=font.Font(size=30,family="Times New Roman")
Button1=tk.Button(window,text="Start",bd=50,width=30,command=screen2)
Button1['font'] = myfont
Button1.pack()

window.mainloop()