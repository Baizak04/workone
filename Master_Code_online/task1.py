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
# Мы перебираем все символы в строке

# 10)
a = [1, 2]
b = [3]
print(*a, *b)
# *a и *b распаковывает списки п передает все их элементы в *args у print(*args). Так можно быстро вывести список без квадратных скобок и запятых

# 11)
x = 5 ** 1
assert (x == 25, 'Error')
# assert это оператор, первым  аргументом он принимает непустой кортеж. Это означает, что assert постоянно будет принимать True

# 12)
x = 5.99
print(int(x))
# int(x) отбрасывает дробную часть

# 13)
class Foo:
    
    def __init__(self, x):
        self.x = x
        
        
    def __hash__(self):
        return self.x
    
    
print(hash(Foo(-1)))
# Поскольку -1 зарезервировано Python, класс не может его вернуть как хеш и поэтому использует -2

# 14)
from contextlib import contextmanager


@contextmanager
def atomic():
    try:
        yield
    except Exception:
        print('error')
    else:
        print('ok')
        
        
@atomic()
def ok():
    pass


ok() 
# @contextmanager можно использовать как декоратор.Тогда управление переходит декорируемой функции при вызове yield.

# 15)
class Inspector:
    
    def __getitem__(self, index):
        return type(index)
    
    
print(Inspector()[1:2])
# __getitem__() вызывается когда мы хотим получить объект по индексу и может принимать любые значения. slice() – типы для создания срезов



# 16)
class Inspector:
    
    def __getitem__(self, index):
        return type(index)
    
    
print(Inspector()[object()])
# getitem() вызывается когда мы хотим получить объект по индексу и может принимать любые значения.

# 17)
class MyList:
    
    def __getitem__(self, index):
        return index + 1
    
    
    def __class_getitem__(cls, item):
        return f'{cls.__name__}[{item.__name__}]'
    
    
print(MyList[int])
# По PEP506,__class_item__() используется когда мы пробуем взять значение с помощью квадратных скобок из класса, а не экземпляра. Часто подобное можно увидеть в Type Hints, например, iterable[int]

# 18)
# for i in range(3.0):
#     print(i)
# range() не работает с числами типа float

# 19)
def func():
    try:
        return 1
    finally:
        return 2
    
    
print(func())
# Поскольку finally выполняется всегда,  return 1 передает управление ему, а тот возвращает 2.

# 20)
class Test:
    
    def __init__(self, value):
        self.value = value
        
        
    def __str__(self):
        return f'{self.value}'
    
    
    def __add__(self, other):
        return self.value + other
    
    
print(1 + Test(1))
# __add__() вызывается у int, а он не знает что делать с Test. Если мы напишем Test(1) + 1, то все сработает  и ответ будет 2.