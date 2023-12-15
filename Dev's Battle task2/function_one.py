def foo():
    return 11, 22, 3


a, b, c = foo()
print(a)

# 2)
def foo():
    return {'Radio', 'TV', 'Phone'}

a = foo()
print(a)

# 3)
def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False
    

result = is_odd(32)
print(result)

# 4)
def sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + sum(lst[1:])


result = sum([32, 34, 44])
print(result)


# 5)
def greeting():
    return "Hi"


response = greeting()
print(response)