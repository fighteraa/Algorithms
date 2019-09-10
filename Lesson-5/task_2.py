# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
# число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

from collections import Counter

numerals = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

number11 = Counter()
number22 = Counter()

number1 = list(input('Введите первое шестнадцатиразрядное число: '))
number2 = list(input('Введите второе шестнадцатиразрядное число: '))

# number1 = list(['C', '4', 'F'])
# number2 = list(['A', '2'])

# Вместо тогг, чтобы просто счивывать массив с конца, я его сначала разворачиваю и считываю с начала
# сразу не пришло в голову, что есть возможность массив с конца считывать
number1.reverse()
number2.reverse()

if len(number1) >= len(number2):
    len_arr = len(number1)
else:
    len_arr = len(number2)

# Перевод введенной строки в 2 массива Counter, чтобы потом их складывать
len_arr1 = len(number1)
len_arr2 = len(number2)
counter1 = 0
counter2 = 0
for i in range(len_arr):
    for keys in numerals.keys():
        if len(number1) > i:
            if number1[i] == keys:
                number11[counter1] = numerals[keys]
                counter1 += 1
        if len(number2) > i:
            if number2[i] == keys:
                number22[counter2] = numerals[keys]
                counter2 += 1

# print(f'Исходные числа переведенные: {number1}  и  {number2}')

#               Функция суммы:
# Сначала суммировали 2 числа Counter, а потом
# сложение в столбик
def my_summa(number_my11, number_my22):
    number_my11 = Counter(number_my11)
    number_my22 = Counter(number_my22)
    summa = number_my11 + number_my22
    offset = 0
    for keys in summa.keys():
        summa[keys] = summa[keys] + offset
        if summa[keys] >= 16:
            offset = summa[keys] // 16
            summa[keys] = summa[keys] % 16
        else:
            summa[keys] = summa[keys]
            offset = 0
    if offset > 0:
        summa[keys + 1] = offset
        offset = 0
    return summa

# Функция вывода в шестнадцатиричной  форме числа на экран:
def my_output(number_output):
    answer_output = []
    for i in range(len(number_output)):
        for keys, value in numerals.items():
            if number_output[i] == value:
                answer_output.append(keys)
    answer_output.reverse()
    return answer_output

# Умножение двух чисел
answer_spam = dict()
answer_product = []
offset = 0
k = 0
number11 = dict(number11)
number12 = dict(number22)
# print('*' * 50)
count_sum = 0
for keys1 in number11.keys():
    for keys2 in number22.keys():
        k = number11[keys1] * number22[keys2] + offset
        if k >= 16:
            offset = k // 16
            answer_spam[keys2 + count_sum] = k % 16
        else:
            answer_spam[keys2 + count_sum] = k
            offset = 0
    if offset > 0:
        answer_spam[keys2 + 1 + count_sum] = offset
        offset = 0
    count_sum += 1
    answer_product.append(answer_spam)
    answer_spam = dict()

# Окончательный вывод на экран
summa_out = my_summa(number11, number22)
print(f'Cумма = {my_output(summa_out)}')

product = Counter({})
for i in answer_product:
    product = my_summa(product, i)
print(f'Произведение = {my_output(product)}')