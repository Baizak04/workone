# атрибуты - это переменные
# методы - это функция
class Car:
    wheels = 4

    def move(self):
        print("Начинаем движение на {} колесах".format(self.wheels))
        
    def change(self, wheels):
        print("Меняю колеса с {} на {}".format(self.wheels, wheels))
        self.wheels = wheels
    
toyota = Car()
honda = Car

print(toyota.wheels)
print(honda.wheels)

toyota.move()
toyota.change(3)
