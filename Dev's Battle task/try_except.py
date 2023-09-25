try:
    raise IndexError
except IndexError:
    print('Получено искличение')
else:
    print('Но в этом нет ничего страшного')