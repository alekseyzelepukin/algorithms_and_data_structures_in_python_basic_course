# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.

import numpy as np
import itertools
import math
import cProfile


def sieve(p):
    if p == 0:
        return
    elif p == 1:
        return 2
    else:
        n = 100
        while True:
            if p < n / np.log(n):
                break
            else:
                n += 100

        numbers = [i for i in range(n)]
        numbers[1] = 0
        for i in range(2, n):
            if numbers[i] != 0:
                j = i + i
                while j < n:
                    numbers[j] = 0
                    j += i

        prime_numbers = [i for i in numbers if i != 0]

        return prime_numbers[p - 1]


def brute(p):
    if p == 0:
        return
    elif p == 1:
        return 2
    else:
        prime_numbers = []
        for i in itertools.count(start=2, step=1):
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
                if len(prime_numbers) == p:
                    return prime_numbers[p - 1]


# sieve timeit:
# >python -m timeit -n 100 -s "import exercise_02" "exercise_02.sieve(100)"
# 100 loops, best of 3: 191 usec per loop
# >python -m timeit -n 100 -s "import exercise_02" "exercise_02.sieve(1000)"
# 100 loops, best of 3: 2.88 msec per loop
# >python -m timeit -n 100 -s "import exercise_02" "exercise_02.sieve(10000)"
# 100 loops, best of 3: 48.7 msec per loop


# sieve cProfile:
# cProfile.run('sieve(100)')
#         1    0.000    0.000    0.000    0.000 exercise_02.py:11(sieve)
# cProfile.run('sieve(1000)')
#         1    0.003    0.003    0.003    0.003 exercise_02.py:11(sieve)
# cProfile.run('sieve(10000)')
#         1    0.044    0.044    0.056    0.056 exercise_02.py:11(sieve)


# brute timeit:
# >python -m timeit -n 100 -s "import exercise_02" "exercise_02.brute(100)"
# 100 loops, best of 3: 454 usec per loop
# >python -m timeit -n 100 -s "import exercise_02" "exercise_02.brute(1000)"
# 100 loops, best of 3: 9.31 msec per loop
# >python -m timeit -n 100 -s "import exercise_02" "exercise_02.brute(10000)"
# 100 loops, best of 3: 220 msec per loop


# brute cProfile:
# cProfile.run('brute(100)')
#         1    0.001    0.001    0.002    0.002 exercise_02.py:38(brute)
# cProfile.run('brute(1000)')
#         1    0.012    0.012    0.013    0.013 exercise_02.py:38(brute)
# cProfile.run('brute(10000)')
#         1    0.237    0.237    0.255    0.255 exercise_02.py:38(brute)


# выводы:
# исходя из проведенных замеров, можно сделать вывод,
# что алгоритм с использованием Решета Эратосфена работает существенно быстрее,
# чем алгоритм, основанный на переботе чисел и его делителей каждого числа
# в реальной практике, для получения p-го простого числа я бы предпочел использовать Решето Эратосфена
# или модификации алгоритма на основе Решета Эратосфена
