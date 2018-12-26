# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
# экран. Например, если введено число 3486, то надо вывести число 6843.
number1 = int(input("Введите целое число: "))
number2 = 0
while number1 > 0:
    numeral = number1 % 10;
    number1 = number1 // 10;
    number2 = number2 * 10
    number2 = number2 + numeral
print(f'Число в обратном порядке: {number2}')