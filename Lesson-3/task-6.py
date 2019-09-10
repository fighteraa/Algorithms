# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный список:\n{array}')

minim = array[0]
maxim = array[0]
for i in array:
    if i > maxim:
        maxim = i
    if i < minim:
        minim = i

print(f'Минимальное число: {minim}')
print(f'Макимальное число: {maxim}')

summa = 0
if array.index(minim) > array.index(maxim):
    for j in range((array.index(maxim) + 1), array.index(minim)):
        summa += array[j]
else:
    for j in range((array.index(minim) + 1), array.index(maxim)):
        summa += array[j]
print(f'Итоговая сумма элементов между ними: {summa}')
