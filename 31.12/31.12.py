import random
'''def fun1():
    print ("Функция сработала")


fun1 ()


def fun2(a):
    print ("Функция сработала " + a)

fun2 ("абв")
n = "123"
fun2 (n)

def area_square(side):
    area = side * side 
    fun1()
    print (area)
    if area == 16:
        return area * 2
    else:
        return area

a = area_square(3)
print (a)'''

'''time = 12
def fun1(time):
    time = time + 1
    return time
fun1(time)
print (time)'''


'''def factorial(n): 

result = 1 

for i in range(1, n+1):
result *= i 

return result'''

'''def lottery(): 

    tickets = [13,54,23,1,5,3]
    ticket = random.choice(tickets) 
    return ticket

winner = lottery()
print(f"Выигрышный билет № - {winner}")'''

'''num1 = 2
def fun1(num):
    num = num + 1
    return num
num2 = fun1(num1)
print (num2)'''

'''def factorial(n): 

    result = 1 

    for i in range(1, n+1):
    result *= i 

    return result'''
'''c = 10
lfun = lambda a: a * a
print (lfun(c) + 1)
#b = lfun (c)
#print (b)
def fun1(a):
    print (a)
    return a

def fun2(a , b):
    print (b)
    fun1(a)
    return b'''

#fun2 (1 , 2)

#функция два значения?

'''def fun1(a, b, c):                                      #дз 1
    if a < b and a < c:
        d = a
    elif b < a and b < c:
        d = b
    else:
        d = c
    
    return d

f = int(input("Введите первое число: "))
g = int(input("Введите второе число: "))
n = int(input("Введите третье число: "))
i = fun1(f, g, n)
print (i)'''


'''def fun2(r):
    
    s = 3.14 * r * r
    return s
h = int(input("Введите радиус: "))
o = fun2(h)
print (o)'''

def lottery(): 

    tickets = [13,54,23,1,5,3]

    ticket = random.choice(tickets) 

    return ticket

winner = lottery()
print(f"Выигрышный билет № - {winner}")

def multi_lottery(): 

    tickets = [13, 54, 23, 1, 5, 3] 

    ticket1 = random.choice(tickets) 
    
    tickets.remove(ticket1) 

    ticket2 = random.choice(tickets) 

    return ticket1, ticket2

first_winner, second_winner = multi_lottery()

print(f"Выигрышные билеты - {first_winner} и {second_winner}")