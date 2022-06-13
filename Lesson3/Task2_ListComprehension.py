#lst = []

# for i in range(1, 101):
#     if(i%2 == 0):
#         lst.append(i)
#
# print(lst)

def f(x):
    return x**3

lst = [(i, f(i)) for i in range(1, 21) if i%2 == 0]
print(lst)
