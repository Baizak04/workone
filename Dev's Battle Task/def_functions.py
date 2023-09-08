from math import ceil

def chunk(arr, size):
    return list(map(lambda x: arr[x * size: x * size + size],
                    list(range(0, ceil(len(arr))))))
    
print(chunk([1, 2, 3, 4, 5, 6,], 2))

# def print_two(*args):
#     arg1, arg2 = args
#     print(f'аргумент1: {arg1}, аргумент2 {arg2}')
    
# def print_two_again(arg1, arg2):
#     print(f'аргумент1 {arg1}, аргумент2 {arg2}')
    
# def print_one(arg1):
#     print(f'аргумент1 {arg1}')
    
# def print_none():
#     print('а я ничего не получаю')
    
# print_two('Михайл', 'Райтман')
# print_two_again('Михайл', 'Райтман')
# print_one('Первый')
# print_none()

# # 2)
# def cheese_and_crackers(cheese_count, boxes_of_cracker):
#     print(f'У нас есть {cheese_count} сырков!')
#     print(f'У нас есть {boxes_of_cracker} пачек чипсов!')
#     print("Этого достаточно для вечеринки!")
#     print("Погнали!\n")
    
# print("Мы можем непосредсвенно передать числа функции:")
# cheese_and_crackers(20, 30)

# print("ИЛИ мы можем использовать переменный из нашего сценария:")
# amount_of_cheese = 10
# amount_of_cracker = 50

# cheese_and_crackers(amount_of_cheese, amount_of_cracker)

# def hello(user):
#     print(f"Hello, {user}!")

# code = "hello('Alex')"
# exec(code)