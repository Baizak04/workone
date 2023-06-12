# 1)
if True > False <= False:
    print("True")
    
# 2)
x = y = 1
y = 2

if x:
    print(x)
    
# 3)
a, b = 1, 0
a = a ^ b
b = a ^ b
a = a ^ b
print(a)

# 4)
name = "alex"
surname = "smith"
print(f'hello, {0} {1}!'. format(surname, name))

# 5)
some_list = [0]
for number in range(10):
    if number % 2 != 0:
        some_list.append(number)
        
print(max(some_list) - min(some_list))

# 6)
# name_list = ['harsh', 'Pratic', 'Bob']
# pos = name_list.index("Pypi")
# print(pos * 3) # Error 

# 7)
name = "Alex"
print("alex" is f"{name.lower()} is Alex".split()[0])

# 8)
mylist = ['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[int(-1/2)])

# 9)
def test():
    try:
        return 1
    finally:
        return 2
    
result = test()
print(result)

# 10)
world = 'you are doing well'
print(world[2:999])

# 11)
for i in range(0):
    print(i)
    
# 12)
# dictionary = {
#   "data": "user",
#   "user": 7,
#   "7": "data"
# }

# print(dictionary[dictionary["user"]]) # KeyError

# 13)

name = "James Bond"
print(name[2::-1])

# 14)
tuple_one = (1, 'Jon', "3+j")
print(type(tuple_one[2:3]))

# 15) 
text_hello = "Hello world!"
text_hello.replace("o", "-")
print(text_hello)

# 16)
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a ,b)
    return a

result = outer_fun(5, 10)
print(result)

# 17)
sample_set = {"yellow", "orange", "black"}
sample_set.discard("blue")
print(sample_set)

# 18)
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var += 1
else:
    var += 1
print(var)

# 19)
for num in range(10, 14):
    for i in range(2, num):
        if num % i == 1:
            print(num)
            break
        
# 20)
for l in 'Jhon':
    if l == 'o':
        pass
    print(l, end=", ")