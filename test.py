# def max(l):
#     max = 0
#     r = 0
#
# for i in range(len(l)):
#     for j in range(len(l[0])):
#         if l[i][j] > max:
#             max = l[i][j]
#
# for i in range(len(l)):
#     for j in range(len(l[0])):
#         if l[i][j] = max:
#             r = '(' + i + ';' + j + ')'
#             print('Максимальный элемент:', max)
#             return r
#
# n = int(input('Количество строк матрицы: '))
# m = int(input('Количество столбцов матрицы: '))
# h = []
#
# for i in range(n):
#     h.append([])
#     c = input()
#     h[i] = c.split(' ')
# for i in range(n):
#     for j in range(m):
#         h[i][j] = int(h[i][j])
# print(max(l))
## Пример правильного вывода:
## Количество строк матрицы: 3
## Количество столбцов матрицы: 5
## 1 4 -9 3 2
## 6 3 9 1 2
## 9 0 5 8 -11
## Максимальный элемент: 9
## (2;3)

def max(l):
    max = 0
    r = 0
    for i in range(len(l)):
        for j in range(len(l[0])):
            if int(l[i][j]) > max:
                max = l[i][j]

    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] == max:
                r = '(' + str(i + 1) + ';' + str(j + 1) + ')'
                print('Максимальный элемент:', max)
                return r


n = int(input('Количество строк матрицы: '))
m = int(input('Количество столбцов матрицы: '))
h = []

for i in range(n):
    h.append([])
    c = input()
    h[i] = c.split(' ')

for i in range(n):
    for j in range(m):
        h[i][j] = int(h[i][j])

print(max(h))
