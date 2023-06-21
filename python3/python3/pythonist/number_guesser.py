import random


top_of_range = input("Введите число: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Пожалуйста, в следующий раз введите число больше 0")
        quit()
else:
    print("Пожалуйста, в следующий раз введите число. ")
    quit()
    
random_number = random.randrange(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Сделать предположение")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Пожалуйста, в следующий раз введите число. ")
        continue
    
    if user_guess == random_number:
        print("Вы поняли!")
        break
    elif user_guess > random_number:
        print("Ты был выше числа!") 
    else:
        print("Вы были ниже числа!")       
print("Вы", guesses, "угадали")