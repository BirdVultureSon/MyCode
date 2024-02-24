import tkinter as tk 

import tkinter.filedialog as tfd

import tkinter.messagebox as tkm

file_name = ""

def support():
    tkm.showinfo(f"Помощь", {help})
    help = "Новый файл - создать файл", 
    support()

def open_file():
    content_text.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    file_label ["text"] = "Файл: "+file_name
    #print (file_name)
    with open(file_name, encoding="utf-8") as file: 
        text1 = file.read()
        #print (text1)
    #with open("C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/21.01/books.txt") as file: 
        content_text.insert(1.0, text1)
       
def save_as_file():
    global file_name
    file_name = tfd.askopenfilename()
    tkm.showinfo("Сохранение файла", f"Сохранения записаны в файл {file_name }")
    file_label ["text"] = "Файл: "+file_name
    #content = content_text.get(1.0, "end")
    print (file_name)
    '''print (content)
    with open(file_name, "w") as file:
        file.write(content)'''
    write_to_file(file_name)

def save_file():
    global file_name
    if file_name == "":
        save_as_file()
    else:
        write_to_file(file_name)
        

def new_file():
    global file_name
    if tkm.askokcancel("Создание нового файла", "Вы уверены? Несохраненный текст будет удален"):
        file_name == ""
        file_label ["text"] = "Файл: "+file_name
        content_text.delete(1.0, "end")
    
def write_to_file(file_name):
    content = content_text.get(1.0, "end") 
    with open(file_name, "w") as file:
        file.write(content)


window = tk.Tk()
window.title("Мой Блокнот")
window.geometry("400x400")


#file_name = ""

content_text = tk.Text(window, wrap="word")
content_text.place (x = 0, y = 0, relwidth = 1, relheight = 1)
#content_text = tk.Text(window, wrap="word")
main_menu = tk.Menu(window)
window.configure (menu = main_menu)
file_menu = tk.Menu(main_menu, tearoff = 0)
support_menu = tk.Menu(main_menu, tearoff = 0)

main_menu.add_cascade(label = "Файл", menu = file_menu)
main_menu.add_cascade(label = "Справка", menu = support_menu)

new_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/MyCode/20.01/new_file.gif")
open_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/MyCode/20.01/openfile.gif")
save_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/MyCode/20.01/save_file.gif")

#file_menu.add_command(label="Открыть", image = open_file_icon, compound="left", command = open_file)
file_menu.add_command(label= "Новый файл", image = new_file_icon, compound = "left", command = new_file)
file_menu.add_command(label= "Открыть файл", image = open_file_icon, compound = "left", command = open_file)
file_menu.add_command(label= "Сохранить файл", image = save_file_icon, compound = "left", command = save_file)
file_menu.add_command(label= "Сохранить как", image = save_file_icon, compound = "left", command = save_as_file)
support_menu.add_command(label = "Помощь")
support_menu.add_command(label = "О программе")

file_label = tk.Label(window, text = "Файл: "+file_name)
file_label.place (relx = 0, rely = 1, anchor = "sw")

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
#  https://magicofpython.blogspot.com/2015/12/python_10.html
#  https://pythonru.com/biblioteki/pyinstaller

'''Сегодня у тебя будет задание, которое улучшит твою программу.

Добавить еще один пункт основного меню "Справка", в него добавить подменю:
Помощь
о программе'''

