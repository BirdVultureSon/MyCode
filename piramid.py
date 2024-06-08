import math


def center_word(word):
    long_word = len(word)
    #print(long_word)
    center = long_word / 2
    #print(center)
    center = math.ceil(center)
    #print(center)
    return center

def with_start_space(word):
    count = 0
    count2 = 1
    center = center_word(word)
    while count < len(word):
        space = ""
        if count < center:
            space = "-" * count2
        else:
            #space = "-" * (len(word) - 1 - count2)
            space = "-" * (len(word) - count)
        print(space + word[count])
        count = count + 1 
        count2 = count2 + 1


def without_start_space(word):
    count = 0
    center = center_word(word)
    while count < len(word):
        space = ""
        if count < center:
            space = "-" * count
        else:
            space = "-" * (len(word) - 1 - count)
        print(space + word[count])
        count = count + 1 
        
def start_piramid():
    word = "Михаил"
    center = center_word(word)
    print(center)
    print("start")
    with_start_space(word)
    without_start_space(word)
