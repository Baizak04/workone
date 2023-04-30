# # class Cat(object):
# #     def talk(self):
# #         print("мяу...")

# # a = Cat()
# # a.talk()


# class Cat(object):
#     total = 0
#     @staticmethod
#     def count():
#         print("Всего кошек: ", Cat.total)
        
        
#     def __init__(self):
#         print("Родилась новая кошка! ")
#         self.name = input("Как мы ее назовем? ")
#         self.name += 1
#         self.__w = 300
#         self.hunger = 1
    
#     def __str__(self):
#         res = "Объект класса Cat\n name: " + self.name + "\nВес: " + str(self.__w)
#         return res
    
#     @property
#     def weight(self):
#         return self.__w
    
#     def talk(self):
#         print(self.name, ": Мяу")
        
#     def eat(self):
#         if self.hunger == 5:
#             print("кошка не голодна!")
#         else:
#             self.hunger += 1
#             self.__w += 30
#             print("Мур...")
    
#     def play(self):
#         self.talk()
#         self.__w -= 5
#         if self.hunger > 0:
#             self.hunger -= 1
#         else:
#             self.hunger = 1
            
# def main():
#     bagira = Cat()
#     choice = None
#     while choice != "0":
#         print \
#         ("""
#             Что будем делать
            
#             0 - выйти
#             1 - Поговорить с кошкой
#             2 - покормить
#             3 - Поиграть
#             4 - Взвесить
#             """)
#         choice = input(">>: ")
#         print()
        
#         if choice == "0":
#             print("Bye bye...")
        
#         elif choice == "1":
#             bagira.talk()
            
#         elif choice == "2":
#             bagira.eat()
            
#         elif choice == "3":
#             bagira.play()
            
#         elif choice == "4":
#             print("вес: ", bagira.weight, " гр. ")
            
#         else:
#             print("Неправильный ввод")
# main()


# 2)

class Purse:
    
    def __init__(self, valuta, name = 'Umar'):
        self.money = 0.00
        self.valuta = valuta
        self.name = name
        
    def top_up_balance(self, howmany):
        self.money = self.money + howmany
        
    def top_down_balance(self, howmany):
        if self.money - howmany < 0:
            print('Не достаточно средств')
            raise ValueError ('Не достаточно средств')
        self.money = self.money - howmany
        
    def info(self):
        print(self.money)
        
    def __del__(self):
        print('кошелек удален')
        return self.money
        
        
x = Purse('USD')
y = Purse('EUR', 'bill')
x.top_up_balance(100)
x.info()
del x