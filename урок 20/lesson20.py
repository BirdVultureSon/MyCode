import tkinter as tk
import random 

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


window = tk.Tk()
window.geometry("650x500")
window.title("Цветные фигуры")
my_canvas = tk.Canvas(window, width = 500, height = 500, bg = "white")
my_canvas.place(x = 0, y = 0)
circle_button = tk.Button(window, text = "Нарисовать круг", width = 17, command = draw_circle)
circle_button.place(x = 510, y = 20)
button_oval = tk.Button(window, text = "Нарисовать овал", width = 17, command = draw_oval)
button_oval.place(x = 510, y = 90)


















window.mainloop()