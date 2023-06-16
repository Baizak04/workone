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
scones = {
    "Фрукты": 22,
    "Пустая": 14,
    "Корица": 4,
    "Сыр": 21
}
scones["Вишня"] = 10
print(scones)

# 5)
fruct = {
    'Картошка': 24,
    'Помидор': 34,
    'Капуста': 30
}

fruct['Баклажан'] = 12
print(fruct)