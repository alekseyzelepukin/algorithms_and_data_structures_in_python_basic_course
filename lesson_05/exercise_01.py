# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
# Примечание: 4 квартала - это 4 разных прибыли ;-)

from collections import defaultdict
# from random import randint


n = int(input('Введите количество предприятий: '))

# n = randint(0, 9)

while n < 1:
    print('Число предприятий должно быть положительным. Попробуйте еще раз!')
    n = int(input('Введите количество предприятий: '))

annual_statement = defaultdict(float)

annual_income = 0
total_income = 0

company = None
income = 0

for i in range(n):
    company = input(f'Введите название предприятия #{i + 1}: ')
    # company = 'Company_' + str(i)
    annual_income = 0
    for j in range(4):
        income = float(input(f'Введите выручку за квартал #{j + 1} предприятия {company}: '))
        # income = randint(-999, 999)
        annual_income += income
        total_income += income
    annual_statement[company] = annual_income

average_income = total_income / n

above_average = []
below_average = []

if n == 1:
    print(f'Колчество предприятий: {n}.\n'
          f'Невозможно определить предприятия с прибылью выше или ниже средней.\n'
          f'Введите больше предприятий для сравнения.')
else:
    for company, income in annual_statement.items():
        if income > average_income:
            above_average.append(company)
        elif income < average_income:
            below_average.append(company)
    if len(above_average) > 0 and len(below_average) > 0:
        print(f'Колчество предприятий: {n}')
        print(f'Средняя прибыль: {average_income}')
        print('Компании с прибылью выше средней: {}'.format(', '.join(above_average)))
        print('Компании с прибылью ниже средней: {}'.format(', '.join(below_average)))
    else:
        print(f'Колчество предприятий: {n}.\n'
              f'Невозможно определить предприятия с прибылью выше или ниже средней.\n'
              f'Прибыль предприятий совпадает.')
