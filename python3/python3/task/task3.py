import re


# 1)
def f1():
    x = 15
    print(x)
      
      
x =12
f1()

# 2)
# i = 1
# while True:
#     if i%2 == 0:
#         break
    
#     print(i)
    
#     i += 2
    
    
# 3)
def foo(k):
    k = [1]
    
    
q = [0]
foo(q)
print(q)

# 4)
def f1():
    x = 100
    print(x)
    
    
    
x = +1
f1()

# 5)
i = 2
while True:
    if i%3 == 0:
        break
    print(i)
    i += 2
    
# 6)
d = {"john":40, "peter":45}
print(list(d.keys()))                                       

# 7)
def foo(x):
    x[0] = ['def']
    x[1] = ['abc']
    return id(x)


q = ['abc', 'def']
print(id(q) == foo(q))

# 8)
def san(x):
        print(x + 1)
        
        
x = -2
x = 4
san(12) 

# 9)
def f1():
    global x
    x += 1
    print(x)
    
    
x = 12 
print("x")

# 10)
x = "abcdef"
i = "i"
while i in x:
    print(i, end="")
         
# 11)
sentence = 'we are humans'
matched = re.match(r'(.*)(.*?)(.*)', sentence)
print(matched.groups())

# 12)
a = {1: "A", 2:"B", 3:"C"}
for i, j in a.items():
    print(i, j, end="")
    
# 13)
def foo(i, x=[]):
    x.append(x.append(i))    
    return x 


for i in range(3):
    y = foo(i)
print(y)

# 14)
x = 10
def f1():
    global x
    x += 1
    print(x)
    
    
f1()
print("hello")    