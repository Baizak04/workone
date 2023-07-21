import random

def fin(func):
    def wrapper(*f, **a):
        wrapper.attempts += 1
        return func(*f, **a)
    wrapper.attempts = 0
    return wrapper

@fin
def fin(number):
    guess = int(input("Угадайте число от 1 до 100: "))
    if guess == number:
        print(f"Вы угадали число {number} за {fin.attempts} попыток! ")
    elif guess < number:
        print("Загаданное число больше")
        fin(number)
    else:
        print("Загаданное число меньше")
        fin(number)
        
if __name__ == '__main__':
    number = random.randint(1, 1000000)
    fin(number)        