def name_function(name):
    print('Привет' + name)
    
name_function(' Кто-то')


def add(n1,n2):
    return n1 + n2

result = add(20, 30)
print(result)


def myfunc(*args):
    return sum(args) * 2

result = myfunc(30, 23, 34, 67, 30, 12, 23)
print(result)

def myfunc(*args):
    for i in args:
        print(i)

myfunc(30, 23, 34, 67, 30, 12, 23)


def myfunc_two(**kwargs):
    if 'fruit' in kwargs:
        print(f'My fruit of choice is {kwargs}')
    else:
        print('Я не нашол такой слово')
        
myfunc_two(fruit='apple')

lst = [1, 2, 3]

def name_one(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs:
        print(k, v)
        
name_one(1, 2, 3, 4, k = 12, z = 10)