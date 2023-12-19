class A:
    
    def _protected(self):
        print("This is protected method")
        
    def __private(self):
        print("This is private method")
        
    
a  = A()
a._A__private()



class Car:
    name = "car-1"
    
    def drive(self):
        print("60 km/h")
        
    
class Bmw(Car):
    
    def drive(self):
        return super().drive()
    
    
class Bmw(Car):
    
    def drive(self):
        print("100 km/h")
        
        
bmw = Bmw()
print(bmw.name)
print(bmw.drive())