from functools import reduce


def add_three(x, y):
    return x + y


three = [1, 2, 3, 4, 5]
a = reduce(add_three, three)
print(a)

