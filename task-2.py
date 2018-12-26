# Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = int(input('Введите натуральное число: '))
even = 0
no_even = 0
while number > 0:
    numeral = number % 10
    number = number // 10
    if numeral % 2 == 0:
        even += 1
    else:
        no_even += 1
print(f'Четных чисел: {even}')
print(f'Нечетных чисел: {no_even}')
