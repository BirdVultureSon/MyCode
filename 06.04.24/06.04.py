import tkinter as tk
import random


def check(event):
    print("проверка")
    user_color = color_entry.get()
    word_color = color_label["fg"]
    if user_color == word_color:
        print ("Вы выиграли")
    else:
        print("Вы не угадали")
    new_word()
    color_entry.delete()

def new_word():
    color_label["fg"] = random.choice(colors)
    color_label["text"] = random.choice(colors)

window = tk.Tk()
window.title("Назови цвет")
window.geometry("400x300")
instructions = tk.Label(window, text = "Введи цвет слова, а не слово! Жми Enter, чтобы играть.", font = ("helvetica", 10))
instructions.place(x = 10, y = 10)
color_label = tk.Label(window, text = "color", font = ("helvetica", 60))
color_label.place(x = 10, y = 80)
color_entry = tk.Entry(window, font = ("helvetica", 10))
color_entry.place(x = 10, y = 180)
color_entry.focus_set()
colors = ["red", "blue", "green", "pink", "black", "yellow", "orange", "purple", "brown", "white"]

'''
https://vimeo.com/682480608/b4fb9e88a6
'''

window.bind("<Return>", check)
window.mainloop()