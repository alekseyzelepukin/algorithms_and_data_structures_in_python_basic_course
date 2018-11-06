# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

# Алгоритм 1 (lesson_03/exercise_06)
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
import timeit
import cProfile


def sum_between_extremum(input_array):

    min_index = 0
    max_index = 0

    for index, element in enumerate(input_array):
        if element < input_array[min_index]:
            min_index = index
        if element > input_array[max_index]:
            max_index = index

    if min_index == max_index:
        return 0
    else:
        start, end = min_index, max_index

        if end < start:
            start, end = end, start

        total = 0
        for value in input_array[start+1:end]:
            total += value

        return total


def main(size=10):
    array = [randint(0, 9) for _ in range(10)]
    x = sum_between_extremum(array)
    return x


print(timeit.timeit('main()', number=100))
