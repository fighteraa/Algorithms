# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
# отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10
# попыток число не отгадано, то вывести загаданное число

import random

user_number = int(input('Введите число от 0 до 100: '))
hidden_number = random.randint(0, 100)
i = 0
while i < 10:
    if user_number > hidden_number:
        print('число меньше')
        i += 1
    elif user_number < hidden_number:
        print('число больше')
        i += 1
    else:
        print(f'Поздравляем! Вы угадали: {hidden_number}')
        break;
    print(f'попытка {i}')
    user_number = int(input('Еще попытка: '))
    if i == 10:
        print(f'Попытки закончились. это число {hidden_number}')
