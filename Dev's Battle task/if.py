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