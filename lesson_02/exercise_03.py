# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

n = int(input('Введите число: '))

r = 0

while n > 0:
    pass
    r = r * 10 + n % 10
    n //= 10

print('Число обратное числу {}: {}'.format(n, r))
