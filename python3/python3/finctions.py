def main():
    print('У меня для вас известие')
    message()
    print('До свидания')
    
def message():
    print('Я - Кто-то')
    print('Президент')
    
main()


# 2)

def main():
    start()
    input('Нажмите на Enter увидете шаг1')
    step()
    input('Нажмите на Enter увидете шаг2')
    step1()
    input('Нажмите на Enter увидете шаг3')
    step2()
    
def start():
    print('Что-то')
    
def step():
    print('Это шаг1')
    
def step1():
    print('Это шаг2')
    
def step2():
    print('Это шаг3')
    
main()

# 3)
def main_two():
    texas()
    california()    
def texas():
    birds = 5000
    print(f'В течасе обитает {birds} птиц')
    
def california():
    birds = 8000
    print(f'В каливорние обитает {birds} птиц')   
    
     
main_two()

# 4)
def main_three():
    value = 5
    show_double(value)
    
def show_double(numbers):
    result = numbers * 2
    print(result)
    
main_three()

# 5)
def main_six():
    intro()
    cups_needed = int(input('Введите число чашек: '))
    cups_to_ounces(cups_needed)
    
def intro():
    print('Что-то')
    
def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'Число конвертируется в {ounces} унции')
    
main_six()
    
    
# 6)
def main_fo():
    print('Сумма чисел 12 и 45 равнеятся')
    show_sum(12, 45)
    
def show_sum(num1, num2):
    result_sum = num1 + num2
    print(result_sum)
    
main_fo()