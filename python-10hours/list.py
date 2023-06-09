# 1) Списки изменение значениие
posts_ids = [123, 1212, 12, 125]

posts_ids[0] = 111
print(posts_ids)

# 2) Удаление элементов
user_inputs = [True, 'hi', 10.3, 10]
print(len(user_inputs))

del user_inputs[1]
print(user_inputs)
print(len(user_inputs))

# 3 

ny_nums = [10, 2, 3, 5, 0, 100]
print(len(ny_nums))
print(type(ny_nums))
res = ny_nums.count(1)
print(res)
ny_nums.append(34)
print(ny_nums)
ny_nums.clear()
print(ny_nums)
ny_nums.extend('asd')
print(ny_nums)