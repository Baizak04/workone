# # def outer_func(x):
# #     y = 4
# #     return lambda z: x + y + z
# # for i in range(1):
# #     closure = outer_func(i)
# #     print(f'closure({i + 5}) = {closure(i + 5)}')
    
# # def f(x, y):
# #     return x ** y


# # print(f.__call__(3, 2) + f(2, 3))

# # def f(a: int = 2, b: int = 2) -> int:
# #     return a ** b


# # # print(f(3))

# # def function(a: int = 5, b: int = 3, c: int = 4) -> int:
# #     return a + b + c


# # print(function(2.5, b=2))


# def function(a: int = '1', b: int = '2', c: int = '3') -> int:
#     return a + b + c


# print(function())

# def sum_one(a: 1 = 2) -> 3:
#     return 4


# print(sum_one())

# def bool_one(a: int = float) -> bool:
#     return str

# print(bool_one())

# def int_one(a: int = 7):
#     return 2 + int(a)

# print(int_one(3.5))

# def sum_1(x: 1 = 1):
#     sum_1.__annotations__["x"] += x
#     return sum_1.__annotations__["x"]

# print(sum_1(), sum_1(), sum_1(10))


# def sum_two(x):
#     return x + 2
# a = list(map(sum_two, [1, 2, 3, 4])) == [sum_two(x) for x in [1, 2, 3, 4]]
# print(a)


# from functools import reduce


# def sum_three(acc, x):
#     acc[x] = x * 2
#     return acc

# result = reduce(sum_three, ['a', 3, (1, 2)], {})  # Правильный порядок аргументов
# print(result)


# def gen():
#     for i in range(1, 5):
#         x = yield i
#         if x:
#             yield x ** 2
            
# g = gen()
# v = g.send(g.send(next(g) + next(g)) + next(g))
# print(v)


# from heapq import heappush, heappop


# def f(iterable):
#     h = []
#     for value in iterable:
#         heappush(h, value)
#     return [heappop(h) for i in range(len(h))]

# print(f([3, 5, 1]))


a = [1, 5, 2, 1, 1, 5]

def func(items):
    s =set()
    for item in items:
        if item not in s:
            yield items
            s.add(item)
            
print(*func(a))

def func(): return 2, 1
b, a = func()
print(a, b)

def func(s='', l=[]):
    s += '1'
    l.append(1)
    return s, l


func()
s, l = func()
print(len(s), len(l))

from functools import partial


def spam(a, b):
    print(a, b)

s = partial(spam, b=1)
s(2)


values = [8, 3, 1]
group = {2, 7}

def func(values, group):
    count = 0
    def func_two(x):
        nonlocal count
        if x in group:
            count += 1
            return (0, x)
        return (1, x)
    values.sort(key=func_two)
    return count
count = func(values, group)
print(count)