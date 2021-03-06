# Во втором массиве сохранить индексы четных элементов первого массива. Например, если
# дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1,
# 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого
# массива стоят четные числа.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'Исходный список:\n{array}')
index_of_even_num = []  # Узнать, есть ли такая встроенная функция
for i in array:
    if i % 2 == 0:
        index_of_even_num.append(array.index(i))

print(f'Индексы четных элементов первого массива:\n{index_of_even_num}')
