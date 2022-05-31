# Программа, которая находит наименьшее общее кратное двух чисел

def lmc(a, b):
    c = a * b
    while a and b:
        if a > b: a %= b
        else:     b %= a
    return c // (a + b)

num1 = int(input('Введите первое число : '))
num2 = int(input('Введите второе число : '))
print(f'НОК двух чисел = {lmc(num1, num2)}')
