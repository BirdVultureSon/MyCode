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
        
enemy = Enemy(330, 10)
#print(enemy)


enemy2 = Enemy(200, 18)
enemy.say()
enemy._say_hello()
enemy._Enemy__say_hi()  #enemy.__say_hi()

#print(enemy2.health, enemy2.attack)
#enemy2.be_attacked(10)
#print(enemy2.health)
hits = 0
while True:
    enemy.be_attacked(enemy2.attack)
    enemy2.be_attacked(enemy.attack)
    hits = hits + 1