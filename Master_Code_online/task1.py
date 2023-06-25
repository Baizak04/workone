# 1)
t = (1, 2)
t *= 2
print(t)
# Оператор * конкатенирует кортежи

# 2)
a = (1, 2, (4, 5))
b = (1, 2, (3, 4))
print(a < b)
# Поскольку первый элемент в подкортеже а больше первого элемента в подкореже b, выведется False

# 3)
i = 1 
while True:
    if i%0O7 == 0:
        break
    print(i)
    i += 1
    
# 4)
def name(fname, value):
    print(fname(value))
    
    
name(max, [1, 2, 3])
name(min, [1, 2, 3])
# Функцию можно передавать в качестве аргумента для другой функции

# 5)
import re
a = re.split('\W+', 'Hello, hello, hello.')
print(a)
# Функция split() разбивает строку по шаблону, указанному в аргументах

# 6)
a = (0, 1, 2, 3, 4)
b = slice(0, 2)
print(a[b])

# 7)
def foo(x):
    x = ['def', 'abc']
    return id(x)


q = ['abc', 'def']
print(id(q) == foo(q))
# В функции создан новый объект

# 8)
x = [i**+1 for i in range(3)]
print(x)
# i**+1 оценивается как (i) ** (+1).

# 9)
print([i.lower() for i in "MASTER CODE ONLINE"])