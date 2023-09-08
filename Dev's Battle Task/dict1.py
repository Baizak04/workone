dict = {True: 'one', 1: 'two', 1.0: 'three'}
print(dict)

dict_one = {'One': 1, 'Two': 2}
dict_two = {val: k for k, val in dict_one.items()}
print(dict_two)

dict_one = {'One': 1, 'Two': 2}
dict_two = {'Two': 2, 'One': 1}
print(dict_one == dict_two)

dct = {'one': 1, 'two': 2, 'three': 3}
while dct:
    print(dct.popitem(), end = '<->')
print('готово')