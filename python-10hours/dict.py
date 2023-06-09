my_disk = {}
print(id(my_disk))
print(type(my_disk))

my_disk['brand'] = 10
my_disk['model'] = 'BMW'
print(my_disk)
print(id(my_disk))

# print(my_disk.__doc__)

print(my_disk.items())
print(my_disk.values())
print(list(my_disk.keys()))
print(my_disk.popitem())
print(my_disk.get('tyo'))     # если нет пары то будеть None
# print(my_disk['model'])         # если нет пары то будеть ошибка

