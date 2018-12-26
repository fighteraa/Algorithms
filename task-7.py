# Напишите программу, доказывающую или проверяющую, что для множества натуральных
# чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Введите натуральное число: '))
left_side = 0
for i in range(1, n + 1):
    left_side = left_side + i
right_side = n * (n + 1) / 2
if left_side == right_side:
    print(f'Совпало {left_side} = {right_side}')
else:
    print('Не совпало')