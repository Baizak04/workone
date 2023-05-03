mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist:
    if num % 2 == 0:
        print(f'четное число: {num}')
    else:
        print(f'нечетное число: {num}')
    
    
for letter in 'Hello World':
    print(letter)
    
mylist = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for i in mylist:
    print(i)
    
d = {'k1': 1, 'k2': 2, 'k3': 3}
for i in d.items():
    print(i)