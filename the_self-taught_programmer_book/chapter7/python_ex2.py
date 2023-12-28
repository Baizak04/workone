number_one = [1, 2, 3, 4, 5]
number_two = [6, 7, 8, 9, 10]
added = []
for i in number_one:
    for j in number_two:
        added = (i + j)
    
print(added)


number_one = [1, 2, 3, 4, 5]
number_two = [6, 7, 8, 9, 10]
added = []
for i in number_one:
    for j in number_two:
        added.append(i + j)
    
print(added)