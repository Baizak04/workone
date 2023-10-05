class Car:
    def __init__(self, name, wheels=4):
        self.name = name
        self.wheels = wheels

    def move(self):
        print("{}Начинает движение на {} колесах".format(self.name, self.wheels))
        
    def change(self, wheels):
        print("{} Менят колеса с {} на {}".format(self.name, self.wheels, wheels))
        self.wheels = wheels
    
toyota = Car(name="Toyota", wheels=6)
honda = Car(name="Honda")

toyota.move()
toyota.change(10)
toyota.move()

honda.move()

