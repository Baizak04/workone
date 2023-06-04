# Бинарный поиск

array = [2, 5, 7, 9, 10, 11, 15, 18, 19, 20, 25, 30, 34, 42, 47, 52, 56, 69]
left = 0
right = len(array) - 1
middle = (left + right) // 2
while left <= right:
    middle = (left + right) // 2
    answer = input(f'Это число больше {array[middle]}? -- ')
    if answer.lower() == 'да':
        left = middle + 1
    elif answer.lower() == 'нет':
        right = middle - 1
    else:
        print('Вы ответили неверно. Укажите "да" или "нет"')
print(array[middle])
