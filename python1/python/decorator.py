# @property - синтаксистический сахар

def second_outer(*dargs, **dkwargs):
    def outer(func):
        def inner(*args, **kwargs):
            print(*dargs, **dkwargs)
            return func(*args, **kwargs)
        
        return inner
    return outer


@second_outer("Тестовое сообщение")
def div(a, b):
    return a / b

print(div(1, 2))




# 2)
def second_outer(*dargs, **dkwargs):   # Параметры декоратора
    def outer(func):                   # Сама декорируемая функция  
        def inner(*args, **kwargs):    # Параметры функции
            attempts = dkwargs["attempts"]
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f"Ошибка: {err}, осталось попыток: {attempts}")
                    attempts -= 1
        return inner
    return  outer

@second_outer(attempts = 70)
def div(a, b):
    return a / b

print(div(1, 0))


# 3)
def second_outer(*dargs, **dkwargs):   # Параметры декоратора
    def outer(func):                   # Сама декорируемая функция  
        def inner(*args, **kwargs):    # Параметры функции
            attempts = dkwargs["attempts"]
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print(f"Ошибка: {err}, осталось попыток: {attempts}")
                    attempts -= 1
        return inner
    return  outer

def simple_deco(func):
    def inner(*args, **kwargs):
        print("Реклама")
        return func(*args, **kwargs)
    return inner


@second_outer(attempts = 7)
@simple_deco

def div(a, b):
    return a / b

print(div(1, 0))


