# def - клячовое слово
# отступы (tab/или 4 пробел)важны для они влиаеть на логику выполнение программы
# отступ налево (shrift + tab)
# разница между параметером и аргумент
# Параметр(ключ) — это значение, которое принимает функция. Аргумент(значения) — это значение, которое передается в функцию при ее вызове в программе.


# Синтаксис для объявления функции:

# def function_name(arguments):
#     # function body 

#     return



def greet():
    print('hello world')
    
greet()


def greet(name):
    result = f'hello {name}'
    print(result) 
       
greet('world')
greet('Azat')

# если не передат аргумент или больше то ошибка


def greet_one(message, name='world'):
    result = f'{message}, {name}'
    print(result)
    
greet_one(message='Hello')



def greet_two(message, name='world'):
    result = f'{message}, {name}'
    return result

g = greet_two('hello').title()
print(g)



children = ['arbuzov_1000', 'ivanov_2030', 'petrov_1255', 'Azat_2002']

def year(name):
    return name.split('_')[-1]


s_children = sorted(children, key=year)
print(s_children)


def add(x,y):
    return x + y

print(add('gweru', 'try'))


def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod
print(fact(6))


def get_user():
    name = "alex"
    age = 27
    admin = False
    return name, age, admin

user = get_user()
print(user[0])
print(user[1])
print(user[2])


# def personal_details():
#     name, age = "Bekzat", 19
#     address = "kyrgyzstan, Bishkek"
#     print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

# personal_details()