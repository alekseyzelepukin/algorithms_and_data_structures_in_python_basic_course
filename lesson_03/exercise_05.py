# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import randint

SIZE = 10

array = [randint(-9, 9) for _ in range(SIZE)]

print(array)

max_neg_index = -1

for index, element in enumerate(array):
    if element < 0:
        if max_neg_index == -1:
            max_neg_index = index
        elif element > array[max_neg_index]:
            max_neg_index = index

if max_neg_index == -1:
    print('В массиве нет отрицательных элемпнтов')
else:
    print(f'Элемент: {array[max_neg_index]}, позиция: {max_neg_index}')
