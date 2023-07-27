from itertools import groupby, chain


# 1)
for key, group in groupby('prrrrrooooooggggrrraaamingggg'):
    print(key, list(group))
    
# 2)
list_a = [1, 23]
list_b = [3, 23]
list_c = [60, 50]

for i in chain(list_a, list_b, list_c):
    print(i)
# chain() помогает нам объединять несколько итераторов в один