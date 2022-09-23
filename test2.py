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

title = 'Для выхода из программы введите "-".'
print('#' * len(title))
print(title)
print('#' * len(title))
print()


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


m = int(input('MAX количество баллов за тест: '))

dict_students = {}
while True:
    name = input('Введите ФИО учащегося: ').title().strip()
    if name == '-':
        break
    else:
        k = int(input('Количество набранных баллов: '))
        dict_students[name] = get_grade(m, k)

list_user_name = [i for i in dict_students.keys()]
list_user_name.sort()

while True:
    q = input('\nВывести оценки учеников? (+/-): ')
    if q == '+':
        print('-' * 50)
        for i in list_user_name:
            print(f'{i}: {dict_students[i]}')
            break
    elif q.isalpha() or q.isdigit() or q in '!@#$%^&*()?|~`"':
        print('Вы ввели невероне значение!')
        continue
    else:
        print('-' * 50)
        break
