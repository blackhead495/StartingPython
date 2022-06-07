#  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

f = open('test.txt', 'r+')  # Открыть файл для чтения - записи

st = f.read()               # Извлечь данные из файла в строку
print(st)

List = list(st.split())     # Разделить данные по пробелу и создать список строк
print(List)

numList = list(map(int, List))  # Преобразовать список строк с список int
print(numList)

newStr = ''  # Создать пустой список
for i in range(len(numList)):
    if numList[i] % 2 == 0:  # Если число нечетное - добавить его в новый список
        newStr += str(numList[i]) + ' '

print(newStr)

f.truncate(0)       # Очистить файл
f.seek(0)           # Перейти в начало
f.write(newStr)     # Записать новую строку

f.close()
