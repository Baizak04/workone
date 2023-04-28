# # цикл - фрагмент кода, который выполняется многократно
# # цикл (for, while)
# # Итерирование - процесс перебора итерируемого объекта
# # for имя_переменной in имя итерируемого объекта:
# #     инструкции

# arr = [1, 2, 3, 4, 5]
# for i in arr:
#     print("Число {}".format(i))


# # children = ['arbuzov_1000', 'ivanov_2030', 'petrov_1255', 'Azat_2002']

# # names = []

# # for childrens in children:
# #     surname = childrens.split('_')[0]
# #     surname = surname.title()
# #     print(surname)
    
    
# # name = "Привет кто-то!"
# # for i in name:
# #     print(i)
# # # выводит по отдельному

# # name = "hello"
# # for i in range(1,11):
# #     print(name)
    
    
for j in 'hello world':
    print(j * 2, end = '')
    
    

# for j in 'hello world':
#     if j == 'w':
#         break
#     print(j * 4, end = '')
    
    
# for i in range(10):
#     print(i, end=" ")
    
    
# else - lesson

for i in 'hello world' :
    if i=='h':
        print(' буквы существует!')
        break
    else:
        print(' Буквы в строке нету')
        break