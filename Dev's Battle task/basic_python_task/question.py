



# # 2) 
# def multipliers():
#     return [lambda x : i * x for i in range(4)]
    
# print ([m(2) for m in multipliers()])

# # Результатом выполнения данного кода будет [6, 6, 6, 6], а не [0, 2, 4, 6].

# # Это объясняется тем, что замыкания в Python работают по принципу позднего связывания. Это означает, что значения переменных, используемых в замыканиях, ищутся во время вызова внутренней функции. Поэтому, когда вызывается любая из функций, возвращаемых multipliers(), значение i ищется исключительно в области видимости этой функции в данный момент. А значение i, вне зависимости от того, какая из функций вызывается, после завершения цикла for всегда равно 3. Таким образом, каждая возвращаемая функция умножает значение, которое ей передано, на 3, а поскольку в приведенном выше коде передается значение 2 , все они возвращают значение 6 (то есть 3 x 2).

# # Между тем, существует довольно распространенное заблуждение, что это как-то связано с лямбда-функциями (например, так сказано в книге «Автостопом по Python»). Но это не так. Функции, созданные с помощью лямбда-выражений, ни в коем случае не являются какими-то особыми, и в работе ничем не отличаются от функций, созданных с использованием обычной функции def.

# # 3)
# class Parent(object):
#     x = 1
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)

# # 4) 
# def div1(x,y):
#     print("%s/%s = %s" % (x, y, x/y))

# div1(5,2)

# # По умолчанию Python 2 автоматически выполняет целочисленное деление, если оба операнда являются целыми числами. В результате 5/2 — 2,5.

# # 5) 
# def div2(x,y):
#     print("%s//%s = %s" % (x, y, x//y))

# div2(5.,2.)

# # 6) 
# list = ['a', 'b', 'c', 'd', 'e']
# print(list[10:])

# # Данный код выдаст в виде результата пустой список [], а ошибка IndexError не возникнет.

# # Как известно, попытка доступа к элементу списка с использованием индекса, превышающего число элементов (например, операция list[10] в списке выше), приводит к ошибке IndexError. Однако, попытка получить доступ к срезу списка с начальным индексом, превышающем количество элементов в списке, не приведет к IndexError и просто вернет пустой список.


# # 7) 
# class Greetings:
#     def good_morning(name):
#         print(f'Good morning {name}')
        
#     def good_afternoon(name):
#         print(f'Good afternoon {name}')
        
#     def good_evening(name):
#         print(f'Good evening {name}')
        
        
# Greetings.good_afternoon('John')
# Greetings.good_morning('Peter')
# Greetings.good_evening('Jane') 


# # 8)
class Student:
    def __init__(self, first, last, age, major):
        self.first = first 
        self.last = last
        self.age = age
        self.major = major
    
    def profile(self):
        print(f"Student name {self.first + ' ' + self.last}")
        print(f"Student age: {self.age}")
        print(f"Major: {self.major}")
        
    
    
s = Student('Sally' , 'Harris', 20, 'Biology')    
    
s.profile()


# # 9) 
# def logger(function):
#     def wrapper(*args, **kwargs):
#         print(f"----- {function.__name__}: start -----")
#     return wrapper


# @logger
# def some_function(text):
#     print(text)

# some_function("first test")

# # 10)
# from functools import wraps

# def logger(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         """wrapper documentation"""
#         print(f"----- {function.__name__}: start -----")
#         output = function(*args, **kwargs)
#         print(f"----- {function.__name__}: end -----")
#         return output
#     return wrapper

# @logger
# def add_two_numbers(a, b):
#     """this function adds two numbers"""
#     return a + b

# a = add_two_numbers.__name__
# print(a)

# # @wraps
# # Этот декоратор обновляет функцию-обертку, чтобы она выглядела как оригинальная функция и наследовала ее имя и свойства.


# @repeat, который принимает в качестве аргумента количество вызовов. Затем декоратор определяет функцию wrapper, которая оборачивает декорируемую функцию. Функция wrapper вызывает декорируемую функцию столько раз, сколько указано в аргументе.

# # 12)
# from dataclasses import dataclass

# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     age: int
#     job: str

#     def __eq__(self, other):
#         if isinstance(other, Person):
#             return self.age == other.age
#         return NotImplemented

#     def __lt__(self, other):
#         if isinstance(other, Person):
#             return self.age < other.age
#         return NotImplemented

# john = Person(first_name="John", 
#               last_name="Doe", 
#               age=30, 
#               job="doctor",)

# anne = Person(first_name="Anne", 
#               last_name="Smith", 
#               age=40, 
#               job="software engineer",)

# print(john == anne)


# # 13)
class B:
    def b(self):
        print('b')
class C:
    def c(self):
        print('c')
class D(B, C):
    def d(self):
        print('d')
d = D()
d.b()
d.c()
d.d()

