# Написать программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.


print('Проверка условия 1+2+...+n = n(n+1)/2, где n — любое натуральное число')
n = int(input('Введите количество элементов последовательности n = '))
first = 0

for i in range(1, n+1):
    first += i
second = int(n * (n + 1) / 2)

if first == second:
    print(f'Левая часть равенства {first}  и правая часть {second} равны. Условие выполонено')
else:
    print('Условие не выполнено')
