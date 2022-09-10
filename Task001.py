# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def sum_of_numbers(one_list):
    sum = 0
    for i in range(1, len(one_list), 2):
        sum += one_list[i]
    return sum


list_of_numbers = [random.randint(0, 10) for x in range(0, 10)]
print(list_of_numbers)
print(f'Сумма элементов списка, стоящих на нечётной позиции => {sum_of_numbers(list_of_numbers)}')
