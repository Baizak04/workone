import random


user_wins = 0 
computer_wins = 0

options = ["камень", "ножница", "бумага"]

while True:
    user_input = input("Введите Камень/Ножница/Бумага или Q, чтобы выйти из игры: ").lower()
    if user_input == "q":
        break
        
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Выбранный компьютер", computer_pick + ".")
    
    if user_input == "камень" and computer_pick == "ножница":
        print("Вы выиграли!")
        user_wins += 1

    elif user_input == "Бумага" and computer_pick == "Камень":
        print("Вы выиграли!")
        user_wins += 1
    
    elif user_input == "Ножница" and computer_pick == "Бумага":
        print("Вы выиграли!")
        user_wins += 1

    else:
        print("Вы проиграли")
        computer_wins += 1
        
print("Вы выиграли", user_wins, "раз")
print("Компьютер выиграл", computer_wins, "раз")    
print("До свидания")