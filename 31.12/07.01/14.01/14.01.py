import tkinter

def get_num1():
    x = int(text_num1.get())     
    return x

def get_num2():
    y = int(text_num2.get())
    return y



def set_answer(x, y, z, sign1):
    clearFn()
    text_answer.insert(0, f"{x} {sign1} {y} = {z}")


def add():
    x = get_num1()                    
    y = get_num2()
    print (x)
    print (y)
    z = x + y
    print (f"Выполняем сложение {z}")
    set_answer(x, y, z, "+")

def sub():
    x = get_num1()                    
    y = get_num2()
    print (x)
    print (y)
    z = x - y
    print (f"Выполняем вычитание: {z}")
    #text_answer.insert(0, z)
    set_answer(x, y, z, "-")

def mul():
    x = get_num1()                    
    y = get_num2()
    print (x)
    print (y)
    z = x * y
    print (f"Выполняем вычитание: {z}")
    #text_answer.insert(0, z)
    set_answer(x, y, z, "*")


def div():
    x = get_num1()                    
    y = get_num2()
    print (x)
    print (y)
    z = x / y
    print (f"Выполняем вычитание: {z}")
    #text_answer.insert(0, z) 
    set_answer(x, y, z, "/")
    

def clearFn():
    #text_num1.delete(0, "end")
    #text_num2.delete(0, "end")
    text_answer.delete(0, "end")


color1 = "white"
color2 = "white"
color3 = "white"
color4 = "white"

window = tkinter.Tk()
window.title("Калькулятор")
window.geometry("300x300")
#height = высота, width = ширина
button_add = tkinter.Button(window, text="+", command = add, width = 7, bg = color1)
button_add.place(x = 95, y = 110)

button_sub = tkinter.Button(window, text="-", command = sub, width = 7, bg = color2)
button_sub.place(x = 160, y = 110)

button_mul = tkinter.Button(window, text="*", command = mul, width = 7, bg  = color3)
button_mul.place(x = 95, y = 154)

button_div = tkinter.Button(window, text="/", command = div, width = 7, bg = color4)
button_div.place(x = 160, y = 154)

text_num1 = tkinter.Entry(window, width="20")
text_num1.place(x = 95, y = 40)

text_num2 = tkinter.Entry(window, width=20)
text_answer = tkinter.Entry(window, width=20)

text_num2.place(x=95, y=81)
text_answer.place(x=95, y=221)


label_num1 = tkinter.Label(window)
label_num1 = tkinter.Label(window, text="Введите первое число: ", background = "silver", fg = "#103486")
label_num1.place(x=95, y=20)

label_num2 = tkinter.Label(window)
label_num2 = tkinter.Label(window, text="Введите второе число: ", background = "silver", fg = "#103486")
label_num2.place(x=95, y=61)


label_answer = tkinter.Label(window)
label_answer = tkinter.Label(window, text="Ответ: ", background = "silver")
label_answer.place(x=95, y=200)

window.configure(bg = "silver")



window.mainloop()                              #Дз выполнено (настроить внешний вид калькулятора по своему усмотрению)
                                               #https://www.color-hex.com/