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



class Person():
    name = 'Baizak'
    age = 18
    
    
p_one = Person.age
print(p_one)


class Hamster:
    color = 'white'
    
    
tom = Hamster()
del tom
print(id(tom))


class PersionCat:
    breed = 'persian'  #attrinute of this class
    age = 12.0   #float
    
    
class SiberianCat:
    breed = 'siberian'
    age = 0.5
    

class BengalCat:
    breed = 'bengal'
    age = 2.0
    
    
tom = PersionCat()
garfield = SiberianCat
maxim = BengalCat

print(type(tom), type(garfield), type(maxim), sep='\n')
print(isinstance(tom, PersionCat)) #принадлежит ли на класс 
