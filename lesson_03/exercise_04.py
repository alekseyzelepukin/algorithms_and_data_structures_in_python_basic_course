# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

SIZE = 10

array = [randint(0, 9) for _ in range(SIZE)]

print(array)

# n = array[0]
# n_freq = 1

scores = [0 for _ in range(len(array))]

for index, i in enumerate(array):
    for j in array:
        if i == j:
            scores[index] += 1

print(scores)
