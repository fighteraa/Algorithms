# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции. По
# возможности доработайте алгоритм (сделайте его умнее).


import random


def bubble_sort(array, flag=True):
    if not flag:
        return array
    flag = False
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            flag = True
    if flag:
        bubble_sort(array)
    else:
        flag = False
        bubble_sort(array, flag)
    return array


size = 10
MIN_ITEM = -100
MAX_ITEM = 99
rand_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

# rend_array = [i for i in range(-100, 100)]

random.shuffle(rand_array)
print(f'Исходный массив: \n{rand_array}')
print(f'Отсортированный массив: \n{bubble_sort(rand_array)}')
