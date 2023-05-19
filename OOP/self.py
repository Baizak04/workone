class A:
    
    def set_number(self):
        self.name = 20
        
        
a = A()
a.set_number()
print(a.__dict__)



class Person:
    age = 19
    
    
    def __init__(self, height, name):
        self.height = height
        self.name = name
        
        
p = Person(143, 'jacob')
print(p.__dict__)