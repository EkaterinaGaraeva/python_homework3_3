# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def difference(one_list):
    max = one_list[0] - int(one_list[0])
    min = one_list[0] - int(one_list[0])
    for number in one_list:
        if isinstance(number, float):
            # if (number - int(number)) > max:
            #     max = number - int(number)
            # if (number - int(number)) < min:
            #     min = number - int(number)
            max = number - int(number) if (number - int(number)) > max else max
            min = number - int(number) if (number - int(number)) < min else min
    return max - min


list_with_example = [1.1, 1.2, 3.1, 5, 10.01]
list_of_numbers = [round(random.uniform(0, 10), 2) for x in range(0, 7)]
print(list_of_numbers)
print(round(difference(list_with_example), 2))
print(round(difference(list_of_numbers), 2))