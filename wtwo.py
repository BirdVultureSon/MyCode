import tkinter as tk
from tkinter import ttk

#_____________________________________________________________________________

def fun_start(ten, content_text):
    print("fun_stor")
    print(ten + " 1")
    fun_create_window(ten, content_text)
    
def fun_close_window(text2, my_this_text, my_this_window, content_text):
        print(text2 + " 2")
        key = my_this_text.get(1.0, "end")
        content_text.insert(1.0, key)
        my_this_window.destroy()

def fun_create_window(text, content_text):
        
    window2 = tk.Tk()
    window2.title("Мой блокнот")
    window2.geometry("400x400")

    print(text + " 3")

    frame2 = tk.Frame(window2)
    # размер контейнера относительно главного окна (window)
    frame2.place(x=0, y=0, relwidth=0.5, relheight=0.5)

    #текстовое поле помещаем в виджет (в контейнер Frame)
    content_text2 = tk.Text(frame2, wrap="word")
    # размер текстового поля (относительно контейнера Frame)
    content_text2.place(x=0, y=0, relwidth=1, relheight=1)

    # подключение полоски смещения
    scrollbar2 = ttk.Scrollbar(frame2, orient="vertical", command=content_text2.yview)
    # указание размещения элемента
    scrollbar2.pack(side="right", fill="y")

    #подключение полоски полю
    content_text2["yscrollcommand"]=scrollbar2.set

    val2 = "tre"

    main_text = content_text

    button2 = tk.Button(window2, text="Click", command = lambda a=val2: fun_close_window(a, content_text2, window2, main_text) )
    button2.place(x=200, y=100, relwidth=0.5, relheight=0.5)

    window2.mainloop()

    return val2, window2










#_____________________________________________________________________________
    
window = tk.Tk()
window.title("Мой блокнот")
window.geometry("400x400")

# Контейнер (контейнер Frame помстили в окно window)
frame = tk.Frame(window)
# размер контейнера относительно главного окна (window)
frame.place(x=0, y=0, relwidth=0.5, relheight=0.5)

#текстовое поле помещаем в виджет (в контейнер Frame)
content_text = tk.Text(frame, wrap="word")
# размер текстового поля (относительно контейнера Frame)
content_text.place(x=0, y=0, relwidth=1, relheight=1)

# подключение полоски смещения
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=content_text.yview)
# указание размещения элемента
scrollbar.pack(side="right", fill="y")

#подключение полоски полю
content_text["yscrollcommand"]=scrollbar.set

value = "ten"

print(content_text)

#динамическое изменение размера
button = tk.Button(text="Click", command = lambda a=value: fun_start(a, content_text) )
#это: relwidth=0.5, relheight=0.5
button.place(x=100, y=200, relwidth=0.5, relheight=0.5)

window.mainloop()
