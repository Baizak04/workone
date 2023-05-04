try:
    result = 10 + '10'
except TypeError:
    print('невозможно складывать числа и строку')



try:
    sum = 10 + 10
except TypeError:
    print('невозможно складывать числа и строку')
else:
    print('Сложение прошло успешно')
    print(sum)
    
    
try:
    f = open('testfile_one.txt', 'w')
    f.write('Записываем строку в файл')
except TypeError:
    print('Произошло ошибка')
except OSError:
    print('ошибка')
finally:
    print('Эта строка выполняется в любом случае')
    
def ask_for_int():
    try:
        result = int(input('Пожалуйста введите число: '))
    except:
        print('Это не число')
    finally:
        print('окончание try/except/finally')
        
ask_for_int()


