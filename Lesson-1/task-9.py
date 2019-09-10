print('Введите три разных числа')
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1 < num2 < num3:
    print(f'Среднее число {num2}')
elif num3 > num2 > num1:
    print(f'Среднее число {num2}')
elif num2 < num3 < num1:
    print(f'Среднее число {num3}')
elif num2 > num3 > num1:
    print(f'Среднее число {num3}')
else:
    print(f'Среднее число {num1}')
