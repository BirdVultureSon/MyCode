import random


class Enemy:
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def be_attacked(self, take_attack):
        self.health = self.health - take_attack

    def _say_hello(self):
        print("hello")

    def __say_hi(self):
        print("hi")

    def say(self):
        self._say_hello()
        self.__say_hi()
        
enemy = Enemy(200, 10)
#print(enemy)


enemy2 = Enemy(200, 10)
enemy.say()
enemy._say_hello()
enemy._Enemy__say_hi()  #enemy.__say_hi()

enemy3 = Enemy(200, 10)



fighters = [enemy, enemy2, enemy3]

def choice_fighters():
    #fighter1 = random.choice(fighters)
    #fighters.remove(fighter1)
    #fighter2 = random.choice(fighters)
    no_fight = random.choice(fighters)
    fighters.remove(no_fight)
    return fighters


#print(enemy2.health, enemy2.attack)
#enemy2.be_attacked(10)
#print(enemy2.health)

choice_fighters()


hits = 0
enemy1 = fighters[0]
enemy2 = fighters[1]


while True:
    
    enemy.be_attacked(enemy2.attack)
    enemy2.be_attacked(enemy.attack)
    hits = hits + 1
    print(hits, enemy.health, enemy2.health)
    if enemy.health <= 0 and enemy2.health <= 0:
        print("Ничья!")
        break
    if enemy.health <= 0:
        print("Второй победил!")
        break
    if enemy2.health <= 0:
        print("Первый победил!")
        break

'''
    hits = 0 
win = False
 
# проверка на победу 
while True: 
if enemy.health <= 0 and enemy_2.health <= 0: # если здоровье обоих стало <= 0 
print('Ничья') 
win = True
elif
 
enemy.health <= 0: # или если здоровье 1 врага <= 0 
print('Второй победил') 
print("У него осталось здоровья", enemy_2.health)
win = True 
elif
 
enemy_2.health <= 0: # или если здоровье 2 врага <= 0 
print('Первый победил')
print("У него осталось здоровья", enemy.health) 
win = True 
if win is True:
 
# победа, это уже другой блок условий 
print('Ударов совершено', hits)
break 
hits += 1 
enemy.be_attacked(enemy_2.attack) 
enemy_2.be_attacked(enemy.attack)

дз:
Добавить третьего персонажа и сделать рандомный подбор соперников с помощью random.choice()


'''