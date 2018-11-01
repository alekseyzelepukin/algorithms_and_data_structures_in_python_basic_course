# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input('Введите натуральное число: '))

even_counter = 0
odd_counter = 0

while n > 0:
    if n % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
    n = n // 10

print('Количество цифр в числе {}: \n\t'
      'четных - {} \n\t'
      'нечетных - {}'.format(n, even_counter, odd_counter))
