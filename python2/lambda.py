def sq(num):
    return num * 2

my_nums = [1,2,3,4]
a = map(sq, my_nums)
print(a)


def sq(num):
    return num * 2

my_nums = [1,2,3,4]
a = list(map(sq, my_nums))
print(a)


def sr(num):
    result = num ** 2
    return result

a = sr(3)
print(a)

sh = lambda num: num ** 2
a = sh(3)
print(a)

a = list(map(lambda num:num**2, my_nums))
print(a)