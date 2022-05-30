str = input('Введите вещественное число : ')

str = str.replace('.', '')
str = str.replace(',', '')

if str.isnumeric():
    num = int(str)
    summ = 0

    for i in range(len(str)):
        summ += num % 10
        num //= 10

    print(summ)
else:
    print('Введено не число!')
