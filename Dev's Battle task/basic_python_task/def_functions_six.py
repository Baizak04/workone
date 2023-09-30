# def func():
#     yield 0
#     yield from [1, 2]
#     yield 3
    
# print(*func())

# def func():
#     x = 1
#     y = 1
#     def func_two():
# #         nonlocal x
# #         x, y = 2, 2
        
    
# #     func_two()
# #     print(x, y)

# # func()

# # x = 1
# # def func_one():
# #     return x
# # def func_two():
# #     global x
# #     x = 2
# #     return x
# # def func_three():
# #     global x
# #     return x


# # print(func_one(), func_two(), func_three(), func_one())


# # # def func():
# # #     def func_one():
# # #         nonlocal x
# # #         x = 2
        
# # #     func_one()
# # #     print(x)
       
# # # func()

# # def f():
# #     x = 1
# #     def g():
# #         x += 1
        
# #     g()
# #     print(x)
    
# # print(f())

# def func(a, b):
#     a = 2
#     b = b[:]
#     b[0] = 10
    
    
# a, b = [0], [1]
# func(a, b)
# print(a, b)


# def func(*args):
#     result = []
    
#     for x in args[0]:
#         if x in result:
#             continue
#         for word in args[1:]:
#             if x not in word:
#                 break
#         else:
#             result.append(x)
#     return ''.join(result)

# s1, s2, s3 = 'message', 'message', 'mask'
# print(func(s1, s2, s3))

# def func(x):
#     if x >= 3:
#         return x
# y = filter(func, (1, 2, 3, 4))
# print(list(y))


# def func(x):
#     if x < 3:
#         return x
# y = filter(func, (1, 2, 3, 4))
# print(list(y))

# def unpacking(x, y):
#     print(x, y, end=" ")
    
# tuple_vec = (1, 0)
# dict_vec = {'x': 1, 'y': 0}
# unpacking(*tuple_vec)
# unpacking(**dict_vec)

a = (lambda: lambda: lambda: lambda: lambda: 1)()()()()()
print(a)