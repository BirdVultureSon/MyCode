import tkinter as tk
import random

#решение: def check(event = ""):
def check(event):
    global attempts
    #print("Работает")
    number = entry.get()
    if number == "":
        window_label["text"] = "Введите число от 1 до 100"
    else:
        number = int(number)
        if number == secret_number:
            window_label["text"] = "Вы угадали!"
        elif number > secret_number:
            window_label["text"] = "Секретное число меньше"
        else:
            window_label["text"] = "Секретное число больше"
    if number != secret_number:
        attempts = attempts - 1
        attempts_label["text"] = f"Кол-во попыток: {attempts}"
    if attempts <= 0:
        new_game_button.configure(state = tk.NORMAL)
        check_button.configure(state = tk.DISABLED)


secret_number = random.randint(1, 100)
print(secret_number)
attempts = 5


window = tk.Tk()
window.geometry("200x150")
window.title("Угадай число")
window_label = tk.Label(window, text = "Угадай число от 1 до 100")
window_label.place(x = 30, y = 0)
attempts_label = tk.Label(window, text = f"Кол-во попыток: {attempts}")
attempts_label.place(x = 30, y = 30) 
entry = tk.Entry(window)
entry.place(x = 30, y = 50)
entry.focus_set()
check_button = tk.Button(window, text = "проверить", width = "17", command = lambda e = "<Return>": check(e))
check_button.place(x = 30, y = 80)
new_game_button = tk.Button(window, text = "Рестарт", width = "17", state = tk.DISABLED)
new_game_button.place(x = 30, y = 110)
#command = lambda e = "<Return>": check(e)
#print(check("<Return>"))


















window.bind("<Return>", check)
window.mainloop()