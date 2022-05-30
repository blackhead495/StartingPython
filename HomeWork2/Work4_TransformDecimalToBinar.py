# Программа, которая преобразует десятичное число в двоичное

number = int(input("Введите натуральное число: "))

def TransDec2Bin(num):
    n = ""
    while num > 0:
        y = str(num % 2)
        n = y + n
        num = int(num / 2)
    return n

print(f' => 0b{TransDec2Bin(number)}')
