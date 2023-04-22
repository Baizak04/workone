# список [list] - измениямый

# методы
# append, clear, copy, count, extend, index, insert, pop, remove,reverse, sort, sorted 


children = ['arbuzov', 'ivanov', 'petrov', 'Azat']

children_2 = sorted(children)
print(children_2)

x = [1, 2, 3, 4]
print(x, type(x), len(x))
x.append(7)
print(x)

# Удалить элемент из списка
del x[1]
print(x, len(x))

# Добавить
x[1] = '2'
print(x, len(x))

#Итерация
for item in x:
    item =+ 2
    print(item)
    
print(x)