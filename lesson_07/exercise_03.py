# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках.

from random import randint


# вариант без сортировки:
def unsorted_array_median(array):
    """
    функция возвращает медиану несортированного массива размером 2m + 1, где m – натуральное число
    """
    length = len(array)

    if length == 0:
        return None
    elif length == 1:
        return array[0]

    mid = length // 2

    for i in range(length):
        median = array[i]
        element_counter = 0
        same_element_counter = 0

        for j in range(length):
            if i != j:
                if median > array[j]:
                    element_counter += 1
                elif median == array[j]:
                    same_element_counter += 1

        if same_element_counter != 0:
            if element_counter < mid <= (element_counter + same_element_counter):
                break
        else:
            if element_counter == mid:
                break

    return median


m = 5
n = 2 * m + 1
array = [randint(-100, 99) for _ in range(n)]

# print(f'Исходный массив:      {array}')
# print(f'Сортированный массив: {sorted(array.copy())}')
print(f'Медиана массива: {unsorted_array_median(array)}')


# вариант с сортировкой:
# def gnome_sort(array):
#     if len(array) <= 1:
#         return array
#
#     i = 1
#
#     while i < len(array):
#         if i == 0 or array[i - 1] <= array[i]:
#             i += 1
#         else:
#             array[i], array[i - 1] = array[i - 1], array[i]
#             i -= 1
#
#     return array
#
#
# def sorted_array_median(array):
#     """
#     функция возвращает медиану массива (массив сортруется) размером 2m + 1, где m – натуральное число
#     """
#     length = len(array)
#
#     if length == 0:
#         return None
#     elif length == 1:
#         return array[0]
#
#     mid = length // 2
#
#     sorted_array = gnome_sort(array.copy())
#
#     return sorted_array[mid]
#
#
# m = 5
# n = 2 * m + 1
# array = [randint(-100, 99) for _ in range(n)]
#
# print(f'Исходный массив:      {array}')
# print(f'Сортированный массив: {gnome_sort(array.copy())}')
# print(f'Медиана массива: {sorted_array_median(array)}')

