try:
    number = int(input("Введите ваш номер: "))
except ValueError:
    print("Ой такой номер не существует лучше введите целое число")