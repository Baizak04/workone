# 1)
a = '13'
b = '100'
print(a > b)

# 2)
print(all([]))

# 3)
x = 10_000
y = int('10_000')

print(x, y)

# 4)
class Foo:
    
    def __init__(self, x):
        self.x = x
        
    """Doc"""
    
    
print(Foo.__doc__)

# 5)
class Foo:
    """Doc"""
    
    
print(Foo.__doc__)

# 6)
print(type(1) is int)
print(type(1.0) is int)

# 7)
# x = complex('1 + 2j')
# print(x)

# 8)
# x = True
# y = False
# print(x == not y)

# 9)
class Foo:
    
    def __getattr__(self, name):
        return 0
    
    
print(Foo().x)

# 10)
class Foo:
    
    def __new__(cls, *args, **kwargs):
        print('__new__')
        
    def __init__(self):
        print('__init__')
        
        
foo = Foo()
        