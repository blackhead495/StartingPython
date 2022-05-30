# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

firststr = input('Введите 1 строку : ')
secstr = input('Введите 2 строку : ')

pos = 0
num = 0

while 1:
    pos = firststr.find(secstr, pos)
    print(pos)
    if pos >= 0:
        pos += 1
        num += 1
    else:
        break

print(f'Количество вхождений = {num}')
