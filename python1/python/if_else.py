# if - если

# if условие:
    # действия
    
# a = True

# if a:
#     print('OK')

i = 10

if i == 10:
    print(i)
else:
    print("i не равно 10")
    


if 4 * 4 == 16:
    print('Туура')
else:
    print('Туура эмес')
    



password = '123'
user_input = '000000'

if user_input == password:
    print('Добро пожаловать')
else:
    print('Пароль не правильно')
    
    
    
sum = '12345678'

if len(sum) == 6:
    print('длина 8')
elif len(sum) == 6:
    print('Длина 6')
else: 
    print('что-то')
    
    
# if lesson-1

age = int(input("Ваш возраст?: "))
if age < 18:
    print("Ты еще мал! ")
elif age >= 18:
    print("Отлично!")
elif age == 18:
    print("Супер!")