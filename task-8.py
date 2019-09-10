year = int(input('Введите год: '))
if year % 4 != 0:
    print(f'Год {year} не високосный ')
elif year % 100 == 0:
    if year % 400 == 0:
        print(f'Год {year} високосный')
    else:
        print(f'Год {year} не високосный')
else:
    print(f'Год {year} високосный')
