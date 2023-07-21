dict_one = {
    'id': 1,
    'name': 'Ashutosh',
}
dict_two = {
    'books': ['python', 'DSA'],
    'coollege': 'NSFC',
}
dict_three = {
    'city': 'Kolkata',
    'country': 'India'
}

dict_one.update(dict_three)
print(dict_one)

merged_dict = dict_one | dict_two | dict_three
print(merged_dict)