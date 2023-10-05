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



# practic 

class A:
    def set_values(self, x, y):
        self.x = x
        self.y = y
        
    def send_sum(self):
        return self.x + self.y
    
    
a = A()
a.set_values(5, y=2)
result = a.send_sum()

print(result)


class PersonOne:
    
    def __init__(self, age:int, name:str):
        self.age = age
        self.name = name
        

p1 = PersonOne(14, 'xs')
p2 = PersonOne(22, 'liza')

print(p1.name, p2.name)
print(p1.age, p2.age)



class Triangle:
    
    def __init__(self, a: float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c
        
    def check_equals(self):
        return self.a == self.b or self.b == self.c or self.a == self.c
    
    
t = Triangle(1, 23, 34.)
print(t.check_equals())