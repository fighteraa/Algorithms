# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.

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

print(f'Минимальный элемент: {minim}')
print(f'Максимальный элемент: {maxim}')

if array.index(minim) > array.index(maxim):
    array[array.index(minim)], array[array.index(maxim)] = array[array.index(maxim)], array[array.index(minim)]
else:
    array[array.index(maxim)], array[array.index(minim)] = array[array.index(minim)], array[array.index(maxim)]
print(f'Итоговый список со сменой переменных:\n{array}')
