import random

list = [1, 3, 4, 6, 7, "loose"]
def bonus_(): 
    counter = 1
    while counter < 2:
        bonus = random.choice(list)
        if bonus == "loose":
            counter = counter + 1
            bonus = random.choice(list)
    print(bonus)
    return bonus
bonus_()
    

