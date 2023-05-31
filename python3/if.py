# HICH_SCORE = 90
# try:
#     test1 = int(input("Введите оценку 1: "))
#     test2 = int(input("Введите оценку 2: "))
#     test3 = int(input("Введите оценку 3: "))

#     array = (test1 + test2 + test3) // 3
#     print('Средный бал состовляеть: ', array)
    
#     if array >= HICH_SCORE:
#         print(f'Поздравляем \n Ваш Средный балл!{array}')
# except:
#     print('ошибка')
    
# temperatura = 1
# if temperatura < 5:
#     print("сегодня погода холодновато \n включи обогревател!")
# else:
#     print("сегодня погода теплый")
    
# name1 = 'Mark'
# name2 = 'Mary'
# if name1 > name2:
#     print("есть в списке")
# else:
#     print("нету в списке")


try:   
    password = str(input("Введите пароль: "))

    if password == "Нурэл":
        print("Вход разрешен")
    else:
        print("Неправильный пароль")
except ValueError:
    print("Введите целое число")
    
    
MIN_SALARY = 3000.0
MIN_YEARS = 2

salary = float(input("Введите свой годовой доход: "))
years_in_job = int(input("Введите количество лет: " + 
                         "рабочего стажа: "))

if salary >= MIN_SALARY:
    if years_in_job >= MIN_YEARS:
        print('Ваша ссуда одобрена.')
    else:
        print(f'Вы должны отроботовать'
              f'не менее {MIN_YEARS}'
              f'лет чтобы получить одобрение')
        
else:
    print('Вы должны работат и зарабатывать')