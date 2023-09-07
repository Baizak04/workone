# dict1 = {'a': 1, 'b': 2}
# print(dict1.get('c'))
# print(dict1.get('c', 3))

# # 2) 
# dict = {'Яблоко': 40, 'Апельсин': 80, 'Бананы': 60}
# dict1 = sorted(dict, key=dict.get)
# print(dict1)

# 3)
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))
print(zipped)