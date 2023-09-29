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

try:
    a = 11 > 0 is True
    if answer:
        print(answer)
    else:
        print(True)
except:
    print(1)
    

try:
    print(1)
except Exception:
    print(0)
    
try:
    a = 2 + '1'
    print(a)
except TypeError:
    print('Error')
    
try:
    b = 1 / 0
except ZeroDivisionError:
    b = 0

print(b)

# try:
#     a = 1 + '1'
# except ValueError:
#     c = 0
    
# print(c)

try:
    e = "{0}".format(1)
except ValueError:
    e = "Error"
    
print(e)

# try:
# except Exception:
#     print(1)

try:
    k = 1 / 0
except ArithmeticError:
    k = 1
else:
    k = 0
    
print(k)

try:
    a = 10 / 5
except CustomError:
    print(1)
else:
    print(0)

