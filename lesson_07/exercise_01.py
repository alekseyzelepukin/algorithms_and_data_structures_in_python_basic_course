# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

from random import randint


def bubble_sort(array, ascending=True):

    if len(array) <= 1:
        return array

    n = 1

    while n < len(array):
        swap_counter = 0
        for i in range(len(array) - n):
            if ascending:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swap_counter += 1
            else:
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swap_counter += 1

        if swap_counter == 0:
            break

        n += 1

    return array


n = randint(2, 12)

array = [randint(-100, 99) for _ in range(n)]

print(f'Исходный массив:        {array}')
print(f'Отсортированный массив: {bubble_sort(array, ascending=False)}')
