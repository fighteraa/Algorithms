# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
# в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
# одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
# используйте метод сортировки, который не рассматривался на уроках

# Отсортировал массив пирамидальной сортировкой и нашел медиану.
import random


def heap_sort(heap_array):
    def sorting_tree(parent, limit):
        i = 0
        item = heap_array[parent]
        while True:
            child = (parent * 2) + 1
            if child >= limit:
                i += 1
                break
            if child + 1 < limit and heap_array[child] < heap_array[child + 1]:
                i += 1
                child += 1
            if item < heap_array[child]:
                i += 1
                heap_array[parent] = heap_array[child]
                parent = child
            else:
                i += 1
                break
        heap_array[parent] = item

    length = len(heap_array)
    for index in range((length // 2) - 1, -1, -1):
        sorting_tree(index, length)
    for index in range(length - 1, 0, -1):
        heap_array[0], heap_array[index] = heap_array[index], heap_array[0]
        sorting_tree(0, index)
    return heap_array


m = int(input('Введите натуральное число: '))
size = 2 * m + 1
MIN_ITEM = -100
MAX_ITEM = 100
rand_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
print(f'Исходный массив:\n{rand_array} ')
median_array = heap_sort(rand_array)
print(f'Отсортированный массив:\n{median_array} ')
index = len(median_array) // 2
print(f'Медиана в массиве находится на {index} месте и равна: {median_array[index]}')
