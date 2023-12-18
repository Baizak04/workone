class Car:
    model = "Mersedec"
    engine = 1.6
    
    def drive():
        print("let's go")
        
        
a = Car.__dict__
print(a)
Car.drive()

getattr(Car, 'drive')()

a = Car()
a = a.__dict__
print(a)