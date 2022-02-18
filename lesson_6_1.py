# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# c. проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл
# с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
# а проявили творчество, фантазию и создали универсальный код для замера памяти.

import sys
import random

total_memory = 0


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')
    global total_memory
    total_memory += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
    return total_memory


print(sys.version, sys.platform)
# 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] win32
matrix = [[random.randint(0, 50) for _ in range(5)] for _ in range(5)]

for line in matrix:  # выведем матрицу на экран
    for item in line:
        print(f'{item:>4}', end='')
    print()

show_size(matrix)
# type= <class 'list'>, size= 120
# type= <class 'int'>, size= 28
print('Всего выделено памяти под переменные total_memory =', total_memory)


min_element_column = None
lst = []
for col in range(0, len(matrix)):
    min_element_column = matrix[0][col]
    for row in matrix:
        if row[col] < min_element_column:
            min_element_column = row[col]
    lst.append(min_element_column)
print()

show_size(min_element_column)
# type= <class 'int'>, size= 24, object= 0
print('Всего выделено памяти под переменные total_memory=', total_memory)

show_size(lst)
# type= <class 'list'>, size= 120
# type= <class 'int'>, size= 28
print('Всего выделено памяти под переменные total_memory=', total_memory)

mx = lst[0]
# type= <class 'int'>, size= 28, object= 9
show_size(mx)

for item in lst:
    print(f'{item:>4}', end='')
    if item > mx:
        mx = item
print()

print(f'Максимальный элемент среди всех элементов столбцов в матрице равен: {mx}')
print('Всего выделено памяти под переменные total_memory=', total_memory)
