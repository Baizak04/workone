class Car:
    name = "Mazda"
    name_two = "Honda"


c1, c2 = Car(), Car()
a = c1.name
a2 = c2.name_two
print(a)
print(a2)

class B:
    
    name = "Test"
    
    def get(self):
        return self.name
    

b = B()
print(b.name)
print(b.get())