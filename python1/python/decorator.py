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