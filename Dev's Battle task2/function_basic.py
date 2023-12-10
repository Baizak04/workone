# # 1) 
# # a = 4
# # b = 11
# # c = (a + b) % 11
# # print(c)

# # 2)
# def some_function():
#     a = 4
#     b = 11
#     c = (a + b) % 11
#     c = (a + b) % 11
#     print(c)
#     print(c)
    
# some_function()
# some_function()

# # 3)
# f = 66

# def ex1():
#     f = 55
#     print(f)
    

# ex1()

# # 4)
# k = 99

# def ex2():
#     global k
#     k = 88
#     print(k)
    
    
# ex2()
# print(k)

# # 5)
# def ex3(a, b):
#     c = (a + b) - 128
#     print(c)

# ex3(3, 4)
# ex3(122, 4)
# ex3(1111, 2222)

# 6)
def ex3(a, b):
    c = (a + b) - 128
    print(c)
    return c

m = 1000 + ex3(22, 23)
print(m)

# 7)
def t2():
    f = '<usb'
    
    if f == '<usb':
        print('yes')
        
    if len(f) == 4:
        print('yes')
    else:
        print('no')
        
    
t2()

# 8)

def t4():
    color = 2
    
    if color == 1:
        trafficLight = 'red'
    elif color == 2:
        trafficLight = 'yellow'
    else:
        trafficLight = 'green'
        
    print(trafficLight)
    
    
t4()


# 9)

def t5():
    user = 'Baizak'
    password = 'Sparta'
    
    if user == 'Baizak' and password == 'Sparta':
        print('welcome')
    else:
        print('wrong')
        
t5()