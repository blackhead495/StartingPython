data = [x for x in range(10)]

res = list(filter(lambda x: not x % 2, data))
print(res)

data2 = '1 2 3 5 8 15 23 38'.split()

res2 = map(int, data2)
res2 = filter(lambda x: not x % 2, res2)
res2 = list(map(lambda x: (x, x**2), res2))
print(res2)