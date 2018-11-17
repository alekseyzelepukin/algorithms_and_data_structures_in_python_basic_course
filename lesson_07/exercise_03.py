# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки,
# который не рассматривался на уроках.

from random import randint


def gnome_sort(array):
    if len(array) <= 1:
        return array

    i = 1

    while i < len(array):
        if i == 0 or array[i - 1] <= array[i]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1

    return array


def median_(array):
    mid = len(array) // 2
    sorted_array = gnome_sort(array.copy())
    return sorted_array[mid]


m = 5
n = 2 * m + 1
array = [randint(-100, 99) for _ in range(n)]

print(gnome_sort(array.copy()))
print(f'Медиана массива: {median_(array)}')
