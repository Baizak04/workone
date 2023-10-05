class Car:
    __wheels = 4
    
    @property
    def wheels(self):
        return self.__wheels
    
    @wheels.setter
    def wheels(self, num):
        print("Кто-то ставит нам колесю")
        if num > 5:
            num = 4
        self.__wheels = num
        
    @wheels.deleter
    def wheels(self):
        print("Кто-то снимает наш колеса")
        
car = Car()

print(car.wheels)
car.wheels = 10
print(car.wheels)
del car.wheels
print(car.wheels)