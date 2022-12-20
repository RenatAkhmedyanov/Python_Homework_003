# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший.

# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7

import random
import os
os.system('cls')

n = int(input('Введите длину списка: '))
if n <= 0:
    print('Некорректный ввод! Введите натуральное число.')
else:    
    x = int(input('Введите проверяемое число: '))

    list = []
    
    for i in range(0,n):
        random_number = round(random.uniform(1,n/2))
        list.append(random_number)
    print(list)
    list.sort(reverse = True)  
    min = list[0]    
    for item in list:
        if abs(item - x) <= abs(min - x):
            min = item
            
    if min == x: 
        print(f'Введенное число ({min}) есть в списке.')
    else:    
        print(f'Наименьшее ближайшее число: {min}')