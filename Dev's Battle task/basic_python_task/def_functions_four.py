a = 1
def func(a):
    return a ** 2


a = func(a) ** 2
print(func(a))

print((9 / 3), (9.0 / 3), (9 // 3), (9 // 3.0))

print(eval('1 + 3 * 2'))

print(bool(0.0))

# x = 0 or 1
# y = 0 or 2
# z = x or y

# print(sum(x, y, z))

def gen():
    for i in range(3):
        yield i
        
for item in gen():
    print(item, end=" ")
    

# def unpack(a, b, c, d):
#     print(a + d)
    
    
# list_one = [1, 4, 7, 10]
# unpack(list_one)

def is_anogram(s1, s2):
    return set(s1) == set(s2)

print(is_anogram('elvis', 'lives'))


def my_len(object):
    total = 0
    for i in object:
        total += 1
    return total


word = "Dev's Battle"
print(my_len(word))


def summator(a: int, b: int, /, *, mod: int) -> int:
    return (a + b) % mod

s = summator(1, 12, mod=5)
print(s)

def display(**kwargs):
    for item in kwargs:
        print(item, end=" ")
        
        
display(lang="Python", ver=3.12)

# def foo(a=[]):
#     print(a)

# foo.__defaults__[0] = 1
# print(foo())


def foo():
    x = 1
    return x

foo.x = 4

print(foo(), foo.x)

def func(a: int, b: int) -> int:
    return a + b


print(func(1.0, 2.5))

# def func(*args):
#     args.append(3)
#     print(*args)
    
    
# func(1, 2)

def foo(*args: tuple[str]):
    pass


foo('1', '2', '3')

def foo(): pass

print(foo())

# def outer(func):
#     def inner(arg):
#         print(f'data is - {arg}')
#         inner(arg)
#     return inner

# @outer
# def get(arg):
#     return arg

# get(6)

def foo():
    return total + 1

total = 0
print(foo())

def cube(num):
    return num*num**num

print(cube(3))

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3, 20, 5))

def sum(*args):
    s = 0
    for i in args:
        s += i
    print('sum is', s)
    
sum(1, 4, 7)

def fibonacci(n):
    def step(a, b):
        return b, a + b
    a, b = 0, 1
    for i in range(n):
        a, b = step(a, b)
    return a
print(fibonacci(6))


def _f():
    yield 'key1', 10
    yield 'key2', 20
    
def f(): return dict(_f())

print(f())