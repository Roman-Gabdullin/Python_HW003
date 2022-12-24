# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

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
res = []
if quant%2 == 1: count = quant//2+1
else: count = quant//2
for i in range(count):
    res.append(list[i]*list[-i-1])
print(res)