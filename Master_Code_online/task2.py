# 1)
class Tester:
    
    def __init__(self, id):
        self.id = str(id)
        id = '224'
        
        
temp = Tester(12)
print(temp.id)
# id в этом случае будет атрибутом класса.

# 2)
def sum_o_t(sum):
    sum = [1]
    
    
sum = [2]
sum_o_t(sum)
print(sum)
# В функции создается новый объект списка и ссылка теряется. Это можно проверить, сравнив id sum до и после sum = [1].

# 3)
def sum_twitter():
    x = 100
    print(x)
    
    
x =+ 1
sum_twitter()

# 4)
i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2
# Следующее значения i - 6. Поскольку 6 делится на 3 без остатка, произойдет выход из цикла.

# 5)
name_age = {'John': 24, 'Peter': 30}
print(list(name_age.keys()))

# 6)
# def world():
#     x[0] = ['web']
#     x[1] = ['com']
#     return id(x)


# w = ['web', 'com']
# print(id(w) == world(w))

# 7)
def san(x):
    print(x + 1)
    
    
x = -2
x = 4
san(12)
# В функции san() передается значение 12. Оно инкрементируется на единицу и выводится. Поэтому в выводе 13

# 8)
# print([if i%2==0: i; else: i+1; for i in range(4)])

# 9)
# True = False
# while True:
#     print(True)
#     break

# 10)
print(chr(ord('b') + 1))

# 11)
def s1():
    global x
    x += 1
    print(x)
    
    
x = 12
print("x")
# Переменная x объявлена в функции как глобальная. Поэтому в выводе будет х. Если бы переменная была локальной в выводе было бы 13 х.

# 12)
x = [{1}] * 2
x[0].add(2)

print(x)
# [{1}] * 2 → [{1}, {1}]Но вторая ссылка указывает на первый объект, поэтому все изменения в первом, повлияют на второй и наоборот.

# 13)
a  = '1_var'
print(a.isidentifier())
# isidentifier() проверяет, можно ли использовать строку как название для переменной, функции, класса. Как мы знаем, идентификатор не может начинаться с числами поэтому получим False.

# 14)
def func():
    func.x = 5 
    return func


print(func().x)
# Функции могут хранить значения внутри себя как свойства. Это достигается за счет __dict__.

# 15)
# import sys


# try:
#     sys.exit()
#     print('Выход')
# finally:
#     print("Выполнено успешно")
# sys.exit() Останавливает выполнение приложения за счет создания исключения SystemExit. finally выполняется всегда, независимо от того, была ошибка или нет.

# 16)
# print('a' * 2, 'a' * 2.0)
# Строки и списки нельзя умножать на числа типа float, поэтому выражение после запятой выдаст ошибку 

# 17)
class PluginBase:
    subclasses = []
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)
        

class PlaginOne(PluginBase):
    pass


print(PluginBase.subclasses)
# Метод __init_subclass__ появился в Python 3.6 и вызывается в базовом классе всякий раз, когда создается новый подкласс.

# 18)
def format(): pass

print(format())
# Функция по умолчанию возвращает None

# 19)
# print(int(11.0) == int('11.0'))
# Ошибка появляется в int(‘11.0’), поскольку int не умееть работать с такими значениями (float в виде строки)

# 20)
print(print('py'))
# print(‘py’) -> выведет py и вернет None print(None) -> выведет None

# 21)
from random import random


def func(x = random()):
    return x


print(func() == func())
# Значения по умолчанию создаются только один раз и сохраняются в __defaults__.

# 22)
print(False + True)
# False это 0, True это 1;w 0 + 1 =1

# 23)
number_set = {range(4)}
print(number_set)
# range это отдельный объект и он так и сохраняется внутрь множества. Чтобы получить {0, 1, 2, 3}

# 24)
a = {1, 2, 3, 1, 2}
print(sorted(a))
# Множества это набор уникальных значений, поэтому копии пропадут

# 25)
# v = {1, 2, 3}
# print(a[1])
# Нельзя брать значения по индексу из множества!

# 26)
try:
    exit()
except SystemExit:
    print('OK')
# exit() выбрасывает ошибку SystemExit, которая позволяет выйти из приложения

# 27)
a = ['1', '2', '3']
print(sorted(a))
# Строки сравниваются по позиции в ASCII

# 28)
number_one = [1, '2', 3]
number_two = map(int, a)

print(sorted(number_two) == sorted(number_two))
# map это все тот же генератор, а значит пройтись по нему можно только один раз. В сравнении получаем [1, 2, 3] == [] -> False

# 29)
result = 0
for x, y in zip(range(3), range(5)):
    result += x + y
    
print(result)
# Если хотя бы один из итераторов в zip <<закончится>>б то цикл прекратит свое выполнение

# 30)
def func():
    try:
        return True
    finally:
        return False
    
    
print(func())
# finally выполняется всегда и, в данном случае, заменяет возвращаемое значение. Если после finally, будет pass, то вернется True