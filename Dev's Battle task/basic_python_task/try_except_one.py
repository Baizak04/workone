# x = None
# arr = [1, 2, 3]
# try:
#     while True:
#         x = next(iter(arr))
# except StopIteration:
#     pass
# print(x)


# a, b = 1, 0
# def divide1(a, b):
# #     try:
# #         return a / b
# #     except ZeroDivisionError:
# #         return None

# # def divide2(a, b):
# #     try:
# #         return True, a / b
# #     except ZeroDivisionError:
# #         return False, None
    
    
# # print(divide1(a, b), *divide2(a, b))


# values = ['1', '-3', 'N/A']
# def f(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
    
    
# vals = list(filter(f, values))
# print(vals)


# def a(z):
#     x = 0
#     try:
#         x += 1
#         100/z
#         x += 1
#     except ZeroDivisionError:
#         try:
#             x += 1
#         finally:
#             x += 1
#             return 10 * x
#     finally:
#         x += 1
#         return 100 * x
    
    
# b = a(0)
# print(b)


# try:
#     try:
#         raise IndexError
#     except:
#         pass
#     finally:
#         print('1', end="")
# finally:
#     print('2')
    
    
# def f1():
#     raise IndexError
# def f2():
#     return
# def f3():
#     raise SyntaxError

# counters = []
# for func in (f1, f2, f3):
#     counter = 0
#     try:
#         try:
#             func()
#         except IndexError:
#             counter += 1
#         except SyntaxError:
#             counter += 1
#     finally:
#         counter += 1
#     counters.append(counter)

# print(counters)


# x = 1
# try:
#     1/0
# except Exception as x:
#     print(x)
# print(x)


# try:
#     1/0
# except:
#     raise TypeError from None


# try:
#     raise IOError()
# except OSError as err:
#     print(isinstance(err, OSError), isinstance(err, IOError))
    
try:
    assert False, "assert"
    print('try')
except Exception as err:
    print(err)
else:
    print('else')


# def func():
#     try:
#         return "Yes"
#     finally:
#         return "No"
    
    
# print(func())