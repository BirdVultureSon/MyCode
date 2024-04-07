import tkinter as tk
import tkinter.messagebox as tmb
import random

def new_game():
    global word 
    global letters
    
    letters = []
    word = random.choice(words)
    label_Word["text"] = "Новое слово"
    

#def check_letter(event = ""):
def check_letter():
    global attempts
    letter = entry_letter.get()
    letters.append(letter)
    entry_letter.delete(0, "end")
    show_word = ""
    print(letter)

    #проверка букв в слове 
    for char in word: 
        if char in letters:
            show_word = show_word + char
        else:
            show_word = show_word + "*"
    label_Word["text"] = show_word

    #Счетчик попыток
    if letter not in word: 
        attempts = attempts - 1
        print(attempts)
        label_attempts["text"] = f"Попытки: {attempts}"
    if attempts == 0:
        tmb.showinfo("Попытки кончились",f"Было загадано слово {word}. Игра закончена, \n начинается новая игра")
        label_Word["text"] = "Новое слово"
        new_game()
        attempts = 5

    
    #условие победы
    if word == show_word:
        print("Победа")
        tmb.showinfo("Победа", "Ты угадал слово!")
        new_game()
#Глобальные переменные
attempts = 5

#окна
window = tk.Tk()
window.title("Угадай слово")
window.geometry("300x250")

#лейблы
label_Word = tk.Label(window, text = "Слово", font = ("arial", 24))
label_Word.place(x = 70, y = 20)
label_attempts = tk.Label(window, text = f"Попытки: {attempts}", font = ("arial", 10))
label_attempts.place(x = 20, y = 180)

#поле ввода
entry_letter = tk.Entry(window, width = 8, font = ("arial", 24))
entry_letter.place(x = 20, y = 120)

#кнопки
button = tk.Button(window, text = "Проверить букву", font = ("arial", 15), command = check_letter)
button.place(x = 120, y = 120)
with open("C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/MyCode/words.txt", encoding="utf-8") as file:
    data = file.read()

button = tk.Button(window, text = "Выход", font = ("arial", 8), command = exit)
button.place(x = 250, y = 220)

#переменные/списки    
words = data.split()
word = random.choice(words)
letters = []



'''
Добавить в игру попытки - сделать глобальную переменную attempts и надпись для окна label_attempts. В функции check_letter уменьшать попытки, если введенной буквы в слове нет. Если попытки кончились - начинать новую игру вызовом функции new_game. В функцию новой игры добавить обновление количества попыток. 
Добавить в условие окончания попыток вывод всплывающего окна с информацией о проигрыше, и какое слово было загадано.
'''












#window.bind("<Return>", check_letter)
window.mainloop()

