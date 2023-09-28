my_dict = {'Name': 'Kristina', 'age': 19, 'subjects': ['os', 'cn']}
my_dict.clear()
print(my_dict)

my_dict = {'Name': 'Kristina', 'age': 19, 'subjects': ['os', 'cn']}
print(len(my_dict))

my_dict = {
    'Name': 'Alex', 
    'age': 11, 
    'subjects': ['os', 'cn']}

for value in my_dict.values():
    print(value)
    
dict_one = {1: {1: {1: '1'}}}
print(dict_one.get(1).get(1))


dict_one = {
    'id': 1,
    'name': 'Bob'
}
dict_two = {
    'book': ['Python']
}
dict_three = {
    'city': 'Russia',
}

merged_dict = {**dict_one, **dict_two, **dict_three}
print(merged_dict)
