import tkinter

def add():
    x = int(text_num1.get())                     
    y = int(text_num2.get())
    print (x)
    print (y)
    z = x + y
    print (f"Выполняем сложение {z}")
    clearFn()
    text_answer.insert(0, f"{x} + {y} = {z}")

def sub():
    x = int(text_num1.get())                     
    y = int(text_num2.get())
    print (x)
    print (y)
    z = x - y
    print (f"Выполняем вычитание: {z}")
    #text_answer.insert(0, z)
    clearFn()
    text_answer.insert(0, f"{x} - {y} = {z}")

def mul():
    x = int(text_num1.get())                     
    y = int(text_num2.get())
    print (x)
    print (y)
    z = x * y
    print (f"Выполняем вычитание: {z}")
    #text_answer.insert(0, z)
    clearFn()
    text_answer.insert(0, f"{x} * {y} = {z}")


def div():
    x = float(text_num1.get())                     
    y = float(text_num2.get())
    print (x)
    print (y)
    z = x / y
    print (f"Выполняем вычитание: {z}")
    #text_answer.insert(0, z) 
    clearFn()
    text_answer.insert(0, f"{x} / {y} = {z}")
    

def clearFn():
    #text_num1.delete(0, "end")
    #text_num2.delete(0, "end")
    text_answer.delete(0, "end")

window = tkinter.Tk()
window.title("Калькулятор")
window.geometry("300x300")
#height = высота, width = ширина
button_add = tkinter.Button(window, text="+", command = add)
button_add.place(x = 95, y = 110)

button_sub = tkinter.Button(window, text="-", command = sub)
button_sub.place(x = 160, y = 110)

button_mul = tkinter.Button(window, text="*", command = mul)
button_mul.place(x = 95, y = 154)

button_div = tkinter.Button(window, text="/", command = div)
button_div.place(x = 160, y = 154)

text_num1 = tkinter.Entry(window, width="20")
text_num1.place(x = 95, y = 40)

text_num2 = tkinter.Entry(window, width=20)
text_answer = tkinter.Entry(window, width=20)

text_num2.place(x=95, y=81)
text_answer.place(x=95, y=221)




window.mainloop()