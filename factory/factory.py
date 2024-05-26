import time


class Store:
    def __init__(self, n):
        self._balance_value = n

    @property
    def balance(self):
        return self._balance_value
    
    @balance.setter
    def balance(self, balance_change):
        self._balance_value += balance_change
    
    '''
    
    def input(self):
        self.balance += 1

    def output(self):
        if self.balance > 0:
            self.balance -= 1
            out = 1
        else:
            out = 0
                  
        return out
    
    def show_balance(self):
        return self.balance
    
    
        


class Machine:
    def __init__(self, productivity ):
        self.productivity = productivity


    def readiness(self): #Счетчик готовности продукции
        self.ready = 0
        while self.ready < 10:
            print(self.ready)
            time.sleep(0.1)
            self.ready += 1
            
        return self.ready   
    
    def production(self): #Производство, работает пока на складе сырья остаток больше 0. Готовая продукция складывается на склад готовой продукции
        self.raw = store_one.output()
        
        if self.raw > 0:
            print ("Вход на станок", self.raw)
            self.complete = self.readiness()
            print(self.complete)
            if self.complete == 10:
                store_two.input()
                print("Остаток на складе сырья", store_one.show_balance())
                print("Остаток на складе продукции", store_two.show_balance())
                self.production()

'''       

class Machine:
    def __init__(self, need, productivity ):
        self.need = need
        self.productivity = productivity


    def readiness(self): #Счетчик готовности продукции
        self.ready = 0
        while self.ready < 100:
            print(f"{self.ready}%")
            time.sleep(0.1)
            self.ready += 10
            
        return self.ready   
    
    def production(self): #Производство, работает пока на складе сырья остаток больше 0. Готовая продукция складывается на склад готовой продукции
        self.raw = store_one.balance
        self.raw_outgo = self.raw - self.need

        if self.raw_outgo >= 0:
            print (f"Вход на станок {self.need} единиц")
            store_one.balance = - self.need
            self.complete = self.readiness()
            print(f"{self.complete}%")
            if self.complete == 100:
                store_two.balance = self.productivity
                print(f"Остаток на складе сырья {store_one.balance} единиц")
                print(f"Остаток на складе продукции {store_two.balance} единиц")
                self.production()

    
store_one = Store(int(input("Введите количество сырья: "))) #Склад готовой продукции
print("Остаток на складе", store_one.balance)

machine_one = Machine(2, 8) #станок, задаем поребление сырья и выход продукции

store_two = Store(0) #Склад готовой продукции





machine_one.production()