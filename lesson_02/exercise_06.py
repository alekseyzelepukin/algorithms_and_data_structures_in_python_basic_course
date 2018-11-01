# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.

from random import randint

rn = randint(0, 100)

print('Попробуйте отгадать загаданное целое число [0, 100] за 10 попыток: ')

i = 0
while i < 10:
    n = int(input('Попытка #{:2d}: '.format(i + 1)))
    if n == rn:
        print('Поздравляю! Вы отгадали число с {:2d} попытки.'.format(i + 1))
        break
    elif n > rn:
        print('Число {:3d} больше загаданногою'.format(n))
    else:
        print('Число {:3d} меньше загаданногою'.format(n))
    i += 1
else:
    print('Вы не отгадали число за 10 попыток. \n'
          'Загаданное число: {:3d}'.format(rn))
