from functools import partial, reduce
import sys
import random


def power(x, exponent):
    return x ** exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)


print(square(4))
print(cube(4))


# 2)
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)


# 3)
numbers_one =[1, 2, 3, 4, 5, 6]
even_numbers_one = list(filter(lambda x: x % 2 == 0, numbers_one))
print(even_numbers_one)

# 4)
def test():
    s = 0
    while True:
        x = yield s
        s += x
        

t = test()
next(t)
print(t.send(111))
print(t.send(123))
print(t.send(456))
print(t.send(789))
print(t.send(1000))

# 5)
a = [1,2,3,4,5]
for i in a:
 if i > 3:
  pass
 print(i)
 
# 6)
def add_three(x,y):
    return x + y
li = [1,2,3,5]
sum_reduce = reduce(add_three, li)
print(sum_reduce)

# 7)
item = [n*2 for n in range(10)]
print(item)

# 8)
item = {n: n*2 for n in range(10)}
print(item)

# 9)
def print_msg(msg):
    # объемлющая функция
    def printer():
        # вложенная функция
        print(msg)
    printer()
print_msg("Hello")

# 10)
def print_msg(msg):
    # объемлющая функция
    
    
    def printer():
        # вложенная функция
        print(msg)
    return printer  # возвращаем вложенную функцию


another = print_msg("Hello")
another()

# 11)
def make_multiplier_of(n):
    
    
    def multiplier(x):
        return x * n
    return multiplier


times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)
print(times3(9))
print(times5(3))
print(times5(times3(2)))

# 12)
randomList = ['a', 0, 2]
for entry in randomList:
    try:
        print("Запись", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "произошло.")
        print("Следующая запись.")
        print()
print("Взаимность", entry, "это", r)

# 13)
try:
    num = int(input("Введите число: "))
    assert num % 2 == 0
except:
    print("Число нечетное!")
else:
    reciprocal = 1/num
    print(reciprocal, "no")
    
# 14)
random.seed(4)
random_number_1 = random.randint(1, 10)
random_number_2 = random.randint(1, 10)
print(random_number_1, random_number_2) 

# 15)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)