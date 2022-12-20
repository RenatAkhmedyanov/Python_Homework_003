# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 3
# 1 2 3 4 5
# Вывод: 1

import random

n = int(input('Введите длину списка: '))
if n <= 0:
    print('Некорректный ввод! Введите натуральное число.')
else:    
    x = int(input('Введите искомое число: '))

    list = []
    count = 0

    for i in range(0,n):
        random_number = round(random.uniform(1, n/2))
        list.append(random_number)
        if list[i] == x: 
            count += 1

    print(list)
    if count == 0: print('Введенное число отсутствует в списке.')
    else: print(f'Количесвто раз, которое встречается введенное число: {count}')
