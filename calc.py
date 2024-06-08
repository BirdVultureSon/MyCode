def main():
    calculation()


#ввод значения
def input_value(seq): 
    s = seq
    user_value = float(input(f"Введите значеие {s}: "))
    return user_value

#ввод операции
def input_operation():
    user_operation = input('Введите операцию "*", "/", "+", "-": ')
    return user_operation

#сложение
def addition(value_one, value_two):
    x = value_one
    y = value_two
    result = x + y
    return result

#вычитание
def substraction(value_one, value_two):
    x = value_one
    y = value_two
    result = x - y
    return result

#умножение
def multiplication(value_one, value_two):
    x = value_one
    y = value_two
    result = x * y
    return result

#деление
def division(value_one, value_two):
    x = value_one
    y = value_two
    result = x / y
    return result

#ввод значений, выполнение операций и отображение результата
def calculation():
    value_one = input_value("1")
    operation = input_operation()
    value_two = input_value("2")

    if operation == "+":
        calculation_result = addition(value_one, value_two)
    if operation == "-":
        calculation_result = substraction(value_one, value_two)
    if operation == "*":
        calculation_result = multiplication(value_one, value_two)
    if operation == "/":
        calculation_result = division(value_one, value_two)

    print (value_one,operation,value_two,"=",calculation_result)



#main()