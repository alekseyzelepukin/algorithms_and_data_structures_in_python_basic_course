# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

# https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B9_%D0%B3%D0%BE%D0%B4
# Отсюда следует распределение високосных годов:
#
#     год, номер которого кратен 400, — високосный;
#     остальные годы, номер которых кратен 100, — невисокосные;
#     остальные годы, номер которых кратен 4, — високосные.

year = int(input('Введите год: '))

print('Вы ввели: {}'.format(year))

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print('Год {} является обычным'.format(year))
else:
    print('Год {} является високосным'.format(year))
