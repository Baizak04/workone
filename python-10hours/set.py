my_set = {10, 12, 5, 5, 5, 5, 35}
print(my_set)
print(len(my_set))

my_set = {(10, 10), 10, 4, 22}
print(my_set)

my_two_set = set()
print(my_two_set)
print(type(my_two_set))

# 2)

my_set = {'abs', 'd', 'f', 'y'}
other_set = {'f', 'd'}
print(my_set.intersection('absd'))
print(my_set.union(other_set))
print(other_set.issubset(my_set))
print(my_set.difference(other_set))
print(my_set & other_set)
print(my_set | other_set)