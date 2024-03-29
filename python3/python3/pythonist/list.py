myList = ["Bran",11,3.14,33,"Stark",22,33,11]
print(myList)

# 2)
myList = ["Bran",11,22,33,"Stark",22,33,11]
myList.remove(22)
print(myList)

# Метод remove() и метод pop() работают по-разному. Применяя remove(), в качестве аргумента мы указываем сам элемент, который нужно удалить. А при использовании pop() мы указываем индекс нужного элемента.

# 3)
myList = ["Bran", 11, 22, 33, "Stark", 22, 33, 11]
myList.pop(1)
print(myList)

# 4)
myList = ["Bran", 11, 22, 33, "Stark", 22, 33, 11]
del myList[2]
print(myList)
# del. С его помощью можно удалить несколько элементов из списка (указав диапазон индексов).

# 5)
my_list = [67, 2, 999, 1, 15]
my_list.sort()
print(my_list)

# 6)
names = ["Jessica", "Ben", "Carl", "Jackie", "Wendy"]
print("Несортированный: ", names)
names.sort(reverse=True)
print("Сортированый: ", names)

# 7)
list_2 = [1, 2, 3, 4]
list_1 = [5, 6, 7, 8]
list_1.append(list_2)
print(list_1)

# 8)
list_1 = [1,2,3,4,5]
list_1.append('Happy')
print(list_1)
list_1.extend("hello")
print(list_1)

class Tester:
    def __init__(self, id):
        self.id = str(id)
        id = '224'
        
        
temp = Tester(12)
print(temp.id)
    
# 9) 
names = ['Jiammy', 'Timmy', 'Kenny', 'Lenny']
print(names[2])
names.append('Dylan')
print(names)

# 10)
programming_languages = ['JavaScript', 'Java', 'C++']
programming_languages.insert(0, 'Python')
print(programming_languages)

# 11)
names = ['Jimmy', 'Timmy']
more_names = ['Kenny', 'Jenny']
names.append(more_names)
print(names)

# 12)
names = ['Jimmy', 'Timmy']
more_names = ['Kenny', 'Jenny']
names.extend(more_names)
print(names)

# 13)
names = ['Jimmy', 'Timmy', 'Kenny', 'Jenny']
names.extend('Dylan')
print(names)
