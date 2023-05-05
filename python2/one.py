# one.py
print('hello')


def func():
    print('Функция func() в one.py')
    
print('Верхний уровен внутри one.py')

if __name__ == '__main__':
    print('one.py запускается напрямую')
else:
    print('one.py был импортирован')