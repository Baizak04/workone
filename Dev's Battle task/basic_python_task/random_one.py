# Напишите программу, которая генерирует случайное трехзначное число и вычислить сумму его цифр

from random import randint

n = randint(100, 999)

a = n // 100
b = (n // 10) % 10
c = n % 10

print(a + b + c)