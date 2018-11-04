# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

SIZE = 6

array = [randint(0, 99) for _ in range(SIZE)]

print(array)

min_element = array[0]
max_element = array[0]

for element in array[1:]:
    if element < min_element:
        min_element = element
    if element > max_element:
        max_element = element

min_index = array.index(min_element)
max_index = array.index(max_element)

array[min_index], array[max_index] = max_element, min_element

print(array)
