# 1)
words_lists = ['Ходячие мертвецы', 'Красавцы', 'Клан сопрано', 'Дневник вампира']

for words_list in words_lists:
    print(words_list)
    
# 2)
for i in range(25, 51):
    print(i)
    
# 3)
numbers = [1, 2, 3]
words = ['a', 'b', 'c']
for i in numbers:
    for j in words:
        print(i, j)
        
        
for i in 'a', 'b', 'c':
    for j in 1, 2, 3:
        print(i, j)
        
shows = ["Ходячие мертвецы", "Красавцы", "Клан Сопрано", "Дневники вампира"]
for index, show in enumerate(shows):
    print(index)
    print(show)
    
# 4)
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(i * j)

print(list3)