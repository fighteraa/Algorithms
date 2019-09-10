letter_1 = str(input('Введите строчную букву английского алфавита: '))
letter_2 = str(input('Введите вторую строчную букву английского алфавита: '))
print(f'Буква "{letter_1}" - {ord(letter_1) - 96} буква в алфавите')
print(f'Буква "{letter_2}" - {ord(letter_2) - 96} буква в алфавите')
number = ord(letter_1) - ord(letter_2)
if number < 0:
    number = (number + 1) * (-1)
    print(f'Количество букв м/д введенными буквами: {number}')
elif number == 0:
    print(f'Количество букв 0 м/д введенными буквами')
else:
    number = number - 1
    print(f'Количество букв м/д введенными буквами: {number}')
