#1 код

d = {True: "yes", 1: "no", 1.0: "maybe"}
print(len(d))

# это  одинаковых объекта, у них один и тот же хеш и True == 1 == 1.0 -> True, поэтому в результате получим одно значение

# # 1. 1
# # 2. 2  *
# # 3. 3
# # 4. Ошибку
  


# #2 код 

x = [{1}] * 2
x[0].add(2)
print(x)

#[{1}] * 2 -> [{1}, {1}] Но вторая ссылка указывает на первый объект,поэтому все
#изменение в первом,повлияют на второй и новорот.

# # 1. [{1,2}, {1}]
# # 2. [{1,2}, {1,2}] *
# # 3. [{1}, {1}]
# # 4. Ошибка



# #3 код

# s = {1, 2, 3}
# print(s[1])

# Множество-неиндексируемая коллекция,а значит мы не можем получить значение по индексу ([1])

# # 1. 1
# # 2. 2
# # 3. Ошибку *
# # 4. 3




# #4 код

odd = lambda x: bool(x % 2)
numbers = [n for n in range(10)]
print(numbers)
n = list()
for i in numbers:
    if odd(i):
        continue
    else:
        break

# #Код возвращает новый список,содержащий целые числа до 10 (иключая 10)

# 1. [0, 2, 4, 6, 8, 10]
# # 2. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  *
# # 3. [1, 3, 5, 7, 9]
# # 4. Ошибка



# #5 код

def foo(k):
    k[0] = 1
q = [0]
foo(q)
print(q) 

# #Списки передаются по ссылке.

# # 1. [0]
# # 2. [1]  *
# # 3. [1,0]
# # 4. Ошибку



# #6 код

print([1, 2, 3] == sorted ([1, 2, 3]))
print((1, 2, 3) == sorted ((1, 2, 3)))

# #sorted вщзвращает отсортированный список элементов последовательности.Во втором случае список не равен кортежу.

# # 1. True, False  *
# # 2. False, True
# # 3. False, False
# # 4. True, True




# #7 код

def foo(fname, val):
    print(fname(val))
foo(max, [1, 2, 3])
foo(min, [1, 2, 3])

# # #Имена функций можно передовать в качества аргументов в другие функции.

# # 1. 3,1   *
# # 2. 1,3
# # 3. Ошибка
# # 4. Перечисленные варианты не подходят




# #8 код

a = ([],)
a[0].extend([1])
print(a[0] == [1])

# Сам кортеж представляет собой неизменямый объект, но список,как
# изменяемая последовательность,может быть расширен.

# # # 1. True  *
# # # 2. False
# # # 3. Error
# # # 4. Ошибка




# #9 код

class A:
    n = 0

    def __str__(self):
        return str(self.n + 9)
    
    def __repr__(self):
        return str(self.n - 9 / 9)
    
print({A(), A()})

# # # Объекты класса не могут сравниться друг с другом,поэтому они считаются разными объектами.

# # 1. {-1.0}
# # 2. {-1.0, -1.0}
# # 3. {-1.0,9}
# # 4. Будет Ошибка



# #10 код

x = ['ad', 'cd']
for i in x:
    i.upper()
print(x)

# # #Функция upper() не изменяет исходную строку,а возвращает новую,котороя здесь не было нигде сохранена.

# # 1. ['ad', 'cd']  *
# # 2. ['AB', 'CD']
# # 3. ['None', 'None']
# # 4. Ничто из перечисленного


# #11код

# x = [i ** +1 for i in range(3)]
# print(x)

# # i** +1 Оценивается как (i)**(+1)

# # 1. [0, 1, 2]  *
# # 2. [1, 2, 5]
# # 3. [1, 2, 3]
# # 4. Error


# #12 код

x = 10.0
y = (x < 100.0) and isinstance(x, float)
print(y)

# Обе части - (x < 100.0) и isinstance(x, float) - правдивы,т.e.равны True.
# Следовательно,все выражение оценивается как True.

# # 1. False
# # 2. True  *
# # 3. 1
# # 4. 0


# #13 код

s = 'foo'
t = 'bar'
print('bar' in 2 * (s + t))

# Оператор + объудиняет строки,а оператор*умножает.Результат 2*(s + t) - "foorbarfoorbar",
# a в этой строке содержится подстрока "barf.

# # 1. True *
# # 2. False
# # 3. Error
# # 4. Ошибка


# #14 код

f = None
for i in range (5):
    with open("data.txt", "w") as f:
        if i > 2:
            break
print(f.closed)

# Оператор WITH при использовании с открытым файлом гарантирует,что объект файла будет закрыт при выходе из блока with.

# # 1. True  *
# # 2. False
# # 3. None
# # 4. Error


# # 15 код 

dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("age")
print(temp)

# # # ???

# # 1. Error
# # 2. None   *
# # 3. Mike
# # 4. 8000  



# # 16 код
 
a = [1,2,3]
print(a[1]) 

# # # ???

# # 1. 1
# # 2. 2  *
# # 3. 3 
# # 4. Ошибку   


# # 17 код 

b = [1,2] == (1,2)
print(b)

# # # ???

# # 1. True
# # 2. False  *
# # 3. Ошибку
# # 4. 1,2


# #18 код 
 
b = set("ppp")
print(str(b) == "p")

# # #???

# # 1. True
# # 2. False  *
# # 3. Ошибку
# # 4. "ppp"


# # 19 код 

a = 10
print(b)

# # #???

# # 1. 10
# # 2. TypeError
# # 3. ValueError
# # 4. NameError  *



# # 20 код

try:
    b = 1 / 0
except ZeroDivisionError:
    b = 0
print(b)

# #  ???

# # 1. 1
# # 2. 0  *
# # 3. Ошибку
# # 4. ZeroDivisionError



# #21 код

# a = int("qwerty")
# print(a)

# # #???

# # 1. 123456
# # 2. ValueError  *
# # 3. TypeError
# # 4. qwerty



# #22 код

try:
    a = 2 + '1'
    print(a)
except TypeError:
    print("Error") 

# # #???

# # 1. Error  *
# # 2. 3
# # 3. Ошибку
# # 4. TypeError



# #23 код

try:
    print(1)
except Exception:
    print(0)

# # #???

# # 1. 1  *
# # 2. 0
# # 3.Ошибку
# # 4. TypeError


# #24 код

a = {1: 5, 2: 3, 3: 4}
print(a.pop(4, 9))

# метод pop()возвращает значение переданного ключа, в словаре нет,-значение,заданное по умолчанию(второй аргумент).

# # 1. 9  *
# # 2. 3
# # 3. Слишком много аргументов для метода pop()
# # 4. 4



# #25 код 

# my_tuple = (1, 2, 3, 4)
# my_tuple.append((5, 6, 7))
# print(len(my_tuple))

# кортежи неизменяемы и не имеют моетода append.

# # 1. 1
# # 2. 2
# # 3. 3
# # 4. Ошибка  *


# # 26 код

a = {1: "A", 2: "B", 3: "C"}
for i in a:
    print(i, end=" ")

# В цикле перебираются ключи словаря.

# # 1. 1 2 3        *
# # 2. 'A' 'B' 'C'
# # 3. 1 'A' 2 'B' 3 'C'
# # 4. Ошибка,должно быть:for i in a.items():


# # 27 код

w = "hello"
v = ('a', 'e', 'i', 'o', 'u')

#  Кортеж 'V' используется для генерации списка,содержащего гласные
#  из 'w'.В результате список содержит лишь гласные из строки "hello"

# # 1. [x for w in v if x in v]
# # 2. [x for x in w if x in v]  *
# # 3. [x for x in v if w in v]
# # 4. [x for v in w for x in w]




# # 28 код 
 
x = 1

def cg():
    global x
    x = x + 1

cg()
print(x)

# Поскольку переменная х была объявлена как глобальная,она легко
# модифицируется внутри функции.Поэтому в выводе будет 2.

# 1. 2  *
# 2. 1
# 3. 0
# 4. Ошибка


# 29 код
x = 100
def f1():
    global x
    X = 90

def f2():
    global x
    x = 80
print(x)
# переменная х объявлена как глобальная внутри функций f1 и f2.

# 1. 100   *
# 2. 90
# 3. 80
# 4. Ошибка


# 30 код
l1 = [10, 20, 30]
l2 = [-10, -20, -30]
l3 = [x + y for x, y in zip(l1, l2)]
print(l3)
# код возвращается х + у для х из списка l1 y из l2.Значит l3=[10-10, 20-20, 30-20],то есть [0, 0, 0].

# 1. Ошибка
# 2. 0
# 3. [-20, -60, -80]
# 4. [0,0,0]         *


#31 код 
a = {1: 5, 2: 3, 3: 4}
a.pop(3)
print(a)
# метод pop() удаляет элемент по переданному ключу.

# 1. {1:5}
# 2. {1:5,2:3}  *
# 3. {1:5,3:4}
# 4. Ошибку

#32 код
import re
re.compile('hello', re.X)
# Функция compile компилирует паттерн регулярного выражения в
# объект регулярного вырожения.Re.X -это флаг,также используемый как re.VERBOSE.VERBOSE

# 1. ['h','e','l','l','o']
# 2. re.compile("hello",re.VERBOSE)  *
# 3. Ошибка
# 4. мусорное значения


# 33 код
a = {1: "A", 2: "B", 3: "C"}
print(a.setdefault(3))
#  setdefault() аналагичен get(),но устанавливает dict[key]=default,если указонного ключа нет в словаре.

# 1. {1: "A", 2: "B", 3: "C"}
# 2. C      *
# 3. {1;3,2:3,3:3}
# 4. Для словарей нет метода setdefault.


# 34 код 
def f1(a, b=[]):
    b.append(a)
    return  b
print(f1(2, [3, 4]))
# число 2 добавляется в список [3,4].Поэтому output кода - [3,4,2].append

# 1. [3,2,4]
# 2. [2,3,4]
# 3. [3,4,2]   *
# 4. Ошибка


# 35 код
x = "abcdef"
i = "a"
while i in x:
    x = x[1:]
    print(i, end=" ")
# Строка х укорачивается на один символ в каждой итерации.
# 1. a a a a a a 
# 2. a           *
# 3. Никакого вывода не будет
# 4. Ошибка


#36 код 
a = {1, 2, 3}
b = {1, 2, 3}
c = a.issubset(b)
print(c)
# Метод issubet()возвращает True,усли является подмножестом a.

# 1. True                                     *
# 2. Ошибка метода issubet()не существует
# 3. SyntaxError для метода issubet()
# 4. False


# 37 код 
# a = {1: "A", 2: "B", 3: "C"}
# print(a.get(5,4))
# Метод get()вшзвращает значение ключа,если ключ присутствует в
# словаре,и значение по умолчанию (второй параметр),если такого ключа нет.

# 1. Ошибка неверный синтаксис
# 2. A
# 3. 5
# 4. 4        *


# 38 код
# x = "abcdef"
# i = "a"
# while i in x[:-1]:
#     print(i, end=" ")
# Строка х не изменаются,i есть в х [:-1]

# 1. a a a a 
# 2. a a a a a 
# 3. a a a a a......     *
# 4. a


# 39 код
x = "abcdef"
i = "a"
while i in x:
    x = x[:-1]
    print(i, end=" ")
# Строка уменьшается на один символ в каждой итерации.

# 1. i i i i i
# 2. a a a a a a    *
# 3. a a a a 
# 4. Ничто из перечисленного


# 40 код
# f = None
# for i in range (5):
#     with open("date.txt", "w") as  f:
#         if i > 2:
#             break
# print(f.closed)
# Инструкция with,применяемая при открытии файла гарантиоует,что объект файла будет закрыт.
    
# 1. True   *
# 2. False
# 3. None
# 4. Ошибка

