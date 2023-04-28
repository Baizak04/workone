# неизмениямый очень похож на список
# кортеж работает быстрее чем список[list]
# tuple = ()

cor1 = ("hello", "sorry", 1, 2, 2000)
cor2 = (1, 2, 2, 3, 4)

print(cor1)
print(cor2)



one = (5,)
print(one)


cor_one = ("салам", "name", 18, 2003)
cor_two = (12, 2, 23, 3)
a = input("Введите название объекта: ")
if a in cor_one:
    print("Нашел!")
else:
    print("Не нашел!")