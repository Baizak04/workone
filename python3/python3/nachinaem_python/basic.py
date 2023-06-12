name = input('Введите свое имя: ')
first_name = input('Введите свое фамилию: ')
age = int(input('Сколько вам лет?: '))
income = float(input('Какой у вас доход?: '))
print('Вот данные которые Вы ввели: ')
print('Имя:', name)
print('Возраст:', age)
print('Фамилия:', first_name)
print('Доход:', income)


salary = 12000
bonus = 1000
pay = salary + bonus
print('Ваша заработная плата составляет', pay)


original_price = float(input("Введите исходную цену товара: "))
discount = original_price * 2.2
sala_price = original_price - discount
print('Отпускная цена составляет', sala_price)


a = input()
b = input()

print((a + b) * 5) 

sum = int(input('Введите 1-ое число: '))
sum_two = int(input('Введите 2-ое число: '))
print(f'{sum} + {sum_two} = {sum + sum_two}')