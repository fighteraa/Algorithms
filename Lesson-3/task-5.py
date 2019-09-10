# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный список:\n{array}')

flag_find_neg = 0
for i in array:
    if i < 0 and flag_find_neg == 0:
        max_negat_el = i
        flag_find_neg = 1
    if i < 0 and i > max_negat_el:
        max_negat_el = i

if flag_find_neg == 0:
    print(f'В массиве нет отрицательных элементов!')
else:
    print(f'Значение максимального отрицательного элемента: {max_negat_el}')
    print(f'Позиция(индекс) максимального отрицательного элемента: {array.index(max_negat_el)}')
