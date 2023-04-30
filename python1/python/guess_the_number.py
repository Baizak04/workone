# Генератор случайных чисел
# Угадай число

import random

print("Игра угадай число")
print("Компьютер загадает число от 1 до 10.") 
print("Попробуйте угадать!")

answer = 1
score = 0 
i = 0

while answer:
    if answer == 0:
        break
    
    rand = random.randint(1, 10)
    answer = int(input("число загадано. попробуйте отгадать: "))
    if answer == rand:
        score = score + 1
        print("ты угадал! Молодец")
    else:
        print("Ты не угадал попробуй еще")
    i = i + 1
    
print("Всего отгадано чисел: ", score, "из", i)
print("Приходи еще ")