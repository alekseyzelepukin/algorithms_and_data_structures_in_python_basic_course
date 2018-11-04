# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 – если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

SIZE = 10

array = [randint(0, 9) for _ in range(SIZE)]

# array = [8, 3, 15, 6, 4, 2]  #  массив из условия задачи

print(array)

even_indexes = []

for index, element in enumerate(array):
    if element % 2 == 0:
        even_indexes.append(index)

print(even_indexes)

for index in even_indexes:
    print(f'Индекс {index}: элемент {array[index]}')
