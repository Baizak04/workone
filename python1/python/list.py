# список [list] - измениямый

# методы
# append, clear, copy, count, extend, index, insert, pop, remove,reverse, sort, sorted 

# elist = [21, 23, 344, 43434,]
# for n in elist:
#     print(n)

workdays = ['Понедельник', 'Вторник', 'Среда']
for i in workdays:
    print(i)
    
print('-------')
print(workdays[1])

workdays[1] = 'Суббота'
print(workdays[1])




# children = ['arbuzov', 'ivanov', 'petrov', 'Azat']

# children_2 = sorted(children)
# print(children_2)

# x = [1, 2, 3, 4]
# print(x, type(x), len(x))
# x.append(7)
# print(x)

# # Удалить элемент из списка
# del x[1]
# print(x, len(x))

# # Добавить
# x[1] = '2'
# print(x, len(x))

# #Итерация
# for item in x:
#     item =+ 2
#     print(item)
    
# print(x)


a = [1, 2, 3, 4, 5]
start = int(input("начальный срез: "))
end = int(input("конечный срез: "))
print(a[start:end])