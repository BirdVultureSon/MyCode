import random


over = "Нет"


userBals = 100
print (f"У вас : {userBals} баллов")
while userBals > 0:
    numRandomOne = random.randint (1, 6)
    numRandomTwo = random.randint (1, 6)
    numRandom = numRandomOne + numRandomTwo
    print (numRandom)

    bindOne = int(input("Введите ставку от 1 до 100: "))
    numUser = int(input("Введите число от 2 до 12:  ")) 


    '''numRandomOne = random.randint (1, 6)
    numRandomTwo = random.randint (1, 6)
    numRandom = numRandomOne + numRandomTwo
    print (numRandom)'''
    if numUser == numRandom:                                    #Подтверждение игры
        userBals = userBals + (bindOne * 4)
        print (userBals)
        over = str(input("Вы хотите продолжить? Да или Нет:"))           
        if over == "Нет":
            break


    if numRandom < 7:
        if numUser < 7:
            print ("Вы выиграли ставку!")
            userBals = userBals + bindOne
                                                #Подтверждение игры
            print (userBals)
            over = str(input("Вы хотите продолжить? Да или Нет:"))           
            if over == "Нет":
                break
        else:
            print ("Ставка проиграна!")
            userBals = userBals - bindOne
                                               #Подтверждение игры
                
            print (userBals)
            over = str(input("Вы хотите продолжить? Да или Нет:"))           
            if over == "Нет":
                break

    else:
        if numUser >= 7:
            print ("Ставка выиграна!")
            numUser = userBals + bindOne
            print (userBals)
            over = str(input("Вы хотите продолжить? Да или Нет:"))           
            if over == "Нет":
                break
        else:
            print ("Ставка проиграна :(")
            userBals = userBals - bindOne
            print (userBals)
            over = str(input("Вы хотите продолжить? Да или Нет:"))           
            if over == "Нет":
                break
    if userBals <= 0:
        print ("Игра окончена")
        break
    