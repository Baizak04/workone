print(bool(0), end=" ")
print(bool(3.14159), end=" ")
print(bool(-3), end=" ")
print(bool(1.0), end=" ")

def func(arg):
    x = arg ** 2
    x *= 4
    
    
x = 0
func(5)

print(x)

def func(x):
    return x < 1


lst = [-4, -2, 0, 2, 4]
res = filter(func, lst)

print(list(res))

def outer_func(a, b):
    def inner_func(c, d):
        return c + d
    return inner_func(a, b)


res = outer_func(5, 10)
print(res)


def sample(*args):
    print(args)
    
    
sample('time', 1, True)


def sample(**kwargs):
    print(kwargs)
    
    
sample(a = 'time', b = 1)

def add_three(x):
    if x % 2 == 0:
        return True
    else:
        return False
    

three = [1, 2, 3, 4, 5, 6, 7, 8]
print([i for i in filter(add_three, three)])

def hum(itm = []):
    itm.append(1)
    return itm

for _ in range(2):
    hum()

print(hum())

# def multiply(arg_one, arg_two):
#     return arg_one * arg_two

# nums = 2, 2
# print(multiply(nums))


def most_frequent(list):
    return max(set(list), key = list.count)

numbers = [1, 2, 1, 2, 3, 2, 1, 4, 2]
result = most_frequent(numbers)
print(result)


def add_to_list(param):
    param += [10]
    

lst = [10, 20, 30, 40]
add_to_list(lst)

print(len(lst))


def func(var):
    var = var + '2 '
    var = var * 2
    return var


print(func('bound'))

def total(a, b, c):
    return a + b + c


list_one = [1, 2, 3]
print(total(*list_one))

def func(arg):
    arg = [1]
    
    
var = [0]
func(var)
print(var)

def func():
    try:
        return 1
    finally:
        return 2
    
    
var = func()
print(var)

var = 100
def func_one():
    global var
    x = 90

def func_two():
    global var
    var = 80

print(var)

def func():
    try:
        return True
    finally:
        return False
    
    
print(func())


def foo(fname, val):
    print(fname(val))
    
foo(max, [1, 2, 3])
foo(min, [1, 2, 3])