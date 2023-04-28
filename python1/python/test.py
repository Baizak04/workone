name = 'World'

s = 'hello {}'

result = s.format(name)
print(result)

name = 'Baizak'
number = 100

result = f'{name} - {number}'
print(result)


# задачка: Пользователь вводит 3 числа, выведите сначала больше из них, а затем меньше

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третое число: "))

if a > b:
    if a > c:
        print(a)
    else:
        print(b)
else:
    if b > c:
        print(b)
    else:
        print(c)
        
if a < b:
    if a < c:
        print(a)
    else:
        print(b)
else:
    if b < c:
        print(b)
    else:
        print(c)


while True:
    a = int(input('первое число: '))
    b = int(input('Знак: ')) 
    c = int(input('второе число: '))
    
    if c == '+':
        print('ответ: ', a + b)
    elif c == '-':
        print('ответ: ', a - b)
    elif c == '*':
        print('ответ: ', a * b)
    elif c == '/':
        print('ответ: ', a / b)
    else:
        print('Ошибка!')