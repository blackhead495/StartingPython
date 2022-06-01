# Программа вычисляет число Пи с указанной точностью

# Существует много различных способов вычисленя числа Пи
# Для целей этой программы я выбрал решение по формуле Мадхавы-Лейбница:
#
#    Pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
#
import math

def calcPi (accur):
    sum = 0.0
    sign = 1
    i = 0
    while True:
        sum += 4.0 * sign / (2 * i + 1)
        i += 1
        sign = -sign
        if abs(math.pi - sum) < accur:
            return (sum)

accuracy = float(input('Введите необходимую точность вычисления : '))
print(f'Число Пи из библиотеки math =    {math.pi}')
print(f'Число Пи с указанной точностью = {calcPi(accuracy)}')

