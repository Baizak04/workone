# 1)
# counter = 0
# def increment():
#     counter = counter + 1
    
# increment()
# print(counter)  #Error

# 2)
def function():
    try:
        print(1)
        raise ValueError()
    except ValueError: 
        print(2)
        return 0
    finally:
        print(3)
        
function()

# 3)
# a_dict = {(1,2): 100, (3,4):200}
# print([1, 2] in a_dict)  # Error

# 4)
a_set = {1,2,3}
a_dict= {3: '3', 4:'4'}

print(a_set - a_dict.keys())

# 5)
def outer():
    value = 100
    
    def inner():
        global value
        value = 10
        
    inner()
    print(value)
        
outer() 
        