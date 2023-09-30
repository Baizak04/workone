# target = [1, 2, 3, 4, 5, 6, 7]

# ind = 0

# while ind < len(target):
#     print(ind)
#     ind += 1
    

# target = [1, 2, 3, 4, 5, 6, 7]

# t = []

# while len(target):
#     el = target.pop(0)
#     if el % 2:
#         continue
#     t.append(el ** 2)
    
# print(t)

# x = 1

# while x <= 10:
#     print(x)
#     x += 1
# else:
#     print('Done')
    
# x = 1

# while x <= 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1
    
# a = 0
# n = 10
# while a != n:
#     b = a * a
#     a += 2
#     print(b)
    
a = 1

while a < 3:
    print('Условие верно')
    a += 1
else:
    print('Условие неверно')
    
n = 12334412
n = abs(n)

count = 1
n //= 10

while n > 0:
    n //= 10
    count += 1
    
print(count)

n = 6

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)


n = 5

f1 = f2 = 1
print(f1, f2, end=' ')

i = 2
while i < n:
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
    i += 1
    
n1 = 2023
n2 = 0

while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit
    
print(n2)



    
