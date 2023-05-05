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
    spec = 'mammal'
    def __init__(self, breed, name, spots):
        
        self.breed =  breed
        self.name = name
        self.spots = spots
        
my_dog = Dog(breed='a', name='sam', spots=False)

# print(my_dog)
print(my_dog.breed, my_dog.name, my_dog.spots)