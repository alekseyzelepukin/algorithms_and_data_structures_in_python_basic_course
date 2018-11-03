# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

SIZE = 10

array = [randint(0, 9) for _ in range(SIZE)]

print(array)

mode = array[0]
mode_freq = 1

for i in range(len(array) - 1):
    freq = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            freq += 1
        if freq > mode_freq:
            mode_freq = freq
            mode = array[i]

print(f'Число {mode} встречается в массиве {mode_freq} раз(а)')
