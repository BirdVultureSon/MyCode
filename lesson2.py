'''
input
'''
'''Fruits = ["яблоко", "груша", "банан"]
print (Fruits)
Fruits. append ("арбуз")
print (Fruits)
x = "яблоко" not in Fruits
print (x)'''
print ("Игра Поле чудес")
wordList = ["яблоко", "груша", "банан"]
import random
#random.choices 
Secret_word = random.choices (wordList)
Bukvi = []
#correctWord = []
choises = 3

while choises > 0 :
    flag_of_v = True 
    Value = input("Введите вашу букву: ")
    Bukvi.append(Value)
    print (Bukvi)
    
    for i in Secret_word:
    #print (i)
        if i in Bukvi:
            #correctWord.append(Value)
            print (i, end ="") 
        else:
            print ("*", end ="")
            flag_of_v = False
            
    if flag_of_v == True:
        print ("Ты победил!")
        break 
            
    #print ()
    if Value not in Secret_word:
        choises = choises - 1
        print (Secret_word)
        print ("У вас осталось попыток :"+ str(choises))
    if choises == 0:
        print (Secret_word)
        print ("Ты проиграл")
        
     
    
        
    
print("ваши попытки кончились")
        
     
