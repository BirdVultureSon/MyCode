"""import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Мой Блокнот")
window.geometry("400x400")

btn = ttk.Button(text="Button")
btn.pack()
btn1 = tk.Button(text="Button")
#btn1.pack(anchor="sw")
#btn ()

btn1.place(relx=0, rely=1, anchor="sw")

window.mainloop()"""

from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
btn = ttk.Button(text="Click me")
btn.place(relx=0.5, rely=0.5, anchor="c", width=80, height=40)
 

 
root.mainloop()