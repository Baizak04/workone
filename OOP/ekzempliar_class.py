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