import random
class Enemy:  # создаем класс врага
    def __init__(self, name, health, attack):  # создаем врага
        self.health = health  # присваиваем переданное здоровье объекту
        self.attack = attack
        self.name = name

    def be_attacked(self, attack):  # быть атакованным
        self.health = self.health - attack  # уменьшение здоровья

    def say_health_and_attack(self):
        print(f"у {self.name} здоровье {self.health} и атака {self.attack}")



class User(Enemy):
    def __init__(self, name, health, attack, armor = 10):
        super().__init__(name, health, attack)
        self.__armor = armor

    def heal(self):
        health = self.health // 10
        self.health = self.health + health
        print(f"Ты восстановил: {health}, твое здоровье: {self.health}")

    def set_armor(self, armor):
        self.__armor = armor

    def get_armor(self):
        return self.__armor
    
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, armor):
        self.__armor = armor

        
    def secret_heal(self):
        health = 20
        self.health = self.health + health
        print(f"Ты восстановил: {health}, твое здоровье: {self.health}")

    def be_attacked(self, attack):  # быть атакованным
        damage = attack - self.armor
        if damage >= 0:
            self.health = self.health - abs(attack - self.armor)  # уменьшение здоровья
        
        
    

enemy1 = Enemy(name="Рыцарь", health=330, attack=10)  # создаем объект класса
enemy2 = Enemy(name="Боец", health=200, attack=18)
enemy3 = Enemy(name="Убийца", health=150, attack=25)
user1 = User("My name", 200, 16)
print(user1.name)
print(user1.armor)
print()

players = [enemy1, enemy2, enemy3]
user_enemy = random.choice(players)
print(f"твой соперник: {user_enemy.name}")


enemy = enemy1
enemy_2 = user1

hits = 0
win = False
while True:
    enemy.say_health_and_attack()
    enemy_2.say_health_and_attack()
    if enemy.health <= 0 and enemy_2.health <= 0:  # and - если оба условия верны, or - если одно из условий верно
        print('Ничья')
        win = True
    elif enemy.health <= 0:
        print('Второй победил')
        print(enemy_2.health)  # здоровье второго врага
        win = True
    elif enemy_2.health <= 0:
        print('Первый победил')
        print(enemy.health)
        win = True
    if win is True:
        print('hits', hits)
        break
    userInput = int(input("Введите:\n1 - лечение,\n2 - атака \n"))
    if userInput == 1:
        print("Лечение")
        enemy_2.heal()
    elif userInput == 2:
        print("Атака")
        enemy.be_attacked(enemy_2.attack)
    else:
        print("увеличиваем броню")
    if userInput == 99:
        print("Вы активировали чит:)")
        enemy_2.secret_heal()
        enemy.be_attacked(enemy2.attack)
                                        # вызываем метод "быть атакованным" и передаем ему атаку соперника
    enemy_2.be_attacked(enemy.attack)
    hits += 1

'''
l
-e 
--o 
---n 
--a 
-r 
d 
'''

    