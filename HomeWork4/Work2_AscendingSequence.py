# Дан список чисел.
# Создать список в который попадают числа, описывающие возрастающую последовательность и
# содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#       [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

import random

N = 20  # Количество случайных чисел
lst = []    # Пустой список

for i in range(N):
    lst.append(random.randint(0, 100))

#print(lst)

numbers = []    # Длина последовательностей
count = 0       # Счетчик для вычисления длины последовательностей

for i in range(N-1):
    count = 0
    j = i
    k = 1
    while (j + k) < N:
        while k < (N - j):
            if lst[j] < lst[j+k]:
                count += 1
                j += k
                k = 1
                break
            k += 1

    numbers.append(count)
#print(numbers)

max_number = max(numbers)
#print(max_number)

max_index = numbers.index(max(numbers))
#print(max_index)

ans = []
i = 1
m = max_index
ans.append(lst[m])
while (i + m) < N:
    if (lst[m] < lst[m + i]):
        m += i
        i = 0
        ans.append(lst[m])
    i += 1

#print(ans)
print(lst, ' => ', ans)

