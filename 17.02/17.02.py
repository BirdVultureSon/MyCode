def turn():
    x1 = int(input("введите строку откудa:"))
    y1 = int(input("введите столбец откудa:"))
    x2 = int(input("введите строку куда:"))
    y2 = int(input("введите столбец куда:"))

    if area[x2][y2] == "*":
        area[x2][y2] = area[x1][y1]
        area[x1][y1] = "*"
    #print1()


def print1():
    print(area[0])
    print(area[1])


area = [["стол", "стул", "шкаф"],
        ["стул", "*", "кресло"]]



while area[0][2] != "кресло" and area[1][2] != "шкаф":
    print1()
    turn()
print("вы выиграли!")


    


