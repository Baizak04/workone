# class A:
#     def __init__(self, x=0):
#         self.x = x
        
#     def f(self):
#         print(self.x)
        
        
# a = A(2020)
# f = a.f
# print(f.__self__ is a, end=" ")
# print(f.__func__ is f, end=" ")
# print(f.__func__ is a.f, end=" ")
# print(f.__func__ is A.f, end=" ")


# class A:
#     def __init__(self, x):
#         self.x = x
    
#     def __call__(self):
#         return self.x
    
# class B:
#     def __init__(self, x):
#         self.x = x
    
#     def method(self):
#         return self.x
    

# class C:
#     def __init__(self, x=3):
#         self.x = x
    
#     def __repr__(self):
#         return str(self.x)
    
    
# a = A(1)
# b = B(2)
# c = C(3)
# callables = [a, b.method, C]
# print([act() for act in callables])


# class A: pass
# class B: pass
# def f(cls, *args):
#     return cls(*args)


# a = f(A)
# b = f()


# from typing import Any


# class M:
#     def __str__(self):
#         return str(self.__dict__)
    
# class A:
#     def __init__(self):
#         self.x = 1
        
# class B(A, M):
#     def __init__(self):
#         super().__init__()
#         self.y = 2
        

# b = B()
# print(b)


# class A:
#     def __init__(self, x):
#         self.x = x
        
#     def __getattribute__(self, name):
#         if name == '__add__':
#             self.x *= 10
#         return object.__getattribute__(self, name)
    
#     def __add__(self, other):
#         return self.x + other.x
    
    
# a1 = A(2)
# a2 = A(3)
# print(a1 + a2, a1.__add__(a2))


# class A:
#     def __getitem__(self, i):
#         return i
    
    
# a = A()
# a.__getitem__ = lambda i: i**2

# print(a[4])


# class C: pass

# c = C()
# a = type(c) == c.__class__
# b = type(type(c)) is c.__class__.__class__
# print(a, b)


# class A:
#     attr = 1

# class B(A): 
#     pass

# class C(A): 
#     attr = 2

# class D(B, C):
#     pass


# x = D()
# print(x.attr)



# class A:
#     attr = 1

# class B(A): 
#     pass

# class C(B): 
#     pass

# class D(A):
#     attr = 2

# class E(C, D):
#     attr = C.attr


# x = E()
# print(x.attr)


