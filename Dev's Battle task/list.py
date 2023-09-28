# # lst_one = list('bob')
# # lst_two = list('obo')
# # lst_three = list('bo')

# # print(lst_one + lst_two - 2 * lst_three)

# fruits = ['Bananas', 'Apples', 'Mangoes']
# len_fruits = len(fruits)
# print(len_fruits)


# l1 = [1, [20, 30, 40], 6]
# l2 = list(l1)
# l1.append(3)
# l1[1].remove(30)

# print(f"{l2 = }")


# mult_value = 2
# lst = [2, 5, 11, 9]

# iterator = map(lambda x: x * mult_value, lst)

# mult_value = 1
# lst = [1, 4, 10, 8]

# print(*list(iterator))

# width = 10
# precision = 2
# value = 12.111

# x = f"{value:.{precision}f}"

# print(x)

# a = [1, '2', 3]
# m = map(int, a)

# print(sorted(m) == sorted(m))

list_one = (1, 2, 3, 4)
print(list_one, end="*")

name_list = ['Adam', 'Dean', 'Harvey']
for name in name_list:
    if name == 'Adam':
        print('Найденный элемент')
        
my_list = [10, 20, 30, 40, 50]
my_list.reverse()
print(my_list)

x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('пройдено')
else:
    print('не пройдено')
    
    
x, y, z = 0, 1, 0
if 2 in (x, y, z):
    print('пройдено')
else:
    print('не пройдено')


x, y, z = 10, 1, 2
if x or y or z:
    print('пройдено')
else:
    print('не пройдено')


x, y, z = 10, 1, 2
if any((x, y, z)):
    print('пройдено')
else:
    print('не пройдено')