# Игра ним

from random import randint

n = int(input('Введите количество камней в куче? -- '))
count = 1
while n > 0:
    print('---------------------')
    count = count + 1
    if count % 2 == 0:
        computer = randint(1, 3)
        print(f'Компьютер взял {computer} камней')
        n = n - computer
        print(f'Количество камней осталось {n}')
        if n <= 0:
            print('Компьютер победил!')
        else:
            player = int(input('Введите количесто камней (от 1 до 3): '))
            while player < 1 or player > 3:
                print('Вы ошиблись!')
                player = int(input('Введите количесто камней (от 1 до 3): '))
            n = n - player
            print(f'Количество камней осталось {n}')
            if n <= 0:
                print('Вы победили!')