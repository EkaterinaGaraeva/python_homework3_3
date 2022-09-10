# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import math
import random

def product_of_pairs_of_numbers(one_list):
    list_of_products = []
    for i in range(0, math.ceil(len(one_list) / 2)):
        list_of_products.append(one_list[i] * one_list[len(one_list) - 1 - i])
    return list_of_products


list_of_numbers = [random.randint(0, 10) for x in range(0, 7)]
print(list_of_numbers)
print(product_of_pairs_of_numbers(list_of_numbers))
