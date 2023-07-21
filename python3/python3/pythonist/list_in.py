name_list = ['Adam', 'Dean', 'Harvey', 'John']

if 'John' in name_list:
    print("В списке John есть")
else:
    print("John Здес нету")

# 2)
name_list_two = ['Adam', 'Mick', 'Harvey']
for name in name_list_two:
    if name == 'Adam':
        print('Найден элемент')
        
# 3)
book_sheif_genres = ['Fict', 'Math', 'Coding', 'Math', 'Cooking']
print(book_sheif_genres.index('Math'))