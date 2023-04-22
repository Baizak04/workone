import sys

# def div(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#         print("деление на ноль")
#     except TypeError:
#         print("невозможно выполнить деление, один из параметром не число")
#     finally:
#         print("мы делили " + str(a) + " на " + str(b))

# div("a",0)


x1 =input('Введите x1: ')
try:
    x1 = int(x1)
    print('Тип x1 =',type(x1))
except ValueError:
    print('Ошибка: введите число: ')
    sys.exit(1)

x2 =input('Введите x2: ')

try:
    x2 = int(x2)
    print('Тип x1 =', type(x2))
except ValueError:
    print('Ошибка: введите число: ')
    sys.exit(2)

print(x1, '**', '=', x1 ** x2)
    
