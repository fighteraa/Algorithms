# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
# отсортированный массивы.

import random


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    lefthalf = array[:middle]
    righthalf = array[middle:]
    merge_sort(lefthalf)
    merge_sort(righthalf)

    left_cur = 0
    right_cur = 0
    cur_index = 0

    while left_cur < len(lefthalf) and right_cur < len(righthalf):
        if lefthalf[left_cur] < righthalf[right_cur]:
            array[cur_index] = lefthalf[left_cur]
            left_cur += 1
        else:
            array[cur_index] = righthalf[right_cur]
            right_cur += 1
        cur_index += 1

    while left_cur < len(lefthalf):
        array[cur_index] = lefthalf[left_cur]
        left_cur += 1
        cur_index += 1

    while right_cur < len(righthalf):
        array[cur_index] = righthalf[right_cur]
        right_cur += 1
        cur_index += 1
    return array


size = 1000
MIN_ITEM = 0
MAX_ITEM = 49
rand_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
# array = [i for i in range(0, 50)]
print(f'Исходный массив:\n{rand_array}')
print(f'Отсортированный массив:\n{merge_sort(rand_array)}')
