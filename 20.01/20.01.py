import tkinter as tk 

window = tk.Tk()
window.title("Мой Блокнот")
window.geometry("400x400")

content_text = tk.Text(window)
content_text.place (x = 0, y = 0, relwidth = 1, relheight = 1)
content_text = tk.Text(window, wrap="word")
main_menu = tk.Menu(window)
window.configure (menu = main_menu)
file_menu = tk.Menu(main_menu, tearoff = 0)
main_menu.add_cascade(label = "Файл", menu = file_menu)


new_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/20.01/new_file.gif")
open_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/20.01/openfile.gif")
save_file_icon = tk.PhotoImage(file = "C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/20.01/save_file.gif")

file_menu.add_command(label= "Новый файл", image = new_file_icon, compound = "left")
file_menu.add_command(label= "Открыть файл", image = open_file_icon, compound = "left")
file_menu.add_command(label= "Сохранить файл", image = save_file_icon, compound = "left")





window.mainloop()