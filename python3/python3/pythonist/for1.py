# 1)
for i in range(-5, 5):
    print(i, end=' ')

# 2)
for letter in 'foo':
    print(letter)
else:
    print('Все буквы напечатаны')
    
s1 = {0, 1, 2, 3}
s2 = {4, 5, 3, 2}
print(s1 | s2)