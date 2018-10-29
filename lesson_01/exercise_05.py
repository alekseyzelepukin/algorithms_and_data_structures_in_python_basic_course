# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter_1 = input('Введите первую букву [a-z]: ')
letter_2 = input('Введите вторую букву [a-z]: ')

print('Вы ввели буквы: {}, {}'.format(letter_1, letter_2))

pos_1 = ord(letter_1) - ord('a') + 1
pos_2 = ord(letter_2) - ord('a') + 1

if pos_1 == pos_2:
    char_num = 0
else:
    char_num = abs(pos_2 - pos_1) - 1

print('Место буквы {} в алфавите: {}'.format(letter_1, pos_1))
print('Место буквы {} в алфавите: {}'.format(letter_2, pos_2))
print('Количесвто символов между буквами {} и {}: {} '.format(letter_1, letter_2, char_num))
