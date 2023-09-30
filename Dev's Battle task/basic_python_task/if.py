f = None
if f is not None and len(f) > 0:
    print('1')
else:
    print('0')
    
password = 'testqwerty12345'

if password.isalnum():
    print(1)
else:
    print(2)


code_language = 'Python'
print(f'{code_language} is first language')

print(sorted)

if __debug__:
    print('yes')
else:
    print('no')
    
*c, last = [1, 2, 3]
print(*c)

x = True
c = 0
while x:
    c += 1
    if c == 10:
        x = False
    print(c)
    
    
temp = 10

if temp > 10:
    print('Холодно')
elif 10 <= temp < 28:
    if 10 <= temp < 15:
        print('Холодно но нормально')  
    else:
        print('Очень хорошо, но нормально')
else:
    print('Очень жарко')
        
        
is_male = True
is_tall = False

if is_male and is_tall:
    print('Вы высокий мужчина')
elif is_male and not(is_tall):
    print('Вы невысокий мужчина')
elif not(is_male) and is_tall:
    print('Вы не являетесь мужчиной, но имеете высокий рост')
else:
    print('Вы либо не мужчина, либо не высокого роста, либо и то и другое вместе')
    
a = 10
b = 25
c = 17

if a < b and c < b:
    print(b)
elif a < c and c < a:
    print(a)
elif a < c and b < c:
    print(c)
    

a = 10
b = 25
c = 17
max = a
if b > max:
    max = b
    if c > max:
        max = c
print(max)

a = 10
b = -25
c = -17
max = a
if b > max:
    max = b
    if c > max:
        max = c
print(max)

for i in 'hello world':
    if i == a:
        print('Буква существует')
    else:
        print('Буква а в строке нету')
        break
    
    
a = {True: '1', 1: False}

if a[1] == False:
    print(True)
else:
    print(False)
    
if (type(6.0)) is float \
    and 6 == 6.0:
        print(False)
else:
    print(True)
    
a = None
if a is not None and len(a) > 0:
    print(True)
else:
    print(False)
    
    

x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('пройдено')
else:
    print('не пройдено')
    
    
x, y, z = 0, 1, 0
if 2 in (x, y, z):
    print('пройдено')
else:
    print('не пройдено')


x, y, z = 10, 1, 2
if x or y or z:
    print('пройдено')
else:
    print('не пройдено')


x, y, z = 10, 1, 2
if any((x, y, z)):
    print('пройдено')
else:
    print('не пройдено')
    
a = 345
b = 14

if a % b == 0:
    print("Yes")
else:
    print('No, the remainder is', a % b)
    
    
x = -34
y = -10

if x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x > 0 and y < 0:
    print('III')
elif x == 0 and y == 0:
    print('IV')
elif x == 0:
    print('X')
elif y == 0:
    print('Y')
    
    
year = 2023
if year % 4 != 0:
    print('usual year')
elif year % 100 == 0:
    if year % 400 == 0:
        print("leap year")
    else:
        print('usual "year"')
    
else:
    print('leap "year"')