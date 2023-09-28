# my_list = [1, 2, 3, 4, 5]
# new_set = {element*3 for element in my_list}
# print(new_set)

s = set('hello')
print(s)

my_set = {1, 2, 3, 4, 6, 8}
new_set = {str(element) for element in my_set}
print(new_set)