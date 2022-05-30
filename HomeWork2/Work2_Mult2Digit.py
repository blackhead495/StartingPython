# Программа, которая находит произведения пар чисел в списке.
# Парой считается первый и последний элемент, второй и предпоследний и т.д.

primer = [2, 3, 4, 2, 3, 4, 5]
ans = []

k = (len(primer) + 1) // 2

for i in range(k):
    tmp = primer[i] * primer[-(i+1)]
    ans.append(tmp)

print(primer)
print(ans)
