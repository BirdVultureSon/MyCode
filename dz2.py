
'''
дз
написать консольное приложение в диапозоне от 0 до 100, чтобы оно ходило с определенным шагом бесконечно в диапозоне от 0 до 100
'''


coord = 0
change = 10
flag = "y"
while flag == "y" :
    if coord <= 0:
        print("hello")
        coord = coord + change
    if coord >= 100:
        print("hello")
        coord = coord - change
        

'''
for i in range(0, 100, change):
    print(change)
    i = i + 1
    if i == 100:
        change = -10
'''