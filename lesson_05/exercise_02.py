# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque, defaultdict


def hex_sum(a, b):
    digit_number_a = len(a)
    digit_number_b = len(b)
    digit_number_diff = abs(digit_number_a - digit_number_b)

    deq_a = deque(a)
    deq_b = deque(b)

    if digit_number_a > digit_number_b:
        deq_b.extendleft('0' for _ in range(digit_number_diff))
    elif digit_number_b > digit_number_a:
        deq_a.extendleft('0' for _ in range(digit_number_diff))

    deq_a.reverse()
    deq_b.reverse()

    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    dec2hex = defaultdict(str)
    hex2dec = defaultdict(int)

    for index, value in enumerate(hex_digits):
        dec2hex[index] = value
        hex2dec[value] = index

    hex_sum = deque()
    dec_sum = 0
    digit = 0
    boost = 0

    for i, j in zip(deq_a, deq_b):
        dec_sum = hex2dec[i] + hex2dec[j]
        digit = dec_sum % 16
        if dec_sum // 16 > 0:
            boost = 1
            hex_sum.appendleft(dec2hex[digit])
        else:
            digit += boost
            boost = 0
            hex_sum.appendleft(dec2hex[digit])

    return list(hex_sum)


print(hex_sum('A2', 'C4F'))
