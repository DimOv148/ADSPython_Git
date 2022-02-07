import random
import cProfile


def ar(n):
    arr = [0] * n
    even = []

    for i in range(n):
        arr[i] = random.randint(1, 100)
        if arr[i] % 2 == 0:
            even.append(i)

    # print(f'Исходный массив {arr}')
    # print(f'Индексы четных элементов: {even}')
    return even


# "df.ar(20)" 1000 loops, best of 5: 13 usec per loop
# "df.ar(50)" 1000 loops, best of 5: 32.1 usec per loop
# "df.ar(500)" 1000 loops, best of 5: 323 usec per loop
# "df.ar(1000)" 1000 loops, best of 5: 642 usec per loop

# cProfile.run('ar(20') ****** ncalls 1
# cProfile.run('ar(1000)') ****** ncalls 1
# при любом значении n функция вызывает себя 1 раз.


def ar1(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(1, 50) - 51)
    # print(arr)

    i = 0
    idx = -1
    while i < n:
        if arr[i] < 0 and idx == -1:
            idx = i
        elif 0 > arr[i] > arr[idx]:
            idx = i
        i += 1

    # print(f'Максимальный отрицательный элемент находится по индексу {idx} и равен : {arr[idx]}')
    return idx

# "df.ar1(20)" 1000 loops, best of 5: 14.6 usec per loop
# "df.ar1(50)" 1000 loops, best of 5: 36.4 usec per loop
# "df.ar1(500)" 1000 loops, best of 5: 362 usec per loop
# "df.ar1(1000)" 1000 loops, best of 5: 729 usec per loop

# cProfile.run('ar1(20)') ****** ncalls 1
# cProfile.run('ar1(1000)') ****** ncalls 1
# при любом значении n функция вызывает себя 1 раз.


# ar1(10)
# ar(20)
