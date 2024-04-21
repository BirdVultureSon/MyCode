import tkinter as tk
import random

def reset():
    global secret_number, attempts, entry
    attempts = 7
    secret_number = random.randint(1, 100)
    print(secret_number)
    window_label["text"] = "Угадай число от 1 до 100"
    attempts_label["text"] = f"Кол-во попыток: {attempts}"
    entry.delete(0, "end")
    new_game_button.configure(state = tk.DISABLED)
    check_button.configure(state = tk.NORMAL)
    entry.focus_set()

#решение: def check(event = ""):
def check(event):
    global attempts
    #print("Работает")
    number = entry.get()
    if number == "":
        window_label["text"] = "Введите число от 1 до 100"
    else:
        if attempts > 0:
            number = int(number)
            if number == secret_number:
                window_label["text"] = "Вы угадали!"
                attempts = 0
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
    entry.delete(0, "end")
    

secret_number = random.randint(1, 100)
print(secret_number)
attempts = 7


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
new_game_button = tk.Button(window, text = "Рестарт", width = "17", state = tk.DISABLED, command = reset)
new_game_button.place(x = 30, y = 110)
#command = lambda e = "<Return>": check(e)
#print(check("<Return>"))
'''
В функции check: после блока условия if attempts > 0 
добавить блок else, в котором делаем надпись label - "Можешь сыграть снова.", и меняем состояния кнопок - check_button делаем неактивной, 
new_game_button - активной.
'''
'''
В нашей программе есть одна проблема: есть пользователь введет какой-то символ 
кроме цифр или введет число больше 100 или меньше 1, то программа будет работать неправильно. 
Замени проверку пустоты строки на проверку, что было введено не число с помощью функции isdigit() 
или число не входит в диапазон от 1 до 100 включительно.
'''













window.bind("<Return>", check)
window.mainloop()