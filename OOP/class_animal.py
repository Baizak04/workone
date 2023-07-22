class Animal:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, value):
        self.name = value
    
    def get_name(self):
        print(self.name)

class Cat(Animal):
        
    def mau(self):
        print("Mau-mau")
    
    
class Dog(Animal):
     
    def __init__(self, last_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_name = last_name
     
    def gav(self):
        print("Gav-gav")
        
        
cat = Cat("Bob", 2)
cat.get_name()
print(cat.name)
print(cat.age)
cat.mau()
cat.set_name("Bax")
print(cat.name)
Cat("Murka", 3).get_name()

dog = Dog(last_name="Johns", name="Bat", age=4)
print(dog.name)
print(dog.last_name)
dog.gav()

