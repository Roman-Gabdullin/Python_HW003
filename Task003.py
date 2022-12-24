# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

quant = int(input('Введите количество элементов списка: '))
min_num = int(input('Введите минимальный элемент списка: '))
max_num = int(input('Введите максимальный элемент списка: '))
list = []
for i in range(quant):
    list.append(round(random.uniform(min_num,max_num+1),3))
print()
print(f'Список: {list}')
min = round(list[0]%1,3)
max = 0
for i in list:
    if min > i%1 and i%1!=0: min = round(i%1,3)
    if max < i%1: max = round(i%1,3)
print(f'Минимальное число дробной части: {min}')
print(f'Максимальное число дробной части: {max}')
res = round(max - min,3)
print(f'Разница между максимальным и минимальным числом дробной части: {res}')