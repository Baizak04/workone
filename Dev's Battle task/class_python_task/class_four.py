# class A:
#     def __init__(self):
#         self.i = 0
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.i > 2:
#             raise StopIteration
#         self.i += 1
#         return self.i
    
    
# a, b, c = A()
# print(a, b, c)


# class User:
#     def __init__(self, name):
#         self.name = name
        
        
# a = (1, User('foo'))
# b = (2, User('bar'))
# c = (1, User('new'))
# print(a < b, b < c)


# from operator import attrgetter


# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __getattr__(self, attr):
#         return 1
    
    
# a = A(2, 3)
# vals = attrgetter('x', 'y', 'z')(a)
# print(sum(vals))


# class A:
#     count = 0 
    
#     def __init__(self):
#         self.__class__.count += 1
        
# class B(A):
#     pass

# class C(A):
#     pass


# x, y, z = B(), A(), C()
# print(A.count, B.count, C.count)


# class A:
#     count = 0
    
#     @classmethod
#     def inc(cls):
#         cls.count += 1
    
#     def __init__(self):
#         self.inc()
        
# class B(A):
#     count = 0
    
#     def __init__(self):
#         A.__init__(self)
        
# class C(A):
#     count = 0
    
    
# x = A()
# y1, y2 = B(), B()
# z1, z2, z3 = C(), C(), C()
# print(x.count, y1.count, z1.count)


# class A:
#     pass

# class B:
#     def __init__(self):
#         x = super()
#         print(x is A, x is B)
        
        
# b = B()


# class Foo:
#     def __init__(self):
#         self.__execute()
        
#     def execute(self):
#         print(1)
        
#     __execute = execute
    
# class Bar(Foo):
#     def execute(self):
#         print(2)
        
        
# Bar()


# class Dog:
#     def walk(self):
#         return "Walking"
    
#     def bark(self):
#         return "Auf"
    
# class Pitbull(Dog):
#     def bark(self):
#         return "Arff"
    
    
# ballon = Pitbull()
# print(ballon.walk())



# class Count:
#     def __init__(self, count=0):
#         self.__count = count
        
        
# fobj = Count(2)
# sobj = Count(2)
# print(id(fobj) == id(sobj))


# class MyExc(Exception):
#     def __str__(self):
#         return 'my-exc'
# try:
#     raise MyExc()
#     print('try')
# except MyExc as err:
#     print(err)
# else:
#     print('else')


class MyExc(Exception):
    pass
def f():
    raise MyExc()
    return 'f'
try:
    print(f())
    print('try')
except MyExc:
    print('exc')
    
    
class Counter:
    def __init__(self, func):
        self.calls = 0
        self.func = func
        
    def __call__(self, *args):
        self.calls += 1
        return self.func(*args), self.calls

@Counter
def square(a):
    return a ** 2


print(square(2)[0] + square(3)[0] + square(4)[1])