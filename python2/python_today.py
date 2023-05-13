# from getpass import getpass
from math import *

# # 1)Скрыть пароль на Python
# username = input('Введите имя: ')
# password = getpass('Введите пароль: ')




# try:
#     x = int(input())
#     y = int(input())

#     if x > 0 and y > 0:
#         print(1)
#     else:
#         if x < 0 and y > 0:
#             print(2)
#         else:
#             if x < 0 and y <   0:
#                 print(3) 
#             else:
#                 if x > 0 and y < 0:
#                     print(4)
#                 else:
#                     print("НИКОГДА!")  
# except ValueError:
#     print('ошибка')
                
                
# def sum(a=2, b=2):
#     print(a + b)
    
# sum(2)

# start = 10
# end = 0
# step = -1
 
# for i in range(start, end, step):
#     print(i, end=' ')


# number = input()
# ansver = 0

# for i in number:
#     ansver += int(i)
    
# print(ansver)

AB = input("Длина первого катета: ")
AC = input("Длина второго катета: ")

AB = float(AB)
AC = float(AC)

BC = sqrt(AB ** 2 + AC ** 2)

S = (AB * AC) / 2

P = AB + AC + BC

print("Площадь треугольника ", S)
print("Периметр треугольника ", P)