# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print('Вы ввели числа: {}, {}, {}'.format(a, b, c))

if b < a < c or b > a > c:
    print('Средним из чисел {}, {}, {} является: {}'.format(a, b, c, a))
elif a < b < c or a > b > c:
    print('Средним из чисел {}, {}, {} является: {}'.format(a, b, c, b))
else:
    print('Средним из чисел {}, {}, {} является: {}'.format(a, b, c, c))