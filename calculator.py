# Калькулятор
x = float(input("Введите значение 1: "))
operation= str(input("Введите операцию +, -, * , /, ^: "))
y = float(input("Введите значение 2: "))
if operation == "+": #сложение
    print("Результат")
    z = x + y
    print(z) 
if operation == "*": #умножение
    print("Результат")
    z = x * y
    print(z)
if operation == "-": #вычитание
    print("Результат")
    z = x - y
    print(z)    
if operation == "/": #деление
    print("Результат")
    z = x / y
    print(z)
if operation == "^": #возведение в степень
    print("Результат")
    z = x ** y
    print(z)
