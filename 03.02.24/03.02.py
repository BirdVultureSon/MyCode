#area = ["*","*","*"]
'''for cell in area: 

    print(cell)
area[0] = "x"
area[1] = "0"
for cell in area:

    print(cell)'''

def check_winner():
    #По горизонтали X
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        return "X"
    elif area[1][0] == "X" and area[1][1] == "X" and area[1][2] == "X":
        return "X"
    elif area[2][0] == "X" and area[2][1] == "X" and area[2][2] == "X":
        return "X"
    

    #По диагонали X
    if area[0][0] == "X" and area[1][1] == "X" and area[2][2] == "X":
        return "X"
    elif area[0][2] == "X" and area[1][1] == "X" and area[2][0] == "X":
        return "X"
    
    #По вертикали X
    if area[0][0] == "X" and area[1][0] == "X" and area[2][0] == "X":
        return "X"
    elif area[0][1] == "X" and area[1][1] == "X" and area[2][1] == "X":
        return "X"
    elif area[0][2] == "X" and area[1][2] == "X" and area[2][2] == "X":
        return "X"
    
    
    #По горизонтали 0
    if area[0][0] == "0" and area[0][1] == "0" and area[0][2] == "0":
        return "0"
    elif area[1][0] == "0" and area[1][1] == "0" and area[1][2] == "0":
        return "0"
    elif area[2][0] == "0" and area[2][1] == "0" and area[2][2] == "0":
        return "0"
    
    #По диагонали 0
    if area[0][0] == "0" and area[1][1] == "0" and area[2][2] == "0":
        return "0"
    elif area[0][2] == "0" and area[1][1] == "0" and area[2][0] == "0":
        return "0"
    
    #По вертикали 0
    if area[0][0] == "0" and area[1][0] == "0" and area[2][0] == "0":
        return "0"
    elif area[0][1] == "0" and area[1][1] == "0" and area[2][1] == "0":
        return "0"
    elif area[0][2] == "0" and area[1][2] == "0" and area[2][2] == "0":
        return "0"
    return ("*")
    


area = [["*","*","*"],
         ["*","*","*"], 
         ["*","*","*"]]
print (area)
'''print (area[0][2])
area[0][2] = "x"
area[2][1] = "0"

for cell in area: 

    print(cell)'''

turn_char = "X"

'''row = int(input("Введите номер строки(0,1 или 2):"))
column = int(input("Введите номер столбца(0,1 или 2):"))
area[row][column] = "x"
print (area)'''

for turn in range(1, 10):
    print (f"Ход номер: {turn}")
    row = int(input("Введите номер строки(0,1 или 2):"))
    column = int(input("Введите номер столбца(0,1 или 2):"))


    if turn % 2 == 0:
        print ("Ходят нолики: ")
        turn_char = "0"
    else:
        print ("Ходят крестики: ")
        turn_char = "X"
    
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("Ячейка уже занята, вы пропускаете ход!")
        continue

    for i in range(0, 3):
        for n in range(0, 3):
            print (area[i][n], end = " ")
        print(" ")

    if check_winner() == "X":
        print ("Победил X!")
       
        break
    elif check_winner() == "0":
        print ("Победил 0!")
        break
    elif turn == 9 and area[row][column]  == "*":
        print ("Ничья")
        break
    

'''Вынести код для вывода поля в отдельную функцию print_area, и вызывать эту функцию в основной программе. 
Придумать, как решить проблему неудобного ввода номеров строк и столбцов, чтобы пользователь мог вводить не 0,1 и 2, а 1, 2 и 3.'''

