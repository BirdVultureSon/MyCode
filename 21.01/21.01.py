import tkinter as tk 

import tkinter.filedialog as tfd

def open_file():
    content_text.delete(1.0, "end")
    file_name = tfd.askopenfilename()
    #print (file_name)
    with open(file_name, encoding="utf-8") as file: 
        text1 = file.read()
        #print (text1)
    #with open("C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/21.01/books.txt") as file: 
        content_text.insert(1.0, text1)
       
def save_as_file():
    file_name = tfd.askopenfilename()
    content = content_text.get(1.0, "end")
    print (file_name)
    print (content)
    with open(file_name, "w") as file:
        file.write(content) 

def save_file():
    save_as_file()

def new_file():
    content_text.delete(1.0, "end")


window = tk.Tk()
window.title("Мой Блокнот")
window.geometry("400x400")

content_text = tk.Text(window, wrap="word")
content_text.place (x = 0, y = 0, relwidth = 1, relheight = 1)
#content_text = tk.Text(window, wrap="word")
main_menu = tk.Menu(window)
window.configure (menu = main_menu)
file_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "Файл", menu = file_menu)


new_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/20.01/new_file.gif")
open_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/20.01/openfile.gif")
save_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/20.01/save_file.gif")

#file_menu.add_command(label="Открыть", image = open_file_icon, compound="left", command = open_file)
file_menu.add_command(label= "Новый файл", image = new_file_icon, compound = "left", command = new_file)
file_menu.add_command(label= "Открыть файл", image = open_file_icon, compound = "left", command = open_file)
file_menu.add_command(label= "Сохранить файл", image = save_file_icon, compound = "left", command = save_file)
file_menu.add_command(label= "Сохранить как", image = save_file_icon, compound = "left", command = save_as_file)

#чтение из файлов
'''with open("C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/21.01/books.txt", encoding="utf-8") as file: 
    print (file.read())'''


'''with open("C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/21.01/books.txt", encoding="utf-8") as file:

    for line in file:
        print(f"Мой любимый язык программирования: {line}")'''

#перезапись
'''with open("C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/21.01/books.txt", "w") as file:

    file.write("Новый тестовый текст 1")

with open("C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/21.01/books.txt", "a") as file:

    file.write("\n Новый тестовый текст 2" )'''

window.mainloop()         

'''Домашнее задание
Добавить в меню Файл пункт "Сохранить как", иконку можно использовать такую же как у "Сохранить" 
Сделать другой цвет текстового поле и цвет текста (по желанию) - см. предыдущий урок.'''
#https://magicofpython.blogspot.com/2015/12/python_10.html
#https://pythonru.com/biblioteki/pyinstaller