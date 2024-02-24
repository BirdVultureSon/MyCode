import tkinter as tk

def push():
    global turn
    print(turn)
    turn = turn + 1
    #turn += 1 


window = tk.Tk()
window.title("Крестики нолики")
window.geometry("300x300")
window.resizable(False, False)
area = []
turn = 1
#print(push())

for x in range (3):
    area.append([])
    for y in range (3):
        button = tk.Button(window, text = "", width= 13, height = 6)
        area[x].append(button)
        area[x][y].place(x = x * 100, y = y * 100)
        area[x][y]["command"] = push




print(area)
























window.mainloop()