# Программа, которая находит разницу между максимальной и минимальной дробными частями
# в заданном списке вещественных чисел

# Primer =  [1.1, 1.2, 3.1, 5.0, 10.01]
Primer = [6.25, 4.1, 55.55, 78.99]

def findDiff (lst):
    ans = []
    for i in range (len(lst)):
        tmp = lst[i] - int(lst[i])
        ans.append(tmp)
    return (max(ans) - min(ans))

print(f'Разница дробных частей составляет {findDiff(Primer)}')
