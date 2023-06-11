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
        
# 6)
def outer(a_list):
    def inner(a_list):
        a_list.append(10)
        return a_list

    return a_list


print(outer([]))

# 7)
# a_dict = {}
# first_tuple = (1, 2)
# second_tuple = (3,[1, 2])
# a_dict[first_tuple] = 1
# a_dict [second_tuple] = 2
# print(a_dict)                     # Error

# 8)
# k = [print(i) for i in my_string if i
# not in "aeiou"]                    # Error

# 9)
print(r"\n hello")

# 10)
x = ['ab', 'cd']
for i in x:
    i.upper()
    
    print(x)
    
# 11)
a_list = [1,2,3]
print(a_list[1:8])

# 12)
example = "snow world"
print("%s" % example[4:7])

# 13)
a = {3,4,5}
a.update([1,2,3])
print(a)

# 14)
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)
    
# 15)
list1 = [1, 2, 3]
list1 = list1 * 2
print(list1)   