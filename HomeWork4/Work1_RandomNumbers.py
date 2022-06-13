# Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.

from random import randint

lst = [randint(0, 100) for i in range(20)]
print(lst)

f = open("RandomNum.txt", 'w')
f.write(' '.join(map(str, lst)))
f.close()

lst = []
f = open("RandomNum.txt", 'r')
rd = f.read()
lst = list(map(int, rd.split()))
lst.sort()
f.close()

f = open("RandomNum.txt", 'w')
f.write(' '.join(map(str, lst)))
f.close()

