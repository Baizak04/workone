try:
    raise IndexError
except IndexError:
    print('Получено искличение')
else:
    print('Но в этом нет ничего страшного')
    
books = ['Cracking the Coding Interview', 'Clean code', 'The Pragmatic Programmer']
try:
    ind = books.index('Design Patterns')
except ValueError:
    ind = -1
print(ind)