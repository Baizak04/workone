from pprint import pprint
import math
import operator

class PersonTwo:
    name = 'max'
    age = 43
    
    
setattr(PersonTwo, 'hair_color', 'black')
pprint(PersonTwo.__dict__)



# 2)

class Computer:
    age: int = 5
    price: int = 200
    size: str = 'big'
    
print(getattr(Computer, 'sdf', str(math.pi)))
pprint(Computer.__dict__)


# 3)

class PersonThree:
    name = 'lisa'
    age = 12
    
    
l = PersonThree()
l.hair_color = 'blue'
print(getattr(PersonThree, 'hair_color', False))
print(isinstance(l, type), isinstance(l, int), sep='\n')

# 4)


class Ben:
    
    def add(self, x, y):
        return operator.add(x, y)
    

a = Ben()
print(a.add(13., 23.1))


# 5)

class L:
    x = 3
    y = 2
    
    def dubl(self):
        self.x = self.x
        self.y = self.y
        
        
a = L()
print(a.__dict__)
a.dubl()
print(a.__dict__)


# 6)

class Ci:
    
    def __init__(self, radius):
        self.radius = radius
        
    def calc_square(self):
        return math.pi * self.radius**2
    

c = Ci(3.4)
print(c.calc_square())