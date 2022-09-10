# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import random

def binary_number(number):
    bin_number = ''
    while (number > 0):
        bin_number = str(int(number % 2)) + bin_number
        number //= 2
    return bin_number


n = random.randint(0, 100)
print(f'{n} => {bin(n)}')
print(f'{n} => {binary_number(n)}')
