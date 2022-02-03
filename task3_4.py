# Определить, какое число в массиве встречается чаще всего.

import random
n = 15
arr = [0] * n

for i in range(n):
    arr[i] = random.randint(1, 20)
print(arr)

num = arr[0]
max_frq = 1
for i in range(n-1):
    frq = 1
    for k in range(i+1, n):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(f'{max_frq} раза встречается число {num}')
else:
    print('Все элементы уникальны')