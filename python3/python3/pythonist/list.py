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