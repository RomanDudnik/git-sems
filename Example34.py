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