# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

i1 = int(input('Введите номер буквы латинского алфавита от "1" до "26":'))
print(f'Буква с номером {i1} это {chr(i1 + 96)}')

