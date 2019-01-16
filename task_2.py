import cProfile


def sieve_Er(number):
    if number == 1:
        answer = 2
        # print(f'число {answer}, по счету {number}')

    else:
        n = number * number
        count = 1
        sieve = [i for i in range(n)]
        sieve[1] = 0
        result = []
        for i in range(2, n):
            if count == number:
                break
            if sieve[i] != 0:
                count += 1
                j = i + i
                while j < n:
                    sieve[j] = 0
                    j += i
        result = [i for i in sieve if i != 0]
        # print(result)
        # print(f'число {result[number - 1]}, по счету {number}')


# Тестирование через timeit
# 100 loops, best of 5: 72.4 usec per loop - 10
# 100 loops, best of 5: 2.2 msec per loop - 50
# 100 loops, best of 5: 9.66 msec per loop - 100
# 100 loops, best of 5: 30.6 msec per loop - 170
# 100 loops, best of 5: 73.5 msec per loop - 250
# 100 loops, best of 5: 320 msec per loop - 500
# 100 loops, best of 5: 1.39 sec per loop - 1000

# cProfile.run('sieve_Er(500)')
# 1    0.000    0.000    0.000    0.000 task_2.py:3(sieve_Er) - 10
# 1    0.002    0.002    0.003    0.003 task_2.py:3(sieve_Er) - 50
# 1    0.007    0.007    0.010    0.010 task_2.py:3(sieve_Er) - 100
# 1    0.022    0.022    0.028    0.028 task_2.py:3(sieve_Er) - 170
# 1    0.055    0.055    0.068    0.068 task_2.py:3(sieve_Er) - 250
# 1    0.301    0.301    0.367    0.367 task_2.py:3(sieve_Er) - 500
# 1    1.198    1.198    1.441    1.441 task_2.py:3(sieve_Er) - 1000

# Другой алгоритм реализации:
def my_not_sieve(number):
    if number == 1:
        answer = 2
        # print(f'число {answer}, по счету {number}')
    else:
        count = 1
        n = number * number
        lst = [2]
        for i in range(3, n + 1, 2):
            if count == number:
                break
            if (i > 10) and (i % 10 == 5):
                continue
            for j in lst:
                if j * j - 1 > i:
                    lst.append(i)
                    count += 1
                    break
                if (i % j == 0):
                    break
            else:
                lst.append(i)
                count += 1
        # print(lst)
        # print(f'число {lst[number - 1]}, по счету {number}')


# Тестирование через timeit
# 100 loops, best of 5: 29 usec per loop - 10
# 100 loops, best of 5: 374 usec per loop - 50
# 100 loops, best of 5: 722 usec per loop - 100
# 100 loops, best of 5: 1.73 msec per loop - 170
# 100 loops, best of 5: 2.71 msec per loop - 250
# 100 loops, best of 5: 6.89 msec per loop - 500
# 100 loops, best of 5: 24.8 msec per loop - 1000

cProfile.run('my_not_sieve(500)')
# 1    0.000    0.000    0.000    0.000 task_2.py:39(my_not_sieve) - 10
# 1    0.000    0.000    0.000    0.000 task_2.py:39(my_not_sieve) - 50
# 1    0.001    0.001    0.001    0.001 task_2.py:39(my_not_sieve) - 100
# 1    0.002    0.002    0.002    0.002 task_2.py:39(my_not_sieve) - 170
# 1    0.003    0.003    0.003    0.003 task_2.py:39(my_not_sieve) - 250
# 1    0.008    0.008    0.008    0.008 task_2.py:46(my_not_sieve) - 500
# 1    0.020    0.020    0.021    0.021 task_2.py:39(my_not_sieve) - 1000


# sieve_Er(3)
# my_not_sieve(4)

# Вывод:
# Алгоритм поиска простых числел, который я применил, имеет линейную сложность O(n).
# B википедии нашел сложность алгоритма Решета Эрастофена О(n * log(logn))
# Сложность растет с увеличение количества элементов в массиве, т.к. обработка исходного массива
# начинает занимать больше времени.
# В текущем примере мой алгоритм быстрее.
