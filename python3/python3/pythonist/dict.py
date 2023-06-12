d = {}
for i in range(5):
    d[i] = i**2
print(d)

# 2)
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
new_dic = {i: j * 2 for i, j in dic.items()}
print(new_dic)

# 3)
a = list(enumerate(['a', 'd', 'c']))
print(a)

# 4)
