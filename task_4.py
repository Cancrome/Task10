"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words:
    a = i.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))
    print(' ')
