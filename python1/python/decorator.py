# # @property - синтаксистический сахар

# def second_outer(*dargs, **dkwargs):
#     def outer(func):
#         def inner(*args, **kwargs):
#             print(*dargs, **dkwargs)
#             return func(*args, **kwargs)
        
#         return inner
#     return outer


# @second_outer("Тестовое сообщение")
# def div(a, b):
#     return a / b

# print(div(1, 2))




# # 2)
# def second_outer(*dargs, **dkwargs):   # Параметры декоратора
#     def outer(func):                   # Сама декорируемая функция  
#         def inner(*args, **kwargs):    # Параметры функции
#             attempts = dkwargs["attempts"]
#             while attempts > 0:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err:
#                     print(f"Ошибка: {err}, осталось попыток: {attempts}")
#                     attempts -= 1
#         return inner
#     return  outer

# @second_outer(attempts = 70)
# def div(a, b):
#     return a / b

# print(div(1, 0))


# # 3)
# def second_outer(*dargs, **dkwargs):   # Параметры декоратора
#     def outer(func):                   # Сама декорируемая функция  
#         def inner(*args, **kwargs):    # Параметры функции
#             attempts = dkwargs["attempts"]
#             while attempts > 0:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err:
#                     print(f"Ошибка: {err}, осталось попыток: {attempts}")
#                     attempts -= 1
#         return inner
#     return  outer

# def simple_deco(func):
#     def inner(*args, **kwargs):
#         print("Реклама")
#         return func(*args, **kwargs)
#     return inner


# @second_outer(attempts = 7)
# @simple_deco

# def div(a, b):
#     return a / b

# print(div(1, 0))



# 4)
def adv_deco(password):
    def deco_1(my_class):
        c = 1
        def inner(*args, **kwargs):
            if password!= "секретный пароль":
                 raise ValueError("Неверный пароль")
            return my_class(*args, **kwargs)
        return inner
    return deco_1

@adv_deco(password="секретный пароль")
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
obj = MyClass(1, 2)
c = 1