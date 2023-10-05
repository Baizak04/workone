# Обращение к экземплярам классов

class Person:
    age = 18
    height = 175
    
    
person_one = Person()
person_two = Person()

person_one.hair_color = 'black'
person_two.hair_color = 'white'
person_one.height = 165

print(person_one.__dict__, person_two.__dict__, Person.__dict__, sep='\n')


# practic

class Person:
    age: int = 20
    height: int = 170
    
    
person_one = Person()
person_two = Person()

person_one.height = 160
print(person_one.__dict__)

person_two.hair_color = 'yellow'
print(person_two.__dict__)

print(Person.__dict__)



class Cat:
    age: int = 2
    breed: str = 'Bengal'
    
tom = Cat()
setattr(tom, 'age', 1)
print(getattr(Cat, 'breed'), getattr(Cat, 'age'), sep='\n')
print()
print(tom.__dict__, tom.age)


class Car:
    speed: float = 90.0
    color: str = 'red'
    
    
print(Car.speed, Car.color, sep='\n')