# two.py

import one

print('верхний уровен внутри two.py')

one.func()

if __name__== '__main__':
    print('two.py вызывается напрямую')
else:
    print('two.py был импортирован')