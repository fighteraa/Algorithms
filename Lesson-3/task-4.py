# Определить, какое число в массиве встречается чаще всего

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный список:\n{array}')

max_friq_el = 0
number = 0
for i in array:
    if max_friq_el < array.count(i):
        max_friq_el = array.count(i)
        number = i
print(f'Чаще всего встречается число: {number}, оно встретилось: {max_friq_el} раз(а)')
