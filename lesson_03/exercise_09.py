# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

M = 3
N = 4

matrix = [[randint(0, 9) for _ in range(N)] for _ in range(M)]

print(f'Матрица {M} x {N}: ')
for i in range(M):
    for j in range(N):
        print(matrix[i][j], end=' ')
    print()
print()

array = [0 for _ in range(N)]

min_element = None

for j in range(N):
    min_element = matrix[0][j]
    for i in range(M):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
        array[j] = min_element

max_element = array[0]

for element in array[1:]:
    if element > max_element:
        max_element = element

print(f'Максимальный элемент: {max_element}')
