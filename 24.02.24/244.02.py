
import math

# Функция для проверки простого числа
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Функция для вычисления факториала
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Функция для нахождения корня числа
def square_root(x):
    if x < 0:
        raise ValueError("Квадратный корень из отрицательного числа не существует")
    return math.sqrt(x)

# Пример использования функций
num = int(input("Введите число: "))
if is_prime(num):
    print(f"{num} - простое число")
else:
    print(f"{num} - составное число")

print(f"Факториал числа {num} равен {factorial(num)}")

try:
    sqrt_num = square_root(num)
    print(f"Квадратный корень из {num} равен {sqrt_num}")
except ValueError as e:
    print(e)


