class Car:
    color = "Черный"
    speed = 120
    
    def __init__(self, color, speed):
        self.speed = speed
        self.color = color

    def beep(self):
        print("бип")
    
    def say_speed(self):
        print(f"скорость: {self.speed}")
    
    def say_color(self):
        print(f"цвет: {self.color}")

car1 = Car("Красный", 90)
car2 = Car("Зеленый", 150)
car1.beep()
car2.beep()
car1.say_speed()
car1.say_color()


class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print(self.name)

    def say_age(self):
        print(self.age)

person1 = Person("Ваня", 14)
person2 = Person("Коля", 13)
person1.say_name()
person1.say_age()
person2.say_name()
person2.say_age()