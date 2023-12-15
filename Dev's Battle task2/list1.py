# 1)
a = [1, 2, 3, 4]
b = a.index(2)
c = a[1]
print(c + b)

# 2)
def f1():
    foo = [11, 22, 33]
    out = ''
    for  i in range(len(foo)):
        out += str(i) + '->' + str(foo[i])
    print(out)
    
    
f1()

# 3)
def f2():
    foo = [11, 22, 77]
    s = 0
    i = 0
    while i < len(foo):
        s += foo[i]
        i += 1
    print(s)
    
    
f2()

# 4)
def f3():
    foo = [1, 32, 33, 2, 31]
    max = foo[0]
    
    for item in foo:
        if (item > max):
            max = item
            
    print(max)
    

f3()

# 5)
pow_args = [(2, 3), (12, 4)]
bases, exponents = zip(*pow_args)
print(bases) 