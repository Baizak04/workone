class Person:
    name = 'Ivan'
    age = 30
    
    
a = Person.name
print(a)
result = Person.__dict__
print(result)
a = getattr(Person, 'name')
print(a)