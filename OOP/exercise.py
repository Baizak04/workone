class Human:
    
    # Статические поля
    default_name = 'No name'
    default_age = 0
    
    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичное
        self.name = name
        self.age = age
        # Приватное
        self.__money = 0
        self.__house = None
       
    
        
    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')
        
        
    def earn_money(self, amount):
        self.__money += amount
        print(f'sa{amount} money ciur {self.__money}')
        
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

if __name__ == 'main.py':
    print(Human.default_name)
    
    fedor = Human('Fedor', 32)
    fedor.info()
    fedor.earn_money(10_000)
    a = 0
    
    
class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.widht = w
        self.height = h
        
class DeskTable(Table):
    def square(self):
        return self.widht * self.length
    

class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.widht * self.length - monitor
    
    
t3 = ComputerTable(0.5, 0.6, 0.7)
print(t3.square(0.8))
    