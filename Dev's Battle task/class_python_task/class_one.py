# class A:
#     class_field = 10
    
#     def method(self, value):
#         self.obj_field = A.class_field + value
        
# a1 = A()
# a2 = A()

# a1.method(3)
# a2.method(100)

# print(a1.obj_field)
# print(a2.obj_field)



# class T1:
#     n = 10
    
#     def total(self, N):
#         print(int(self.n) + int(N))
        
        
# class T2:
#     def total(self, s):
#         print(len(str(s)))
        
        
# t1 = T1()
# t2 = T2()
# t1.total(45)
# t2.total(45)



# class B:
#     __count = 0
    
#     def __init__(self):
#         B.__count += 1
        
#     def __del__(self):
#         B.__count -= 1
        
#     @staticmethod
#     def qty_objects():
#         return B.__count
    
    
# a = B()
# b = B()
# c = B()
# print(b.qty_objects())
# del a 
# print(B.qty_objects())
# print(b.qty_objects())


# class A:
#     num = 0
    
#     def __init__(self):
#         self.num = 1
        
        
# print(A.num, A().num)


# class Foo:
#     a = 0
    
#     def __init__(self, value):
#         a = value
        
        
# print(Foo(1).a)


# class MyClass:
    
#     def __init__(self, value):
#         self.value = value
        
#     def print_value(self):
#         print(self.value)
        
    
# obj = MyClass(42)
# obj.print_value()


# class A:
#     __x = 1
    

# a = A()


# class A:
#     __x = 1
    
#     def f(self):
#         return "f from A"
    
#     def g(self):
#         return "g from A"
    

# # class B:
# #     __x = 2
    
# #     def f(self):
# #         return "f from B"
    
# #     def g(self):
# #         return "g from B"
    
    
# # class C(A, B):
# #     f = B.f


# # c = C()
# # print(c.f(), c.g(), c._A__x, c._B__x)        


# # class A:
# #     pass

# # class B(A):
# #     pass


# # a = A()
# # b = B()
# # print(isinstance(b, A), isinstance(a, B))


# class A:
#     x = 1
    
# class B(A):
#     pass

# class C(A):
#     pass

# A.x = 2
# B.x = 3

# print(B.x, C.x)


# def f():
#     import sys
#     locs = sys._getframe(1).f_locals
#     setattr(locs['self'], 'xy', 4 * locs['x'] + 7 * locs['y'])

# class A:
#     def __init__(self, x, y):
#         self.xy = 2 * x + 3 * y
#         f()

# a = A(2, 3)
# A.xy = 99
# print(a.xy)


# class B:
#     def __init__(self):
#         self.arr = []
    
#     def __getattr__(self, attrname):
#         return getattr(self.arr, attrname)
    
    
# b = B()
# b.append(1)
# b.append(2)
# b.append(3)
# b.pop()
# print(b.arr)


# class A:
#     def __repr__(self):
#         return "repr"
    
#     def __str__(self):
#         return "str"
    

# a = A()
# print(a, repr(a), str(a))


# class A:
#     def __init__(self, x):
#         self.x = x
        
#     def __and__(self, outer):
#         return self.x + outer.x
    
    
# a1 = A(1)
# a2 = A(2)
# print(a1 & a2)


# class A:
#     def __init__(self, value):
#         self.value = value
        
#     def __call__(self, other):
#         return self.value ** other
    
    
# x = A(2)
# print(x(3))


# class A:
#     def __init__(self, x):
#         self._x = x
#     @property
    
#     def x(self):
#         return self._x
    
    
# a = A(1)
# print(A.x.fget(a), a.x)


# class A:
#     x = 1
    
#     def __init__(self):
#         self.y = 2
        
# a = A()


class A:
    def __iter__(self):
        yield from range(10)
        

a = A()
print(5 in a, 20 in a)