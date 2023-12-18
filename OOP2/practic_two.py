class Car:
    model = "BMW"
    engine = 1.6
    
    
result = Car.__dict__
print(result)

a1 = Car()
a1.seat = 4
result = a1.__dict__
print(result)