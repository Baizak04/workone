# while выражение:
#     фрагмент кода


# while - пока
# counter = 0
# while True:
#     print(counter)
#     counter += 1       #counter = counter + 1
    
    
# sum = 0 
# while sum < 20:
#     print(sum)
#     sum += 1
    
    
# counter = 0
# while True:
#     print(counter)
#     if counter >= 20:
#         break
#     counter += 1 
    
    
i = 0 
while i < 20:
    i = i + 2
    print(i)
    
print("The end")


i = 1
while i <= 10:
    if i != 5:
        print(i)
    i = i + 1
    continue





n = int(input('Введите число: '))
i = 1
while i < n + 1:
    print('hello')
    i = i + 1


sum = int(input('Введите число: '))
while sum != 0:
    print('Повторите ввод')
    a = int(input('Введите число снова: '))
    
    
g = input()
password = 'asd'
count = 0 
while g != password:
    count += 1
    print('Неправильный ввод пароля')
    g = input()

print('Вы потратили', count, 'попыток')