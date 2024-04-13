import tkinter as tk
import random
import tkinter.messagebox as tmb
def timer():
    global time_left
    if time_left > 0:
        time_left = time_left - 1
        time_lable["text"] = f"Осталось: {time_left} секунд"
        time_lable.after(1000, timer)
    else:
        tmb.showinfo("Время истекло", f"Правильно {score}, \n Ошибки: {fales}")
        if score > fales:
            tmb.showinfo("Хороший результат", "Ты молодец") 
        else:
            tmb.showinfo("Неважный результат", "В следующий раз получится лучше")

def check(event):
    print("проверка")
    global score
    global fales
    user_color = color_entry.get()
    word_color = color_label["fg"]
    if time_left > 0:    
        if user_color == word_color:
            print ("Вы выиграли")
            score = score + 1
            score_lable["text"] = f"Правильно: {score}"
        else:
            print("Вы не угадали")
            fales = fales + 1
            score_lableF["text"] = f"Ошибки: {fales}"
    '''else: 
        if score > fales:
            tmb.showinfo("Хороший результат", "Ты молодец") 
        else:
            tmb.showinfo("Неважный результат", "В следующий раз получится лучше")'''
    new_word()
    color_entry.delete(0, "end")

def new_word():
    color_label["fg"] = random.choice(colors)
    color_label["text"] = random.choice(colors)

score = 0
fales = 0
time_left = 30

window = tk.Tk()
window.title("Назови цвет")
window.geometry("400x300")
instructions = tk.Label(window, text = "Введи цвет слова, а не слово! Жми Enter, чтобы играть.", font = ("helvetica", 10))
instructions.place(x = 10, y = 10)
color_label = tk.Label(window, text = "color", font = ("helvetica", 60))
color_label.place(x = 10, y = 80)
score_lable = tk.Label(window, text = f"Правильно: {score}", font = ("helvetica", 10))
score_lable.place(x = 10, y = 40)
score_lableF = tk.Label(window, text = f"Ошибки: {fales}", font = ("helvetica", 10))
score_lableF.place(x = 10, y = 60)
time_lable = tk.Label(window, text = f"Осталось: {time_left} секунд")
time_lable.place(x = 10, y = 210)
color_entry = tk.Entry(window, font = ("helvetica", 10))
color_entry.place(x = 10, y = 180)
color_entry.focus_set()
colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown", "white"]
new_word()


'''
https://vimeo.com/682480608/b4fb9e88a6
'''


window.bind("<Return>", check)
time_lable.after(2000, timer)
window.mainloop()
'''
В функции timer: после блока условия if time_left > 0 добавить блок else, в котором выводить всплывающее окно из библиотеки tkinter.messagebox - "Конец игры", "Время вышло". 
В функции check: после блока условия if time_left > 0 добавить блок else, в котором делаем проверку - если правильных ответов больше неправильных - сделать всплывающее окно - "Хороший результат", "Ты молодец". Иначе - "Неважный результат", "В следующий раз получится лучше".
'''