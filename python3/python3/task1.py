# 1)
a = 4
b = 11
print(a | b)
print(a >> 2)

# 2)
l = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
print(sum(l, []))

# 3)
for j in 'hi! i am mister Robert':
    if j == 'h':
        print("Найдено")
        break
else: 
    print("Готово")
    
# 4)
nums = range(3)
a = 15
for j in nums[1:]:
    a *= j
    
print(a)

# 5)
x, y = 5, 8
def spam(x = 10, y = 6):
    return x + y

print(spam(x))

# 6)
text = "anytext"
print(text[:-1])

# 7)
s = {10, 20, 30}
t = {3, 4}
u = s.union(t)
print(u)

# 8)
y = [1, 2, 3]
x = y.copy()
print(y is x)

# 9)
x = {2, 3, 4}
y = {2, 3, 4}
z = x.issubset(y)
print(z)

# 10)
s = set('any')
s.add('data')
print(s)