# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random

n = 20
arr = [0] * n

for i in range(n):
    arr[i] = random.randint(1, 100)
    print(arr[i], end=' ')
print()

# # вариант min/max
mn = min(arr)
mx = max(arr)
idx_min = arr.index(mn)
idx_max = arr.index(mx)
print(f'arr[{idx_min + 1}] = {mn}   arr[{idx_max}] = {mx}')
arr[idx_min], arr[idx_max] = arr[idx_max], arr[idx_min]

# вариант с циклом
# mn = 0
# mx = 0
# for i in range(n):
#     if arr[i] < arr[mn]:
#         mn = i
#     elif arr[i] > arr[mx]:
#         mx = i
# print(f'arr[{mn}] = {arr[mn]}   arr[{mx}] = {arr[mx]}')
# spam = arr[mn]
# arr[mn] = arr[mx]
# arr[mx] = spam

for i in range(n):
    print(arr[i], end=' ')
print()
