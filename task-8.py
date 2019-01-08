# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
# должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
# ячейку строки. В конце следует вывести полученную матрицу.

matrix = []
for line in range(5):
    print(f'Введите 3 элемента {line + 1} строки через пробел и нажмите \'Enter\':')
    row = input().split()
    sum_line = 0
    for i in range(len(row)):
        row[i] = int(row[i])
        sum_line += row[i]
    row.append(sum_line)
    matrix.append(row)

print('*' * 59)
print(f'Итоговая матрица:')
for line in matrix:
    for i in line:
        print(f'{i:^7}', end='')
    print()
