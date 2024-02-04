import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Мой блокнот")
window.geometry("400x400")

content_text = tk.Text(window, wrap="word")
content_text.place(x=0, y=0, relwidth=0.5, relheight=0.5)

# подключение полоски смещения
scrollbar = ttk.Scrollbar(orient="vertical", command=content_text.yview)
# указание размещения элемента
scrollbar.pack(side="right", fill="y")

#подключение полоски полю
content_text["yscrollcommand"]=scrollbar.set

#динамическое изменение размера
content_text = tk.Button(text="Click")
#это: relwidth=0.5, relheight=0.5
content_text.place(x=100, y=100, relwidth=0.5, relheight=0.5)

window.mainloop()
