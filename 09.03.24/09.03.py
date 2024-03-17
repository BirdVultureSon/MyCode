import turtle

t = turtle.Turtle()
t.speed(1000)
t.color("green")
t.width(15)


def star():
    for i in range(5):
        t.forward(100)
        t.left(-144)

def up_pen(x, y):
    t.up()
    
    
    t.goto(x, y)
    t.down()

def circle():
    for i in range(60):
        t.forward(5)
        t.left(6)


def spiral():
    for i in range(60):
        t.forward(i)
        t.left(15)
#spiral()
#star()


def olimpic_circle(x, y, color):
    t.color(color)
    t.width(10)
    up_pen(x, y)
    circle()
    

def olympic_logo():
    olimpic_circle(-120, 60, "blue")
    olimpic_circle(0, 60, "black")
    olimpic_circle(120, 60, "red") 
    olimpic_circle(-60, 0, "yellow") 
    olimpic_circle(60, 0, "green")
#olympic_logo()

def clearF():
    t.clear()
    #print("clearF")


def up():
    t.setheading(90)
    t.forward(10)

def down():
    t.setheading(-90)
    t.forward(10)

def left():
    t.setheading(180)
    t.forward(10)

def right():
    t.setheading(0)
    t.forward(10)

def up_or_down():
    if t.isdown():
        t.up()
    else:
        t.down()

def red():
    t.color("red")

def green():
    t.color("green")

def blue():
    t.color("blue")

def yellow():
    t.color("yellow")

def rainbow():
    t.setheading(90)
    up_pen(0,100)
    t.width(10)
    t.color("red")
    for i in range(30):
        t.forward(7)
        t.left(6)

    up_pen(-10,100)
    t.setheading(90)
    t.color("orange")
    for i in range(30):
        t.forward(6)
        t.left(6)

    up_pen(-20, 100)
    t.setheading(90)
    t.color("yellow")
    for i in range(30):
        t.forward(5)
        t.left(6)
    up_pen(-30, 100)

    t.setheading(90)
    t.color("green")
    for i in range(30):
        t.forward(4)
        t.left(6)

    up_pen(-40, 100)
    t.setheading(90)
    t.color("blue")
    for i in range(30):
        t.forward(3)
        t.left(6)

    up_pen(-50, 100)
    t.setheading(90)
    t.color("purple")
    for i in range(30):
        t.forward(2)
        t.left(6)

t.screen.onkeypress(up, "Up")
t.screen.onkeypress(down, "Down")
t.screen.onkeypress(left, "Left")
t.screen.onkeypress(right, "Right")
t.screen.onkeypress(clearF, "0")
t.screen.onkeypress(up_or_down, "space")
t.screen.onkeypress(red, "r")
t.screen.onkeypress(green, "g")
t.screen.onkeypress(spiral, "s")
t.screen.onkeypress(yellow, "y")
t.screen.onkeypress(blue, "b")
t.screen.onkeypress(rainbow, "h")
t.screen.listen()
t.screen.mainloop()


'''
Написать функции смены цвета линии и присвоить их клавишам букв - например, клавиша "b" меняет цвет на голубой ("blue"), клавиша "y" - на желтый ("yellow"), "g" - на зеленый("green").
Сделать функцию отрисовки радуги. (Подсказка: дуга - это половина круга, т.е. произведение угла поворота на количество повторов должно быть равно 180. Чтобы следующая дуга была меньше предыдущей - уменьшаем длину линии)
'''