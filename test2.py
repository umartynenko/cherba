# m = int(input('MAX количество баллов за тест: '))
# k = int(input('Количество набранных баллов: '))
# n = (k/m)*100
# if n < 50:
#     print('Отметка: 2')
# elif n >= 50 and n < 65:
#     print('Отметка: 3')
# elif n >= 65 and n < 85:
#     print('Отметка: 4')
# elif n >= 85:
#     print('Отметка: 5')

m = int(input('MAX количество баллов за тест: '))
k = int(input('Количество набранных баллов: '))


def get_grade(k, m) -> int:
    n = (k / m) * 100
    if n < 50:
        return 2
    elif 50 <= n < 65:
        return 3
    elif 65 <= n < 85:
        return 4
    elif n >= 85:
        return 5


print(f'Отметка: {get_grade(k, m)}')
