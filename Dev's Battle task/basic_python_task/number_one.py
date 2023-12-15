# a = "123.45"
# b = 78
# a_float = float(a)
# b_float = float(b)
# print(a_float)  
# print(b_float)

# numbers = [1, 2, 3, 4]
# def square(x):
#     return x * x
# squared_numbers = map(square, numbers)
# print(list(squared_numbers))  

# number = 123
# if isinstance(number, int):
#     print("It's an integer!")
    
# # value = -1
# # if value < 0:
# #     raise ValueError("Negative values are not allowed!")


# for i in "hello world":
#     if i == 'a':
#         print("Буква существует")
#     else:
#         print("Буква 'а' в строке нету")
#         break
    
# a ="Pythonist"
# print("Reverse is", a[::-1])

# n = 10
# result = 1 < n < 20
# print(result) 
# result = 1 > n <= 9
# print(result) 

# class Animal: 
#     CAT, DOG, COW, CAT = range(4)
# print(Animal.CAT)
# print(Animal.DOG) 
# print(Animal.COW)
# print(Animal.CAT) 


# def x(): 
#     return 1, 2, 3, 4
# a, b, c, d = x() 
# print(a, b, c, d)


# test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
# print(max(set(test), key=test.count))


# n = 2;
# a ="Python";
# print(a * n);

# from collections import Counter
# def is_anagram(str1, str2):
#  return Counter(str1) == Counter(str2)
# print(is_anagram('python', 'nythop'))
# print(is_anagram('python', 'cython')) 


# def first(msg):
#     print(msg)
# first("Hello")
# second = first
# second("Hello")
# # При работе данного кода обе функции, first и second, дают один и тот же результат. Это оттого, что имена first и second относятся к одному объекту.


# def inc(x):
#     return x + 1

# def dec(x):
#     return x - 1

# def operate(func, x):
#     result = func(x)
#     return result

# print(inc(3))
# print(dec(3))

# def is_called():
#     def is_returned():
#         print("Dev's Battle")
#     return is_returned

# new = is_called()


# new()
# # Здесь is_returned() — это вложенная функция, так как она определена внутри функции is_called(). И она возвращается каждый раз, как только мы вызываем is_called().


# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
# def ordinary():
#     print("I am ordinary")
    
    
# pretty = make_pretty(ordinary)
# pretty()

# # В данном примере функция make_pretty() является декоратором. Декорирование происходит вот на этом шаге: pretty = make_pretty(ordinary) Функция ordinary() теперь задекорирована и возвращаемая функция носит имя pretty().


# squares = []
# for i in range(10):
#         squares.append(i * i)

# print(squares)

# # Здесь мы создаем пустой список squares. Затем используем цикл for для перебора range(10). Наконец, умножаем каждое число отдельно и добавляем результат в конец списка.


# sentence = 'the rocket came back from mars'
# vowels = [i for i in sentence if i in 'aeiou']
# print(vowels)

# # В этом блоке кода условный оператор отфильтровывает в sentence любые символы, не являющиеся гласными.


# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# prices = [i if i > 0 else 0 for i in original_prices]
# print(prices)

# # Здесь наше выражение i содержит условный оператор, if i> 0 else 0. Это указывает Python выводить значение i, если число положительное, но менять i на 0, если число отрицательное.


# quote = "life, uh, finds a way"
# unique_vowels = {i for i in quote if i in 'aeiou'}
# print(unique_vowels)

# # В нашем примере set comprehension выводит все уникальные гласные, которые он нашел в quote

# squares = {i: i * i for i in range(8)}
# print(squares)

# matrix = [
# [0, 0, 0],
# [1, 1, 1],
# [2, 2, 2],
#         ]
# flat = [num for row in matrix for num in row]
# print(flat)


# class Foo(object):
#     bar = True

# Foo = type('Foo', (), {'bar':True})
# print(Foo.bar)


# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self, item):
#         self.stack.append(item)
            
#     def pop(self):
#         if len(self.stack) == 0:
#             return None
#         removed = self.stack.pop()
#         return removed
    
    
# s = Stack()
# print(s.push(10))
# print(s.pop())


# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.max = None
            
#     def pop(self):
#         if len(self.stack) == 0:
#             return None
#         removed = self.stack.pop()
#         if len(self.stack) == 0:
#             self.max = None
#         elif removed == self.max:
#             self.max = self.stack[0]
#             for value in self.stack:
#                 if value > self.max:
#                     self.max = value
#         return removed
    
#     def push(self, item):
#         self.stack.append(item)
#         if len(self.stack) == 1 or item > self.max:
#             self.max = item
            
#     def get_max(self):
#         return self.max

    
    
# s = Stack()
# print(s.push(1))
# print(s.push(10))
# print(s.max)
# print(s.pop())
# print(s.max)


# class MyClass:
#     def method(self):
#         return 'instance method called', self
#     @classmethod
#     def classmethod(cls):
#         return 'class method called', cls
#     @staticmethod
#     def staticmethod():
#         return 'static method called'
    
    
# obj = MyClass()
# print(obj.staticmethod())


# num1 =10
# num2=20        
# def mathOP():
#     return num1 + num2
#     return num1 - num2
#     return num1 * num2
#     return num1 / num2
# print(mathOP())
# # функция возвращает только первое значение, после чего программа завершается.


# num1 =10
# num2=20   
# def mathOP():
#     yield num1 + num2
#     yield num1 - num2
#     yield num1 * num2
#     yield num1 / num2

# for i in mathOP():
#     print(i)
    
    
myList=[10,20,25,30,35,40,50]
def mod(myList):
    for i in myList:
        if(i % 10 == 0):
            return i
print(mod(myList))
# Создадаем список чисел и передадим его в функцию mod() в качестве аргумента. Далее, внутри функции, мы проверяем каждый элемент списка. Если он делится без остатка на 10, то мы его выводим.Оператор return возвращает только первое число, кратное 10, и завершает выполнение функции.

myList=[10,20,25,30,35,40,50]
def mod(myList):
    for i in myList:
        if(i % 10 == 0):
            yield i
for i in mod(myList):
    print(i)
    
# yield создает объект-генератор и возвращаеть несколько значений, не прерывая выполнение программы.