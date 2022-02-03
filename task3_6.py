# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

n = 10
arr = []
for i in range(n):
    arr.append(random.randint(1, 50))
print('Исходный массив')
print(arr)

mn = min(arr)
mx = max(arr)
idx_min = arr.index(mn)
idx_max = arr.index(mx)
print(f'Минимальное значение в массиве = {mn} и находится по индексу {idx_min}')
print(f'Максимальное значение в массиве = {mx} и находится по индексу {idx_max}')

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

summa = 0
for i in range(idx_min + 1, idx_max):
    summa += arr[i]
print(f'Сумма элементов между минимальным и максимальным значениями = {summa}')
