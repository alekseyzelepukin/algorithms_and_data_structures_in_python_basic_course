# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
        print('Введите знак операции [+, -, *, /] для продолжения работы или 0 для выхода из программы: ')
        sign = input('Знак операции: ')
        if sign == '0':
            print('Завершение работы программы.')
            break
        if sign == '+' or sign == '-' or sign == '*' or sign == '/':
                print('Введите числа a и b: ')
                a = float(input('a = '))
                b = float(input('b = '))
                if sign == '+':
                    print('a {} b = {}'.format(sign, a + b))
                elif sign == '-':
                    print('a {} b = {}'.format(sign, a - b))
                elif sign == '*':
                    print('a {} b = {}'.format(sign, a * b))
                elif sign == '/':
                        if b != 0:
                            print('a {} b = {}'.format(sign, a / b))
                        else:
                            print('Деление на ноль невозможно. Попробуйте еще раз!')
        else:
                print('Вы ввели несуществующий знак операции. Попробуйте еще раз!')
