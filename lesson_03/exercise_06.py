# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

SIZE = 10

array = [randint(0, 9) for _ in range(SIZE)]

print(array)

min_index = 0
max_index = 0

for index, element in enumerate(array):
    if element < array[min_index]:
        min_index = index
    if element > array[max_index]:
        max_index = index

if min_index == max_index:
    print('Все элементы массива одинаковы')
else:
    start, end = min_index, max_index

    if end < start:
        start, end = end, start

    total = 0
    for value in array[start+1:end]:
        total += value

    print(f'Сумма элементов: {total}')
