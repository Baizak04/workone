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

