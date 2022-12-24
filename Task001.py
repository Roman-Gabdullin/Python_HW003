# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

quant = int(input('Введите количество элементов списка: '))
min_num = int(input('Введите минимальный элемент списка: '))
max_num = int(input('Введите максимальный элемент списка: '))
list = []
for i in range(quant):
    list.append(random.randint(min_num,max_num+1))
print()
print(f'Список: {list}')
print()
sum = 0
list_odd = []
for i in range(1, len(list), 2):
    list_odd.append(list[i])
    sum+=list[i]
print('На начетных позициях элементы: ')
print(*list_odd, sep=',')
print()
print(f'Сумма элементов списка стоящих на нечетных позициях: {sum}')
