'''
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке

Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам

Вывод:
Парам пам-пам
'''
"Решение 1"

# def PuhSongVowels(song):
#     vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ы', 'ю', 'я']
#     num_vowels = list()
#     for i in song:
#         count = 0
#         for j in i:
#             if j in vowels:
#                 count += 1
#         num_vowels.append(count)
#     return num_vowels

# def GodSong(num):
#     if len(set(num)) == 1:
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')

# poem = list(input('Напишите стихотворение: ').lower().split())
# GodSong(PuhSongVowels(poem))

"Решение 2"

# poem = list(input('Напишите стихотворение: ').lower().split())
# print(poem)
# volwes = 'аеёиоуэыюя'

# num_volwes = [sum(x in volwes for x in y) for y in poem]
# # print(num_volwes)

# if len(set(num_volwes)) == 1 :
#     res = "Парам пам-пам"
# res = "Пам парам"

# print(res)

'''
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.

Ввод:
print_operation_table(lambda x, y: x * y)

Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
'''


def print_operation_table(op, rows, columns):
    for i in range(1, rows + 1):
        matrix = list()
        for j in range(1, columns + 1):
            num_op = op(i, j)
            matrix.append(num_op)
        # print (*matrix)
        print('\t'.join([str(x) for x in matrix]))  # центрирование столбцов


num_rows = 6
num_columns = 6
print_operation_table(lambda x, y: x * y, num_rows, num_columns)
