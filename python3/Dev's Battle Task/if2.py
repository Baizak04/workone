number = 43
if number % 3 == 0:
    print ("This number is divided by 3")
else:
    print ("This number is not divisible by 3")
    
number = 40
if number % 4 == 0:
    print ("This number is divided by 4")
else:
    print ("This number is not divisible by 4")
    
sample = 45
if sample % 3 == 0:
    print ("This number is divisible by 3")
elif sample % 4 == 0:
    print("This number is divisible by 4")
else:
    print ("This number is not divisible by 3 and 4")
    
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")
    
furry = True
large = True
if furry:
    if large:
        print("Это йети.")
    else:
        print("Это кошка!")
else:
    if large:
        print("Это кит!")
    else:
        print("Это человек. Или бесшерстная кошка.")
        
some_list = []
if some_list:
    print("Здесь что-то есть")
else:
    print("Эй, он пустой!")
    
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
    or letter == 'o' or letter == 'u':
    print(letter, 'гласный')
else:
    print(letter, 'не является гласным')
    
vowels = 'aeiou'
letter = 'i'
if letter in vowels:
    print(letter, 'гласный')