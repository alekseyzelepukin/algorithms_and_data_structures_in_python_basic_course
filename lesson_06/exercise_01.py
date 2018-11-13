# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.


# Python 3.7.0
# Windows 10 Home x64


import sys


# будем использовать для проверки
def show_size(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


def memory_size(logging=False):
    """
    функция подсчитывает выделенную под переменные память
    функция возвращает целое число в байтах
    logging=True - для вывода подробной информации
    """

    if logging:
        print('*' * 100)

    variables = globals().copy()
    size = 0

    for obj, val in variables.items():
        if obj.startswith('__'):
            continue
        elif hasattr(val, '__loader__'):
            continue
        elif hasattr(val, '__call__'):
            continue
        size += sys.getsizeof(val)
        if logging:
            print(f'Под переменную {obj} выделено: '
                  f'{sys.getsizeof(val)} байт (накопленный итог: {size} байт)')
        if hasattr(val, '__iter__'):
            if hasattr(val, 'items'):
                for key, value in val.items():
                    size += sys.getsizeof(key)
                    size += sys.getsizeof(value)
                    if logging:
                        print(f'Под ключ {key} выделено: '
                              f'{sys.getsizeof(key)} байт (накопленный итог: {size} байт)')
                        print(f'Под значение {value} выделено: '
                              f'{sys.getsizeof(value)} байт (накопленный итог: {size} байт)')
            elif not isinstance(val, str):
                for item in val:
                    size += sys.getsizeof(item)
                    if logging:
                        print(f'Под элемент {item} выделено: '
                              f'{sys.getsizeof(item)} байт (накопленный итог: {size} байт)')
    if logging:
        print('*' * 100)

    return size


# lesson_01 / exercise_01
# # 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# n = 123  # имитируем пользовательский ввод
#
# h = n // 100
# t = n // 10 % 10
# u = n % 10
#
# print(f'Под переменные выделено: {memory_size()} байт')
#
# # проверка:
# show_size(n)
# show_size(h)
# show_size(t)
# show_size(u)

# lesson_02 / exercise_04
# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# n = 1  # для учебных целей установим количество итераций цикла равным 1
#
# e = 1
# s = 0
#
# for _ in range(n):
#     s += e
#     e /= -2
#
# print(f'Под переменные выделено: {memory_size()} байт')
#
# # проверка:
# show_size(n)
# show_size(e)
# show_size(s)
# show_size(_)


# lesson_03 / exercise_02
# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

SIZE = 10

array = [8, 3, 15, 6, 4, 2]  # массив из условия задачи

even_indexes = []

for index, element in enumerate(array):
    if element % 2 == 0:
        even_indexes.append(index)


print(f'Под переменные выделено: {memory_size()} байт')

# # проверка:
# show_size(SIZE)
# show_size(array)
# show_size(even_indexes)
# show_size(index)
# show_size(element)


# проверим работоспособность функции на словаре

# my_dict = {
#     'a': 42,
#     'b': 123.007,
#     'c': True,
#     'd': 'hello world'
# }

# print(f'Под переменные выделено: {memory_size(logging=True)} байт')

# проверка:
# show_size(my_dict)
