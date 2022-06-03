# Программа, которая получает список неповторяющихся элементов из исходной последовательности
#  Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

# numbers = [1, 2, 3, 5, 1, 5, 3, 10]
numbers = [2, 3, 3, 33, 5, 3, 33, 2, 16]

def getUniqueNumbers(num):
    unique = []

    for number in num:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(numbers, ' => ', getUniqueNumbers(numbers))