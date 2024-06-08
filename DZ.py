
wordList = ["яблоко", "груша", "банан"]
import random
wordSecret = random.choice(wordList)
letters = []
print (wordSecret) #Test random function
choises = 5
while choises > 0 :
    if wordSecret != letters:
        wordUser = input ("Введите вашу букву: ")
        letters.append(wordUser)
        print (letters)
    

        for i in wordSecret:
                if i in letters:
                    print (i, end ="")
                else:
                    print ("*", end ="")
            
    if wordSecret == letters:
        print ("Вы угадали")
        break
    if wordUser  not in wordSecret:
        choises = choises - 1
    
else:
    print ("Ваши попытки закончились")
       
