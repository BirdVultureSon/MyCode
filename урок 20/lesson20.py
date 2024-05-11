import tkinter as tk
import random 
import time

def animate_circle():
    color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    circle = my_canvas.create_oval(x, y, x + d, y + d, fill = color)
    dx = 2
    dy = 2
    while True:
        coords = my_canvas.coords(circle)
        print(coords[0], coords[1], coords[2], coords[3])
        print(coords)
        left = coords[0]
        top = coords[1]
        right = coords[2]
        bottom = coords[3]
        if left <= 0 or right >= 500:
            if dx < 0:
                dx = random.randint(1, 5)
                dx = -dx
            else:
                dx = random.randint(1, 5)
            dx = -dx
        if top <= 0 or bottom >= 500:
            if dy < 0:
                dy = random.randint(1, 5)
                dy = -dy
            else:
                dy = random.randint(1, 5)
            dy = -dy
        my_canvas.move(circle, dx, dy)
        time.sleep(0.01)
        window.update()
        
        
        

def stop_draw():
    global stop
    stop = True


def draw_circles():
    global stop
    while True:
        draw_circle()
        window.update()
        time.sleep(0.1)
        if stop:
            stop = False
            break

        

def draw_square():
    color = random.choice(colors)
    border_color = random.choice(colors)
    d = random.randint(1, 100)
    x = random.randint(0, 500 - d)
    y = random.randint(0, 500 - d)
    my_canvas.create_rectangle(x, y, x +d, y + d, fill = color, outline= border_color)

def draw_oval():
    color = random.choice(colors)
    d1 = random.randint(1, 100)
    d2 = random.randint(1, 100)
    x = random.randint(0, 500 - d1)
    y = random.randint(0, 500 - d2)
    my_canvas.create_oval(x, y, x + d1, y + d2, fill = color)

def draw_circle():
    d = random.randint(1, 100)
    x1 = random.randint(0, 500 - d)
    y1 = random.randint(0, 500 - d)
    color = random.choice(colors)
    my_canvas.create_oval(x1, y1, x1 + d, y1 + d, fill = color, outline= "white")
    #color = random.randint(0, 8)
    #n = colors[color]
    #my_canvas.create_oval(200, 200, 400, 220, fill = random.choice(colors))
    #my_canvas.create_oval(200, 200, 400, 220, fill = colors[random.randint(0, 8)])
    #circle_button.place(x = x1, y = y1)



colors = ['red', 'blue', 'green', 'pink', 'black', 'yellow', 'orange',  'purple', 'brown']
stop = False 

window = tk.Tk()
window.geometry("650x500")
window.title("Цветные фигуры")
my_canvas = tk.Canvas(window, width = 500, height = 500, bg = "white")
my_canvas.place(x = 0, y = 0)
circle_button = tk.Button(window, text = "Нарисовать круг", width = 17, command = draw_circle)
circle_button.place(x = 510, y = 20)
button_oval = tk.Button(window, text = "Нарисовать овал", width = 17, command = draw_oval)
button_oval.place(x = 510, y = 90)
button_square = tk.Button(window, text = "Нарисовать квадрат", width = 17, command = draw_square)
button_square.place(x = 510, y = 160)
circles_button = tk.Button(window, text = "Бесконечные круги", width = 17, command = draw_circles)
circles_button.place(x = 510, y = 220)
stop_button = tk.Button(window, text = "Остановить рисование", width = 17, command = stop_draw)
stop_button.place(x = 510, y = 350)
ant_circle = tk.Button(window, text = "Анимированный круг", width = 17, command = animate_circle)
ant_circle.place(x = 510, y = 280)














window.mainloop()