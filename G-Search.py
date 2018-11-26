import tkinter as tk
import webbrowser
from tkinter import *



mw = tk.Tk()
mw.title("Search Engine")
mw.resizable(0, 0)

label1 = Label(mw, fg="black", bg="white", text="Query")
label1.grid(row=0, column=0)

entry1 = Entry(mw, width=50)
entry1.grid(row=0, column=1)

def callback():
    webbrowser.open("https://www.google.com/search?q="+entry1.get())
    
def get(event):
    webbrowser.open("https://www.google.com/search?q="+entry1.get())
    
button1 = Button(mw, text="Search", command=callback)
button1.grid(row=0,column=2)
entry1.bind('<Return>',get)
mw.wm_attributes('-topmost',1)
mw.mainloop()
