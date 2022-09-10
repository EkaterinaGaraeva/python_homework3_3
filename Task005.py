# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

def negafibonacci(number):
    if number > 1:
        fib = [0, 1]
        negafib = [1, -1]
        for i in range(2, number + 1):
            fib.append(fib[i-1] + fib[i-2])
        for j in range(2, number):
            negafib.append(negafib[j-2] - negafib[j-1])
        negafib.reverse()
        return negafib + fib
    elif number == 0:
        return [0]
    elif number == 1:
        return [1, 0, 1]


n = 8
print(negafibonacci(n))
