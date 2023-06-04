class Car:
    def __init__(self, maker, model, color, price):
        self.maker = maker
        self.model = model
        self.color = color
        self.price = price
        
    def get_price(self):
        if hasattr(self, "discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def set_discount(self, amount):
        self._discount = amount
        
class Boat:
    def __init__(self, name):
        self.name = name
        
        
        
car1 = Car("BMW", "i8", "black", 5000000)
car2 = Car("Mercedes", "C-class", "white", 25000)
boat1 = Boat('Titanic')
print(type(car1))
print(type(boat1))
print(type(car1) == type(car2))

print(car1.get_price())
car2.set_discount(0.25)
print(car2.get_price())