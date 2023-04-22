import sys


print(1 == 2)  #False
print(1 != 2)  #True
print(1 > 2)   #False
print(1 >= 2)  #True
print(1 < 2)   #False
print(1 <= 2)  #True


operation = input('''
1 - сложить
2 - вычесть
3 - умножить
4 - разделить
5 - возвести в степень
''')



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


res = None
if (operation == '1'):
    res = x1 + x2
elif operation == '2':
    res = x1 - x2
elif operation == '3':
    res = x1 * x2
elif operation == '4':
    res = x1 / x2
elif operation == '5':
    res = x1 ** x2
else:
    print('Ошибка: неправильная операция')
    sys.exit(1)
    
if (1 == 2 or 2 == 3) and (2 == 2):
    pass
 
if res is not None:
    print('res =', res)

    
    
    
    
def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("деление на ноль")
    except TypeError:
        print("невозможно выполнить деление, один из параметром не число")
    finally:
        print("мы делили " + str(a) + " на " + str(b))

div("a",0)


fruits = {'banana', 'orange', 'apple'} 
try:
    fruits.remove('orange')
except KeyError:
    print('такое имя не существует')