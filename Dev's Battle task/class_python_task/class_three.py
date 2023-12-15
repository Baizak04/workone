# from collections.abc import Iterator


# class MyList(list):
#     def __getitem__(self, index):
#         return super().__getitem__(index) * 2
    
    
# m = MyList([1, 2])
# print([m[i] + x for i, x in enumerate(m)])


# class D:
#     __slots__ = ['a', 'b']
    
    
# d = D()
# d.a = 1
# f = lambda attr: getattr(d, attr, '*')
# print(f('a'), f('b'), f('__dict__'))


# class D:
#     __slots__ = ['a', '__dict__']
#     def __init__(self):
#         self.b = 2
    
    
# d = D()
# d.a = 1
# d.c = 3
# print(sorted(d.__dict__.values()))


# class MyList(list):
#     def __iter__(self):
#         return iter(self * 2)
    
    
# m = MyList([1, 2, 3])
# print(list(m))


# class X:
#     def __init__(self, arr):
#         self._arr = arr
        
#     def __iter__(self):
#         return reversed(self._arr)
    

# x = X([1, 2, 3])
# for i in x:
#     print(i, end=" ")
    
    
# from itertools import repeat, chain


# class A:
#     def __init__(self, x):
#         self.x = x
        
#     def __reversed__(self):
#         return chain(reversed(self.x), repeat(0, 2))
    
    
# a = A([1, 2])
# print(*reversed(a))


# from itertools import repeat, chain


# class X:
#     def __init__(self, l):
#         self.l = l
        
#     def __iter__(self):
#         return (x for x in self.l)
    
    
# a = X([1, 2])
# b = X([3, 4])
# print(*chain(a, a, b, b))


# class A:
#     def f(self):
#         print('A', end="")

# class B:
#     def f(self):
#         print('B', end="")
        
# class C(A):
#     def f(self):
#         print("C", end="")
#         super().f()
#         self.__class__.__bases__ = (B,)
        
        
# x = C()
# _ = x.f(), x.f()


class A:
    def f(self):
        print('A', end="")

class B(A):
    def f(self):
        print('B', end="")
        super().f()
        A.f(self)
        
class C(A):
    def f(self):
        print("C", end="")
        super().f()
        A.f(self)
        
class D(B, C):
    def f(self):
        print("D", end="")
        super().f()


d = D()
d.f()



# class A:
#     x = 1
#     l = []
    
    
# a1, a2 = A(), A()
# a1.x = 2
# a1.l.append(100)
# print(a2.x, len(a2.l))


# class C:
#     listing = []
    
    
# x = C()
# x.listing.append(1)
# x.listing.append(1)
# x.listing = 1
# print(x.listing, C.listing)