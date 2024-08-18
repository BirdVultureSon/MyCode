import random
class Insects:

# 1. задаем атрибуты насекомого (имя, еда, чувство сытости)
    def __init__(self, name, food = 3, satiety = 2):
        self.name = name
        self.food = food
        self.satiety = satiety

# 2. после еды увеличиваем/уменьшаем нужные атрибуты      
    def eat(self):
        if self.food > 0:
            self.food = self.food - 1
            self.satiety = self.satiety + 1
            print(f"{self.name} you have take food, satiety {self.satiety}, food: {self.food}")
        else:
            print(f"{self.name}, you don't have food")

# 3. после поиска еды уменьшаем/увеличиваем нужные атрибуты
    def find_food(self):
        self.food = self.food + 5
        self.satiety = self.satiety - 1
        print(f"{self.name} you have find food!!!, satiety {self.satiety}, food: {self.food}")

# 4. унаследуем класс пчелы от класса насекомых
class Bee(Insects):
# 5. задаем атрибуты пчелы (количество меда, помимо остальных атрибутов)
    def __init__(self, name, food = 3, satiety = 2, honey = 5):
        super().__init__(name, food, satiety)
        self.honey = honey

# 6. после сбора меда увеличиваем/уменьшаем нужные атрибуты
    def collecting_honey(self):
        self.honey = self.honey + 2
        self.satiety = self.satiety - 1
        print(f"{self.name} you have collect honey! Honey: {self.honey}, satiety: {self.satiety}, food: {self.food}")

        
# 7. данный метод готов, нужно будет его запустить в самый последний момент и объяснить, как он работает
    def live(self):
        living = True
        if self.satiety <= 0:
            print(f'{self.name} died :(')
            living = False
            return living
        action = random.randint(1,3)
        if self.satiety < 4:
            if self.food == 0:
                self.find_food()
            else:
                self.eat()
        else:
            if action == 1:
                self.collecting_honey()
            elif action == 2:
                self.eat()
            else:
                self.find_food()

                
# 8. пчела живет 30 дней (если она погибает, то итерации заканчиваются)
bee = Bee("Майа")
for i in range(30):
    print(i)
    if bee.live() == False:
        print("Пчела умерла:(")
        break
    if bee.satiety <= 0 or i == 29 :
        print("Прошло 30 дней. Пчела die")