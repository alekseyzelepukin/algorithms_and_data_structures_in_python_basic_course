# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint

SIZE = 10

array = [randint(0, 99) for _ in range(SIZE)]

print(array)

first_min = array[0]
second_min = array[1]

if second_min < first_min:
    first_min, second_min = second_min, first_min

for element in array[2:]:
    if element < first_min:
        second_min = first_min
        first_min = element
    elif element < second_min:
        second_min = element

print('Наименьшение элементы массива: ')
print(f'\t - Первый элемент: {first_min}\n'
      f'\t - Второй элемент: {second_min}')
