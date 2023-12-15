names_user_devs_battle = ['Leoonid', 'Arkadiy', 'Alex', 'Dmitry', 'Baizak', 'Alex', 'Yuri']

lengths = []
for name in names_user_devs_battle:
    lengths.append(len(name))
print(lengths)

# # 2)
list_num = [10, 20, 33, 1]
sum = 0
for i in list_num:
    sum += 1

print("Sum = ", sum)

# # 3)
list_num = [10, 20, 33, 1]
sum = 0
for i in list_num:
    sum += 1

print("Average = ", sum/len(list_num))


# # 4)

n = 2
for i in range(1, 3):
    n = 0
    mul = n * i
    print(n, "*",  i, "=", mul)
    
    
# # 5)
list_one = ["C#", "Python", "Go"]
for i in range(len(list_one)):
    print("Hello", list_one[i])
    
# # 6)
for i in range(5):
    if (i == 3):
        continue
    print(i)
    
# 7)
d = [1, 2, 3, 4, 6]
sum = 0
for x in d:
    s = x * x
    sum += s
print(sum)