# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

from random import randint

M = 5
N = 4

matrix = [[None for _ in range(N)] for _ in range(M)]

row_sum = 0

for i in range(M):
    row_sum = 0
    for j in range(N - 1):
        n = int(input('Введите число: '))
        # n = randint(0, 9)  # для тестирования: имитация ручного ввода
        row_sum += n
        matrix[i][j] = n
    matrix[i][N - 1] = row_sum

print(f'Матрица {M} x {N}: ')
for i in range(M):
    for j in range(N):
        print(matrix[i][j], end=' ')
    print()
print()
