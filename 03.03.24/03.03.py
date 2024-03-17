'''forward - прямо, left = лево, right - вправо
up - поднять карандаш, down - опустить карандаш
#goto() - принимает координаты'''

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(10)

def circle():
    for i in range(60):
        t.forward(10)
        t.left(6)

def poligon(sides):
    for i in range(sides):
        t.forward(50)
        t.left(360 / sides)

def pentagon():
    for i in range(5):
        t.forward(100)
        t.left(360 / 5)

def square():
    for i in range(4):
        t.forward(100)
        t.left(90)

def up_pen(x, y):
    t.up()
    
    
    t.goto(x, y)
    t.down()

'''square()
up_pen(100, 100)
square()
up_pen(150, -150)
pentagon()
up_pen(250, 200)
poligon(12)'''

'''
for i in range(24):
    poligon(10)
    t.left(15)
    
up_pen(-200, -200)

for i in range(10):
    poligon(6)
    t.left(36)
up_pen(200, 200)

for i in range(6):
    poligon(4)
    t.left(60)
up_pen(200, -200)

for i in range(6):
    poligon(7)
    t.left(60)
up_pen(-200, 200)

for i in range(60):
    poligon(5)
    t.left(6)


up_pen(0, 200)
circle()

'''

'''
def poligonX(sides, l):
    for i in range(sides):
        t.forward(l)
        t.left(360 / sides)
poligonX(7, 50)
'''

for i in range(6):
    circle()
    t.left(60)

























t.screen.mainloop()


'''Сделать улучшенную функцию многоугольника, чтобы она принимала количество сторон и длину стороны.
 В цикле вызывать функцию отрисовки круга и поворачивать линию.'''