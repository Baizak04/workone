# # # 1) 
# # day_time = True
# # greet = 'hello' if day_time else 'goodbye'
# # print(greet)

# # # 2) 
# # day_time = False
# # print(f"Ну: {'hello' if day_time else 'goodbye'}")

# # # 3)
# # min_value = 5
# # max_value = 10
# # value = 7

# # if min_value < value and max_value > value:
# #     print("True")

# # 4)
# # test_dict = {'a': 1, 'b': 2, 'c': 3}
# # if test_dict.get('a'):
# #     print(test_dict.get('a'))
    
# # # 5)
# # names = []

# # if not names:
# #     print("Список пуст")
# # print(len(names))

# # # 6)
# # my_list = [1, 2, 3, 8, 6, 11, 14, 44]
# # chunk_size = 4
# # print([my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)])

# # # 7)
# # def square_generator(n):
# #     for i in range(3, n + 5):
# #         yield i ** 2
        
        
# # generator = square_generator(8)
# # print(next(generator))
# # print(next(generator))
# # print(next(generator))
# # print(next(generator))
# # print(next(generator))

# # 8)
numbers = [11, 22, 33, 44, 55, 20, 66, 77, 88, 99]
result = 0
for num in numbers:
    result += 5
    
print(result)

# # 9)
numbers = [11, 22, 33, 44, 55, 20, 66, 77, 88, 99]
result = 0
for num in numbers:
    result += num
    
print(result)

# # 10)
# numbers = [1, 2, 3, 4]
# letters = ['a', 'b', 'c']

# for value_one, value_two in zip(numbers, letters):
#     print(value_one, value_two)
    
# # 11)
# events = [('learn', 5), ('learn', 10), ('relaxed', 20)]
# minutes_studied = 0
# for event in events:
#         if event[0] == 'learn':
#             minutes_studied += event[1]
# print(minutes_studied)