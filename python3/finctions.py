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