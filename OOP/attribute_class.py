print(isinstance(4, str))


class Person:
    age = 16
    name = 'Max'
    
    
print(Person.name)
print(getattr(Person, 'x', 'такой атрибута нету'))
# функция getattr() если атрибута нету то ошибку можно поменять на свое слово / обработка ошибка исключения

setattr(Person, 'name', 'Azat')
print(Person.name)
# функция setattr() изменить значения аттрибута еще может создать новый аттрибут

print(Person.__dict__)

#метод  __dict__ выводить словар 

# practic

class A:
    x: float = 17.8
    

print(A.x)

class B:
    x: int = 15
    y: int = 7
    
    
print(getattr(B, 'x') + getattr(B, 'y'))
print(getattr(B, 'z', 'такое нету'))


class C:
    pass


setattr(C, 'x', 11)
C.y = 'hello world'
print(getattr(C, 'y').upper())