import tkinter as tk
import tkinter.messagebox as tmb
import random

def new_game():
    global word 
    global letters 
    letters = []
    word = random.choice(words)
    label_Word["text"] = "Здесь будет слово"
    

#def check_letter(event = ""):
def check_letter():    
    letter = entry_letter.get()
    letters.append(letter)
    entry_letter.delete(0, "end")
    show_word = ""
    print(letter)
    for char in word:
        if char in letters:
            show_word = show_word + char
        else:
            show_word = show_word + "*"
    label_Word["text"] = show_word
    if word == show_word:
        print("Победа")
        tmb.showinfo("Победа", "Ты угадал слово!")
        new_game()

window = tk.Tk()
window.title("Угадай слово")
window.geometry("300x200")
label_Word = tk.Label(window, text = "Слово", font = ("arial", 15))
label_Word.place(x = 70, y = 20)
entry_letter = tk.Entry(window, width = 8, font = ("arial", 10))
entry_letter.place(x = 130, y = 80)
button = tk.Button(window, text = "Проверить букву", font = ("arial", 15), command = check_letter)
button.place(x = 100, y = 120)
with open("C:/Users/mizad/OneDrive/Рабочий стол/lesson 1/MyCode/words.txt", encoding="utf-8") as file:
    data = file.read()
words = data.split()
word = random.choice(words)
letters = []



'''
Добавить в игру попытки - сделать глобальную переменную attempts и надпись для окна label_attempts. В функции check_letter уменьшать попытки, если введенной буквы в слове нет. Если попытки кончились - начинать новую игру вызовом функции new_game. В функцию новой игры добавить обновление количества попыток. 
Добавить в условие окончания попыток вывод всплывающего окна с информацией о проигрыше, и какое слово было загадано.
'''












#window.bind("<Return>", check_letter)
window.mainloop()

