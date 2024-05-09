class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    
    def beep(self):
        print("бип")
    
    def say_speed(self):
        print(f"скорость: {self.speed}")
    
    def say_color(self):
        print(f"цвет: {self.color}")

class Car(Transport):
    def __init__(self, speed, color, owner):
        super().__init__(speed, color)
        self.owner = owner
        self.wheels = 4
    
    def say_owner(self):
        print(f"Владелец: {self.owner}")
car1 = Car(120, "Белый", "Коля")
car1.say_owner()
car1.beep()


class Bus(Transport):
    def __init__(self, speed, color, seats):
        super().__init__(speed, color)
        self.seats = seats
        self.wheels = 6
    
    def say_owner(self):
        print("Владелец: Отсутствует.")
bus1 = Bus(50, "Белый", 16)
bus1.say_color()
bus1.say_owner()
bus1.say_speed()

'''
Добавить в классы машины и автобуса методы сообщения количества колес, а для автобуса еще метод для сообщения количества посадочных мест. 
Сделать класс Student, унаследованный от класса Person, у которого будет свойства "школа" и "класс" и методы для сообщения значений этих свойства.
'''