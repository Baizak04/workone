from math import sqrt
x = -100
a = x > 0 and sqrt(x)
print(a)



result = 2 + 3 * 4 ** 2 / 8 % 3 - 1
print(result)

a = 60
b = 13
c = a & b
print(c)

a = 2,3
print(a)

x = 10.0
y = (x < 100.0) and isinstance(x, float)
print(y)

a = 100
b = 200
print(a and b)

print(
    '$100 $200 $300'.count('$'),
    '$100 $200 $300'.count('$', 5, 10),
    '$100 $200 $300'.count('$', 5)
)


print(*[*zip([1], [3, 4])])