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

# 11)

a = 1j
print(bool(a))

print(type(1 / 2))

# 12)
def main():
    return 2

main.value = main() + 1
print(main.value, end=' ')
print(main())

# 13)
def func(lst=[]):
    lst.append(1)
    return lst

func()
func()
print(func())

# 14)
# foo = [3, 1, 2]
# foo = foo + 3
# print(foo)          #error

# 15)
print(print())        # None

# 16)
a_list = [1, '1', 0, None, False]
result = list(filter(None, a_list)) 
print(result)

# 17)
a_dict = {}
a_dict[1] = 'foo'
a_dict[True] = 'bar'
print(a_dict)

# 18)
var = 1,
var_2 = (1)
print(var, var_2)

# 19)
for v in range(3):
    print(v)
    if v == 3:
        break
else:
    print(10)
        