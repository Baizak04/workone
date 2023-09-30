word1 = 'python'
word2 = 'colab'

counter = 0

if 'p' in word1.lower():
    counter += 1

if 'p' in word2.lower():
    counter += 1
    
print(counter)


my_list = [2, 1, 3]

for element in my_list:
    if element == 1:
        print('Это единичка')
    else:
        print('Это не единичка')