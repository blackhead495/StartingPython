# Программа, которая вычисляет  список простых множителей натурального числа N

def findPrimeFactors(num):
    factors = []
    d = 2
    m = num
    while d * d <= m:
        if m % d == 0:
            factors.append(d)
            m //= d
        else:
            d += 1
    factors.append(m)  # Добавить последнеё простое число
    return factors


n = int(input("Введите натуральное число: "))
print('{0} = {1}' .format(n, findPrimeFactors(n))) 