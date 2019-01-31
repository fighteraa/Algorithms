# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить
# программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для
# одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в
# комментариях версию Python и разрядность вашей ОС.


# JetBrains PyCharm Community Edition 2018.3.1 x64
# Система 64 разрядная

# Задание из 3-го урока №4: Определить, какое число в массиве встречается чаще всего
# Сделал для нее 3 варианта, чтобы посмотреть затраты памяти.


import random
import sys


def sum_mamory_size(func_for_sum):
    def total_sum(arg1):
        # print('*' * 50)
        memory_for_sum = func_for_sum(arg1)
        sum_ = 0
        for key, value in memory_for_sum.items():
            sum_ += get_size(value)
            # print(f'    переменная {key} = {value}, size = {get_size(value)}')
        print(f'Под переменные выделено памяти: {sum_}')
    return total_sum


def get_size(object, view=None):
    size = sys.getsizeof(object)
    if view is None:
        view = set()
    object_id = id(object)
    if object_id in view:
        return 0
        view.add(object_id)
    if isinstance(object, dict):
        size += sum([get_size(value, view) for value in object.values()])
        size += sum([get_size(key, view) for key in object.keys()])
    elif hasattr(object, '__iter__') and not isinstance(object, (str, bytes, bytearray)):
        size += sum([get_size(i, view) for i in object])
    return size


@sum_mamory_size
def version_one(size):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    # print(f'Исходный список:\n{array}')
    max_friq_el = 0
    number = 0
    for i in array:
        if max_friq_el < array.count(i):
            max_friq_el = array.count(i)
            number = i
    # print(f'Чаще всего встречается число: {number}, оно встретилось: {max_friq_el} раз(а)')
    print('Вариант 1')
    variables = locals().copy()
    return variables


@sum_mamory_size
def version_two(size):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    # print(f'Исходный список:\n{array}')
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]
    # if frequency > 1:
    #     print(f'Число {num} встречется {frequency} раз(а)')
    # else:
    #     print('Все элементы уникальны')
    print('Вариант 2')
    variables = locals().copy()
    return variables


@sum_mamory_size
def version_three(size):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    # print(f'Исходный список:\n{array}')
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    # if num is not None:
    #     # print(f'Число {num} встречается {frequency} раз(а)')
    # else:
    #     # print('Все элементы уникальны')

    print('Вариант 3')
    variables = locals().copy()
    return variables


version_one(10000)
version_two(10000)
version_three(10000)

# Выводы, сделанные в результате измерений времени:
# Алгоритмы 3 имеют линейную сложность О(n)
# алгоритм 2 за счет вложенного цикла имеет квадратичную сложность O(n**2).
# алгоритм 1 имеет квадратичную сложность O(n**2), но он быстрее второго, т.к. встроенная функция
# работает быстро, но с ростом числа элементов массива ее скорости перестает хватать.
# Алгоритм со словарем (№3) оказался быстрее всего.

# Результаты проверки занимамой памяти:
# Массив из 10 элементов:
# Вариант 1
# Под переменные выделено памяти: 322
# Вариант 2
# Под переменные выделено памяти: 350
# Вариант 3
# Под переменные выделено памяти: 750

# Массив из 100 элементов:
# Вариант 1
# Под переменные выделено памяти: 1940
# Вариант 2
# Под переменные выделено памяти: 1970
# Вариант 3
# Под переменные выделено памяти: 5030

# Массив из 1000 элементов:
# Вариант 1
# Под переменные выделено памяти: 18582
# Вариант 2
# Под переменные выделено памяти: 18602
# Вариант 3
# Под переменные выделено памяти: 24028

# Массив из 10000 элементов
# Вариант 1
# Под переменные выделено памяти: 183688
# Вариант 2
# Под переменные выделено памяти: 183756
# Вариант 3
# Под переменные выделено памяти: 189134

# Вывод: Когда у нас количество элементов в массиве маленькое,
# то словарь в третьем варианте занимает много места, поэтому и размер памяти большой.
# Когда у нас большое количество элементов, то в первых двух вариантах мы видим небольшое
# различие, т.к. эти массивы генерируются с разнами числами.
# При больших значениях в массиве 1000 и 10000 элементов память в первом и во втором варианте
# по сравнению с третьим отличается примерно на 5300-5500.
# (Подробнее это можно посмотреть, раскомментировав 26 строку)
# Большую чоасть этой память занимает словарь,максимальное количество элементов в словаре
# может быть максимум 100, но он содержит разные значения, поэтому память практически не изменяется.
# Интересно получилось в данном случае, что алгоритм 3, который быстрее по времени, занимает больше памяти.
# А если диапазон значений в массиве будет больше, то словарь будет больше
# и память будет увеличиваться.
