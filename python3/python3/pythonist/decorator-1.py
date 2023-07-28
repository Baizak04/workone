# 1)
def decorator1(function):
    def wrapper():
        print('this is first message')
        function()
        print ('this is second message')
    return wrapper
def decorator2():
    print('this is 3rd message')
decorator2 = decorator1(decorator2)
decorator2()

# 2)
def decorator1(f):
    def wrapped():
        return '*****' + f() + '*****'
    return wrapped
    
def decorator2(f):
    def wrapped():
        return '+++' + f() + '+++'
    return wrapped
@decorator1
@decorator2
def function():
    return 'Python 3.8'
print(function())