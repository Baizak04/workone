# f = None
# if f is not None and len(f) > 0:
#     print('1')
# else:
#     print('0')
    
# password = 'testqwerty12345'

# if password.isalnum():
#     print(1)
# else:
#     print(2)


# code_language = 'Python'
# print(f'{code_language} is first language')

# print(sorted)

# if __debug__:
#     print('yes')
# else:
#     print('no')
    
# *c, last = [1, 2, 3]
#! print(*c)

#? x = True
# c = 0
# while x:
#     c += 1
#     if c == 10:
#         x = False
#     print(c)
    
    
# temp = 10

# if temp > 10:
#     print('Холодно')
# elif 10 <= temp < 28:
#     if 10 <= temp < 15:
#         print('Холодно но нормально')  
#     else:
#         print('Очень хорошо, но нормально')
# else:
#     print('Очень жарко')
        
        
# is_male = True
# is_tall = False

# if is_male and is_tall:
#     print('Вы высокий мужчина')
# elif is_male and not(is_tall):
#     print('Вы невысокий мужчина')
# elif not(is_male) and is_tall:
#     print('Вы не являетесь мужчиной, но имеете высокий рост')
# else:
#     print('Вы либо не мужчина, либо не высокого роста, либо и то и другое вместе')
    
# a = 10
# b = 25
# c = 17

# if a < b and c < b:
#     print(b)
# elif a < c and c < a:
#     print(a)
# elif a < c and b < c:
#     print(c)
    

# a = 10
# b = 25
# c = 17
# max = a
# if b > max:
#     max = b
#     if c > max:
#         max = c
# print(max)

# a = 10
# b = -25
# c = -17
# max = a
# if b > max:
#     max = b
#     if c > max:
#         max = c
# print(max)


    
    
# a = {True: '1', 1: False}

# if a[1] == False:
#     print(True)
# else:
#     print(False)
    
# if (type(6.0)) is float \
#     and 6 == 6.0:
#         print(False)
# else:
#     print(True)
    
# a = None
# if a is not None and len(a) > 0:
#     print(True)
# else:
#     print(False)
    
    

# x, y, z = 0, 1, 0
# if x == 1 or y == 1 or z == 1:
#     print('пройдено')
# else:
#     print('не пройдено')
    
    
# x, y, z = 0, 1, 0
# if 2 in (x, y, z):
#     print('пройдено')
# else:
#     print('не пройдено')


# x, y, z = 10, 1, 2
# if x or y or z:
#     print('пройдено')
# else:
#     print('не пройдено')


# x, y, z = 10, 1, 2
# if any((x, y, z)):
#     print('пройдено')
# else:
#     print('не пройдено')
    
# a = 345
# b = 14

# if a % b == 0:
#     print("Yes")
# else:
#     print('No, the remainder is', a % b)
    
    
# x = -34
# y = -10

# if x > 0 and y > 0:
#     print('I')
# elif x < 0 and y > 0:
#     print('II')
# elif x < 0 and y < 0:
#     print('III')
# elif x > 0 and y < 0:
#     print('III')
# elif x == 0 and y == 0:
#     print('IV')
# elif x == 0:
#     print('X')
# elif y == 0:
#     print('Y')
    
    
# year = 2023
# if year % 4 != 0:
#     print('usual year')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print("leap year")
#     else:
#         print('usual "year"')
    
# else:
#     print('leap "year"')

# class RepeaterIterator():
#     def __init__(self, source):
#         self.source = source

#     def __next__(self):
#         return self.source.value

# class Repeater:
#     def __init__(self, value):
#         self.value = value
        
#     def __iter__(self):
#         return RepeaterIterator(self)
    

# repeater = Repeater("Hello")
# for i in repeater:
#     print(i)


class Repeater:
    def __init__(self,key):
        self.key=key

    def __iter__(self):
        for i in range(1):
            yield self.key


class RepeaterIterator:
    pass


repeater = Repeater("Hello")
for i in repeater:
    print(i) 
    
    
for val in [8, 3, 5]:
    res = "even" if val % 2 == 0 else "odd"
    print(val, res)    
    
    
    
from multipledispatch import dispatch

class Pasta:
    def __init__(self, width, height, classification):
        self.width, self.height = width, height
        self.classification = classification

    def classify(self):
        if self.width > 3 and self.height < 2:
            self.classification = "Linguine"
        elif self.width == self.height and self.width < 3:
            self.classification = "Spaghetti"
        elif self.width > 2 and self.height == 1:
            self.classification = "Fettuccine"
        else:
            self.classification = "Dough"

    @classmethod
    def make_dough(cls, pasta=False):
        if pasta:
            return Pasta(10, 10, "Dough")
        else:
            return Bread(10, 10, "Dough")

class Bread:
    def __init__(self, width, height, classification):
        self.width, self.height = width, height
        self.classification = classification

    @dispatch(Pasta)
    def roll_thinner(self, x):
        x.height -= 1
        x.width += 1
        x.classify()

    @dispatch(Pasta)
    def cut(self, x):
        x.width -= 1
        x.classify()

    @dispatch(Pasta)
    def fold(self, x):
        x.width += 1
        x.classify()

    @classmethod
    def make_dough(cls, pasta=False):
        if pasta:
            return Pasta(10, 10, "Dough")
        else:
            return Bread(10, 10, "Dough")

dough = Pasta.make_dough()
print(dough.classification)

    
