# 1)
class Tester:
    
    def __init__(self, id):
        self.id = str(id)
        id = '224'
        
        
temp = Tester(12)
print(temp.id)
# id в этом случае будет атрибутом класса.

# 2)
def sum_o_t(sum):
    sum = [1]
    
    
sum = [2]
sum_o_t(sum)
print(sum)
# В функции создается новый объект списка и ссылка теряется. Это можно проверить, сравнив id sum до и после sum = [1].

# 3)
def sum_twitter():
    x = 100
    print(x)
    
    
x =+ 1
sum_twitter()

# 4)
i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2
# Следующее значения i - 6. Поскольку 6 делится на 3 без остатка, произойдет выход из цикла.

# 5)
name_age = {'John': 24, 'Peter': 30}
print(list(name_age.keys()))

# 6)
# def world():
#     x[0] = ['web']
#     x[1] = ['com']
#     return id(x)


# w = ['web', 'com']
# print(id(w) == world(w))

# 7)
def san(x):
    print(x + 1)
    
    
x = -2
x = 4
san(12)
# В функции san() передается значение 12. Оно инкрементируется на единицу и выводится. Поэтому в выводе 13

# 8)
# print([if i%2==0: i; else: i+1; for i in range(4)])

# 9)
# True = False
# while True:
#     print(True)
#     break

# 10)
print(chr(ord('b') + 1))

# 11)
def s1():
    global x
    x += 1
    print(x)
    
    
x = 12
print("x")
# Переменная x объявлена в функции как глобальная. Поэтому в выводе будет х. Если бы переменная была локальной в выводе было бы 13 х.