# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть
# дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти
# количество различных подстрок в этой строке.


def find_subline_hash(line):
    len_sub = 1
    subline_set = set()
    while len_sub <= len(line):
        for i in range(len(line)):
            if i + len_sub <= len(line) and len_sub < len(line):
                hash_subline = hash(line[i:i + len_sub])
                if hash_subline in subline_set:
                    continue
                else:
                    subline_set.add(hash_subline)
                    # print(f'{line[i:i + len_sub]} = {hash_subline}') #Вывод подстроки и ее хеша
        len_sub += 1
    return subline_set


line = (input('Введите строку: ')).lower()
print(line)
answer_set = find_subline_hash(line)
print(f'Количество различных подстрок: {len(answer_set)}')


