i = 5
while i < 8:
    print(i)
    i = i + 1
    
# # 2)
i = 5
while i < 8:
    i = i + 1
    print(i)
    
# # 3) 
def f1(n):
    out = ''
    i = 0
    while i <= n:
        out += str(i) + '_'
        i += 3
    print(out)
    
    
f1(7)


# 4)
def f1(n):
    out = ''
    i = 0
    while i <= n:
        out += ' :)'
        i += 3
    print(out)
    
    
f1(7)