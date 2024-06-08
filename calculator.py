# Калькулятор



def main():
    calculation()

def value1():
    global x
    x = float(input("Введите значение 1: "))
    return x

def operate():
    operation= str(input("Введите операцию +, -, * , /, ^: "))
    return operation


def value2():
    global y
    y = float(input("Введите значение 2: "))
    return y

def input_value(msg):
    x = float(input(f"Введите значение {msg}: "))
    return x 

def calculation():
    x = value1()
    operation = operate()
    y = value2()


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
    
    

main()

'''
class TestArea(unittest.TestCase):

    def test_news(self):
        self.assertEqual(two.sum(1, 2), 3)
        self.assertEqual(two.sum(3, 4), 3)
        self.assertEqual(two.sum(3, 4), 7)
        self.assertEqual(two.sum(3, 2), 3)
output = StringIO()
tests = unittest.TestLoader().loadTestsFromTestCase(TestCirkleArea)
test_result = unittest.TextTestRunner(stream=output).run(tests)
print(output.getvalue())
'''