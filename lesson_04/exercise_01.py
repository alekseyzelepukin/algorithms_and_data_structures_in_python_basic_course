# 1. Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.

# Алгоритм 1 (lesson_03/exercise_06)
# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
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
    array = [randint(0, 9) for _ in range(size)]
    x = sum_between_extremum(array)
    return x


# воспользуемся timeit:
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main(10)"
# 100 loops, best of 3: 13 usec per loop
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main(100)"
# 100 loops, best of 3: 117 usec per loop
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main(1000)"
# 100 loops, best of 3: 1.19 msec per loop


# воспользуемся cProfile:
# print(cProfile.run('main(1000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          5586 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 exercise_01.py:12(sum_between_extremum)
#         1    0.000    0.000    0.002    0.002 exercise_01.py:38(main)
#         1    0.000    0.000    0.002    0.002 exercise_01.py:39(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:173(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:217(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1580    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
# None
#
# Process finished with exit code 0

# print(cProfile.run('main(10000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          55910 function calls in 0.021 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.021    0.021 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 exercise_01.py:12(sum_between_extremum)
#         1    0.000    0.000    0.021    0.021 exercise_01.py:38(main)
#         1    0.002    0.002    0.020    0.020 exercise_01.py:39(<listcomp>)
#     10000    0.007    0.000    0.015    0.000 random.py:173(randrange)
#     10000    0.003    0.000    0.018    0.000 random.py:217(randint)
#     10000    0.006    0.000    0.008    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.021    0.021 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     15904    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
# None
#
# Process finished with exit code 0

# print(cProfile.run('main(100000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          560151 function calls in 0.236 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.236    0.236 <string>:1(<module>)
#         1    0.013    0.013    0.013    0.013 exercise_01.py:12(sum_between_extremum)
#         1    0.000    0.000    0.236    0.236 exercise_01.py:38(main)
#         1    0.024    0.024    0.223    0.223 exercise_01.py:39(<listcomp>)
#    100000    0.073    0.000    0.167    0.000 random.py:173(randrange)
#    100000    0.032    0.000    0.199    0.000 random.py:217(randint)
#    100000    0.064    0.000    0.094    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.236    0.236 {built-in method builtins.exec}
#    100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    160145    0.023    0.000    0.023    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
# None
#
# Process finished with exit code 0


# попробуем изменить алгоритм:

def sum_between_extremum2(input_array):

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
        for index, value in enumerate(input_array):
            if start < index < end:
                total += value

        return total


def main2(size=10):
    array = [randint(0, 9) for _ in range(size)]
    x = sum_between_extremum2(array)
    return x


# воспользуемся timeit:
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main2(10)"
# 100 loops, best of 3: 14.4 usec per loop
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main2(100)"
# 100 loops, best of 3: 125 usec per loop
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main2(1000)"
# 100 loops, best of 3: 1.37 msec per loop


# воспользуемся cProfile:
# print(cProfile.run('main2(1000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          5573 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 exercise_01.py:129(sum_between_extremum2)
#         1    0.000    0.000    0.002    0.002 exercise_01.py:156(main2)
#         1    0.000    0.000    0.002    0.002 exercise_01.py:157(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:173(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:217(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1567    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
# None
#
# Process finished with exit code 0

# print(cProfile.run('main2(10000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          56014 function calls in 0.020 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.020    0.020 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 exercise_01.py:129(sum_between_extremum2)
#         1    0.000    0.000    0.020    0.020 exercise_01.py:156(main2)
#         1    0.002    0.002    0.019    0.019 exercise_01.py:157(<listcomp>)
#     10000    0.006    0.000    0.014    0.000 random.py:173(randrange)
#     10000    0.003    0.000    0.017    0.000 random.py:217(randint)
#     10000    0.005    0.000    0.008    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.020    0.020 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     16008    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
# None
#
# Process finished with exit code 0

# print(cProfile.run('main2(100000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          560192 function calls in 0.219 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.219    0.219 <string>:1(<module>)
#         1    0.017    0.017    0.017    0.017 exercise_01.py:129(sum_between_extremum2)
#         1    0.000    0.000    0.219    0.219 exercise_01.py:156(main2)
#         1    0.021    0.021    0.202    0.202 exercise_01.py:157(<listcomp>)
#    100000    0.068    0.000    0.152    0.000 random.py:173(randrange)
#    100000    0.029    0.000    0.180    0.000 random.py:217(randint)
#    100000    0.057    0.000    0.084    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.219    0.219 {built-in method builtins.exec}
#    100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    160186    0.020    0.000    0.020    0.000 {method 'getrandbits' of '_random.Random' objects}
#
#
# None
#
# Process finished with exit code 0


# выводы:
# алгоритм является простым sum_between_extremum и sum_between_extremum2
# алгоритм sum_between_extremum достаточно быстрый чтобы его использовать,
# так как в аглоритме отсутствует рекурсия, лишних запусков функции не происходит
# по линейному увеличению времени tottime можно сделать предположение что алгоритм имеет сложность O(N)
# по замерам timeit и tottime, кажется что измененный алгоритм sum_between_extremum2
# ведет себя немного хуже, но нельзя исключать случайного фактора на столь малом количестве замеров
# таким образом с помощью timeit и cProfile можно сравнить разные реализации алгоритма
# и выбрать наиболее быстродейственный


# Алгоритм 2 (lesson_03/exercise_03)
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def swap_extremum(input_array):

    min_element = input_array[0]
    max_element = input_array[0]

    for element in input_array[1:]:
        if element < min_element:
            min_element = element
        if element > max_element:
            max_element = element

    min_index = input_array.index(min_element)
    max_index = input_array.index(max_element)

    input_array[min_index], input_array[max_index] = max_element, min_element

    return input_array


def main3(size=10):
    array = [randint(0, 99) for _ in range(size)]
    x = swap_extremum(array)
    return x


# воспользуемся timeit:
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main3(10)"
# 100 loops, best of 3: 12.1 usec per loop
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main3(100)"
# 100 loops, best of 3: 118 usec per loop
# >python -m timeit -n 100 -s "import exercise_01" "exercise_01.main3(1000)"
# 100 loops, best of 3: 1.18 msec per loop


# воспользуемся cProfile:
# print(cProfile.run('main3(1000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          5277 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 exercise_01.py:254(swap_extremum)
#         1    0.000    0.000    0.002    0.002 exercise_01.py:273(main3)
#         1    0.000    0.000    0.002    0.002 exercise_01.py:274(<listcomp>)
#      1000    0.001    0.000    0.001    0.000 random.py:173(randrange)
#      1000    0.000    0.000    0.002    0.000 random.py:217(randint)
#      1000    0.000    0.000    0.001    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1269    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
#
# None
#
# Process finished with exit code 0

# print(cProfile.run('main3(10000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          52857 function calls in 0.023 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.023    0.023 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 exercise_01.py:254(swap_extremum)
#         1    0.000    0.000    0.023    0.023 exercise_01.py:273(main3)
#         1    0.002    0.002    0.022    0.022 exercise_01.py:274(<listcomp>)
#     10000    0.008    0.000    0.017    0.000 random.py:173(randrange)
#     10000    0.003    0.000    0.020    0.000 random.py:217(randint)
#     10000    0.006    0.000    0.009    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.023    0.023 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12849    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
#
# None
#
# Process finished with exit code 0

# print(cProfile.run('main3(100000)'))
# C:\Users\DELL\Anaconda3\python.exe C:/Users/DELL/PycharmProjects/algorithms_and_data_structures_in_python_basic_course/lesson_04/exercise_01.py
#          528029 function calls in 0.204 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.204    0.204 <string>:1(<module>)
#         1    0.005    0.005    0.005    0.005 exercise_01.py:254(swap_extremum)
#         1    0.000    0.000    0.203    0.203 exercise_01.py:273(main3)
#         1    0.022    0.022    0.198    0.198 exercise_01.py:274(<listcomp>)
#    100000    0.068    0.000    0.146    0.000 random.py:173(randrange)
#    100000    0.030    0.000    0.176    0.000 random.py:217(randint)
#    100000    0.054    0.000    0.078    0.000 random.py:223(_randbelow)
#         1    0.000    0.000    0.204    0.204 {built-in method builtins.exec}
#    100000    0.007    0.000    0.007    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    128021    0.017    0.000    0.017    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
#
# None
#
# Process finished with exit code 0

# выводы:
# алгоритм является простым
# так как в алгоритме отсутствует рекурсия, лишних вызовов функции не происходит
