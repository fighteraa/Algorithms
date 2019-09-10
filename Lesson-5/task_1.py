# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

from collections import defaultdict

company = defaultdict(list)
n = int(input('Введите количество компаний: '))
i = 1
assert n > 1, 'Введено меньше 2-х разных компаний, повторите запуск программы'
avarage = 0
my_summa = 0
company_list = []
while i <= n:
    name = str(input(f'введите название {i} компании: '))
    quarter_1 = int(input('Введите прибыль за первый квартал: '))
    quarter_2 = int(input('Введите прибыль за второй квартал: '))
    quarter_3 = int(input('Введите прибыль за третий квартал: '))
    quarter_4 = int(input('Введите прибыль за четвертый квартал: '))
    summa = quarter_1 + quarter_2 + quarter_3 + quarter_4
    my_summa += summa
    company[name] = summa
    company_list.append(company)
    company = defaultdict(list)
    i += 1
avarage = my_summa / n

lst_more_aver = []
lst_less_aver = []
flag_all_aver = True
for lst in company_list:
    for keys, valyes in lst.items():
        if lst[keys] < avarage:
            flag_all_aver = False
            lst_less_aver.append(keys)
        if lst[keys] > avarage:
            lst_more_aver.append(keys)
            flag_equ = False
else:
    if flag_all_aver == True:
        print('У всех компаний одинаковый уровень дохода')

print(f'Предприятия, чья прибыль меньше среднего:')
for name in lst_less_aver:
    print(name)
print(f'Предприятия, чья прибыль больше среднего:')
for name in lst_more_aver:
    print(name)