# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

array = [0 for _ in range(8)]

for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            array[j-2] += 1

print('В диапазоне натуральных чисел от 2 до 99: ')
for index, value in enumerate(array):
    print(f'\t- числу {index+2} кратно: {value} чисел')
