# Программа находит сумму чисел списка, стоящих на нечетной позиции

primer = [5, 7, 16, 2, 22, 6, 1, 9]

summ = 0
for i in range(1, len(primer), 2):
    summ += primer[i]

print(f'{primer} => {summ}')
