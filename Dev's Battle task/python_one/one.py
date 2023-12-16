# 1)
def reward_for_fruit(fruit: str) -> int:
    if fruit == 'banana':
        return 1
    elif fruit == 'apple':
        return 2
    elif fruit == 'orange':
        return 3
    else:
        raise ValueError("Несуществующий фрукт")
    
    
print(reward_for_fruit('banana'))


# 2)
dictFruits = dict({
    'banana': 1,
    'apple': 2,
    'orange': 3,
    'orange': 4
    })

def reward_for_fruit_dict(fruit: str) -> int:
    if fruit in dictFruits.keys():
        return dictFruits[fruit]
    else:
        raise ValueError("Несуществующий фрукт")
    
    
result = reward_for_fruit_dict('orange')
print(result)


# 3) 
from enum import Enum

class RewardEnum(Enum):
    banana = 1
    apple = 2
    orange = 3
    
def reward_for_fruit_enum(fruit: str) -> int:
    if fruit in RewardEnum.__members__:
        return RewardEnum[fruit].value
    else:
        raise ValueError("Несуществующий фрукт")


result = reward_for_fruit_enum('orange')
print(result)


# 4)
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap Year')
            else:
                print('Not leap year')
        else:
            print('Leap year')
    else:
        print('Not Leap Year')
        
        
is_leap_year(2023)


# 5)
user_profile = {
    'name': 'Baizak',
    'comments_gty': 20
}

def user_info(name: str, comments_gty=0):
    if not comments_gty:
        return f"{name} has no comments"
    
    return f"{name} has {comments_gty} comments"


result = user_info(**user_profile)
print(result)
    
# 6)
num_one = 10
num_two = 15

if (num_one > 0 and
    num_two > 0 and
    isinstance(num_one, int) and
        isinstance(num_one, int)):
    print("Yes")