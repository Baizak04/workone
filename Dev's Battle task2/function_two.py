def add_one(num):
    
    if (num >= 7):
        return num + 1
    
    total = num + 1
    print(total)
    
    return add_one(total)


mynewtotal = add_one(4)
print(mynewtotal)


# 2)
def get_choice():
    player_choice = "rock"
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


choices = get_choice()
print(choices)