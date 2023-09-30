# # fvar = 6
# # lam = lambda svar : svar * fvar
# # print(lam(8))

# # fx = lambda y: bool(y % 5)
# # print(fx(10), fx(12))

# print((lambda *args: args[0]) ('a', 'qqq'))

# a = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
# print(a)

# f = (lambda x, y: x if x < y else y)
# z1 = f('b', 'a')
# z2 = f('a', 'b')
# print(z1 == z2)



# import sys
# lambda_one = lambda x: list(map(sys.stdout.write, x))
# t = lambda_one(['1', '2', '3'])

# a = ((lambda x: (lambda y: x ** y))(3))(2)
# print(a)

c = map(lambda x: x ** x, filter(lambda x: x % 2, (1, 2, 3, 4)))
print(*c)

a = lambda x: type(x)
g = a(a(a(a(a(a)))))
print(g)


x = 1
a = lambda y: x + y
x = 2
b = lambda y: x + y
print(a(3), b(3))


