class Sample():
    pass

my_sample = Sample()
print(type(my_sample))

class Dog():
    
    def __init__(self, breed):
        
        self.breed =  breed
try:
    my_dog = Dog()  
except TypeError:
    print("Ошибка")  
    
    
class Dog():
    
    def __init__(self, breed):
        
        self.breed =  breed
        
my_dog = Dog(breed='a')
# print(my_dog)
print(my_dog.breed)