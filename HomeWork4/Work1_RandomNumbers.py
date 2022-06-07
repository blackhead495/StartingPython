# Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.

import random

def sorting(lowLimit, highlimit, number):
    x = []
    for i in range(number):
        x.append(random.randint(lowLimit, highlimit))
    print(x)

    x.sort()
    print(x)

a = int(input('Введите нижнюю границу : '))
b = int(input('Введите верхнюю границу : '))
c = int(input('Введите количество элементов : '))

sorting(a, b, c)


