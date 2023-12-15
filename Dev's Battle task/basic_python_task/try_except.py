# try:
#     raise IndexError
# except IndexError:
#     print('Получено искличение')
# else:
#     print('Но в этом нет ничего страшного')
    
# # books = ['Cracking the Coding Interview', 'Clean code', 'The Pragmatic Programmer']
# # try:
# #     ind = books.index('Design Patterns')
# # except ValueError:
# #     ind = -1
# # print(ind)

# # try:
# #     a = 11 > 0 is True
# #     if answer:
# #         print(answer)
# #     else:
# #         print(True)
# # except:
# #     print(1)
    

# try:
#     print(1)
# except Exception:
#     print(0)
    
# try:
#     a = 2 + '1'
#     print(a)
# except TypeError:
#     print('Error')
    
# try:
#     b = 1 / 0
# except ZeroDivisionError:
#     b = 0

# print(b)

# # try:
# #     a = 1 + '1'
# # except ValueError:
# #     c = 0
    
# # print(c)

# try:
#     e = "{0}".format(1)
# except ValueError:
#     e = "Error"
    
# print(e)

# try:
# except Exception:
#     print(1)

# try:
#     k = 1 / 0
# except ArithmeticError:
#     k = 1
# else:
#     k = 0
    
# print(k)

# try:
#     a = 10 / 5
# except CustomError:
#     print(1)
# else:
#     print(0)

# try:
#     my_x = 1
#     raise Exception('исключение') #1
# except Exception as my_err:
#     print(my_err)                 #2
#     my_y = 2
# print(my_x)                       #3
# print(my_y)                       #4
# print(my_err)                     #5

# from random import random

# try:
#     a = random() - 0.5
#     a = a/0
#     print(a, end=" ")
# except:
#     print("err", end=" ")
# finally:
#     print(a/a)


def f(x):
    try:
        print('1', end=" ")
        y = 1 * 0 if x % 2 else 1 / 0
    except:
        y = 0
        print('2', end=" ")
    else:
        print('3', end=" ")
    finally:
        print('4', end=" ")
    return y


print(f(1) + f(2))

s = 'Hello, Max!'.isalnum()
try:
    10/s
except:
    print('Buy, Max')
else:
    print('See you tomorrow')