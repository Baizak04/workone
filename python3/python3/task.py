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
