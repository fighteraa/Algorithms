# Задание: Определить, какое число в массиве встречается чаще всего

# Проверил производительность в зависимости от количества элементов в массиве
# и стало инетересно посмотреть какое время будет с count

import random
import cProfile

# Вариант 1 мой вариант из 3 ДЗ
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

# 100 loops, best of 5: 78 usec per loop - 10
# 100 loops, best of 5: 1.18 msec per loop- 100
# 100 loops, best of 5: 57.6 msec per loop - 1000
# 100 loops, best of 5: 217 msec per loop - 2000

# cProfile.run('version_one(2000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:7(version_one) - 10
# 1    0.000    0.000    0.001    0.001 task_1.py:7(version_one) - 100
# 1    0.000    0.000    0.060    0.060 task_1.py:7(version_one) - 1000
# Приведу полное описание от cProfile для 2000 элементов в массиве:
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.226    0.226 <string>:1(<module>)
#      2000    0.007    0.000    0.014    0.000 random.py:174(randrange)
#      2000    0.002    0.000    0.016    0.000 random.py:218(randint)
#      2000    0.005    0.000    0.007    0.000 random.py:224(_randbelow)
#         1    0.003    0.003    0.019    0.019 task_1.py:10(<listcomp>)
#         1    0.001    0.001    0.226    0.226 task_1.py:7(version_one)
#         1    0.000    0.000    0.226    0.226 {built-in method builtins.exec}
#      2000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      2004    0.206    0.000    0.206    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2534    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}

# Вариант 2
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

# 100 loops, best of 5: 106 usec per loop - 10
# 100 loops, best of 5: 2.18 msec per loop - 100
# 100 loops, best of 5: 167 msec per loop - 1000
# 100 loops, best of 5: 660 msec per loop - 2000

# cProfile.run('version_two(2000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:47(version_two) - 10
# 1    0.002    0.002    0.002    0.002 task_1.py:47(version_two) - 100
# 1    0.164    0.164    0.174    0.174 task_1.py:47(version_two) - 1000
# 1    0.848    0.848    0.868    0.868 task_1.py:47(version_two) - 2000
# Приведу полное описание от cProfile для 2000 элементов в массиве:
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.868    0.868 <string>:1(<module>)
#      2000    0.006    0.000    0.013    0.000 random.py:174(randrange)
#      2000    0.002    0.000    0.015    0.000 random.py:218(randint)
#      2000    0.005    0.000    0.007    0.000 random.py:224(_randbelow)
#         1    0.848    0.848    0.868    0.868 task_1.py:47(version_two)
#         1    0.003    0.003    0.018    0.018 task_1.py:50(<listcomp>)
#         1    0.000    0.000    0.868    0.868 {built-in method builtins.exec}
#      2001    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#      2000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2594    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}


# Вариант 3
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

# 100 loops, best of 5: 78.5 usec per loop - 10
# 100 loops, best of 5: 676 usec per loop - 100
# 100 loops, best of 5: 7.21 msec per loop - 1000
# 100 loops, best of 5: 14.5 msec per loop - 2000


cProfile.run('version_three(2000)')
# 1    0.000    0.000    0.000    0.000 task_1.py:94(version_three) - 10
# 1    0.000    0.000    0.001    0.001 task_1.py:94(version_three) - 100
# 1    0.001    0.001    0.010    0.010 task_1.py:94(version_three) - 1000
# 1    0.001    0.001    0.020    0.020 task_1.py:94(version_three) -2000
# Приведу полное описание от cProfile для 2000 элементов в массиве:
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.020    0.020 <string>:1(<module>)
#      2000    0.006    0.000    0.013    0.000 random.py:174(randrange)
#      2000    0.002    0.000    0.016    0.000 random.py:218(randint)
#      2000    0.005    0.000    0.007    0.000 random.py:224(_randbelow)
#         1    0.001    0.001    0.020    0.020 task_1.py:94(version_three)
#         1    0.003    0.003    0.019    0.019 task_1.py:97(<listcomp>)
#         1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#      2000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2513    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}



# version_one(5000)
# version_two(5000)
# version_three(5000)


# Выводы:
# Составил график по точкам и приложил к отчету. Называется task_1.png
# Не учел возможности github график не отображается..
# Из них видно, что алгоритмы 3 имеют линейную сложность О(n)
# алгоритм 2 за счет вложенного цикла имеет квадратичную сложность O(n**2).
# алгоритм 1 имеет квадратичную сложность O(n**2), но он быстрее второго, т.к. встроенная функция
# работает быстро, но с ростом числа элементов массива ее скорости перестает хватать.
# Алгоритм со словарем (№3) оказался быстрее всего.
