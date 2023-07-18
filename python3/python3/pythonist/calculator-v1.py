from colorama import init
from colorama import Fore, Back, Style

init()

what = input("Что делаем (+, -): ")

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if what == "+":
    c = a + b
    print(Back.GREEN + "Результат:" + str(c))
elif what == "-":
    c = a - b
    print(Fore.RED + "Результат:" + str(c))
else:
    print(Style.DIM + 'Такой нету')    