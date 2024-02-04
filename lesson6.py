'''x = int(input("Введите месяц: "))      #Домашнее задание
if 1 > x: 
    print ("Вы ввели неверный номер")
elif x == 1 or x == 2 or x == 12:
    print ("Зимний месяц")
elif 3 <= x <= 5:
    print ("Весенний месяц")
elif 6 <= x <= 8:
    print ("Летний месяц")
elif 9 <= x <= 11 :
    print ("Осенний месяц")
else : 
    print ("Вы ввели неверный номер")'''
#четвертая методичка

counter = 7

'''while counter > 0:
    print (counter, end = "")
    counter = counter - 1 

counter = 10

while counter > 0:
    print (counter, end = "")
    counter = counter - 2 '''

'''while True:
    print ("Привет")
    stop = input("Остановить цикл? Да - нет: ")
    if stop == "Да":
        break '''
'''word = "Привет"
for i in range(1 , 5):
    print (i) '''
'''print ("Программа счёта сбережений")
saveMoney = int(input("Уже накопил: "))
addedMoney = int(input("Собираемся копить за день: "))
days = int(input("Сколько дней планируешь копить?: "))
goal = input("А сколько ты хочешь накопить? ") 
goal = int(goal)
saved_roubles = input("Сколько ты уже накопил? ") 
saved_roubles = int(saved_roubles)
added_roubles = input("Сколько ты планируешь откладывать каждый день? ") 
added_roubles = int(added_roubles)
days = 0
while goal > saved_roubles: 

    saved_roubles = saved_roubles + added_roubles 

    days = days + 1 

#print(f"День {days}, сумма - {saved_roubles}") 

print(f"Ты накопишь {goal} рублей за {days} дней")
for i in range (days):
    saveMoney = saveMoney + addedMoney
    print (f"День {i} {saveMoney}")'''
goal = input("А сколько ты хочешь накопить? ") 

goal = int(goal)

saved_roubles = input("Сколько ты уже накопил? ") 

saved_roubles = int(saved_roubles)

added_roubles = input("Сколько ты планируешь откладывать каждый день? ") 

added_roubles = int(added_roubles)
days = 0
while goal > saved_roubles: 

    saved_roubles = saved_roubles + added_roubles 

    days = days + 1 

#print(f"День {days}, сумма - {saved_roubles}") 

print(f"Ты накопишь {goal} рублей за {days} дней")





    
