numeric = int(input('Введите трезначное число: '))
number0 = numeric % 10
number1 = numeric % 100 // 10
number2 = numeric // 100
sum = number0 + number1 + number2
product = number0 * number1 * number2
print(f'Сумма = {sum}')
print(f'Произведение = {product}')
