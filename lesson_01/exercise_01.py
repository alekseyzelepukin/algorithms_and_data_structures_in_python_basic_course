# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input('Введите трехзначное число: '))

print('Вы ввели число:', n)

h = n // 100
t = n // 10 % 10
u = n % 10

print('Сумма цифр:', h + t + u)
print('Произведение цифр:', h * t * u)
