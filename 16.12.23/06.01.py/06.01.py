import random
'''months = ["январь" , "февраль" , "март" , "апрель" , "май", "июнь" , "июль" , "август" , "сентябрь" , "октябрь" , "ноябрь" , "декабрь"]       #первая задача
num = 1
for i in months:
    #print (num)
    print (i , num)
    num = num + 1'''

answers = ["да" , "нет" , "не могу сейчас сказать"]
question = str(input("Привет! Задай свой вопрос: "))
print (random.choice (answers))

