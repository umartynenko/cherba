exc_students = sorted(list())
good_students = sorted(list())

while True:
    classroom = input('Класс: ').strip()
    print("Чтобы закончить ввод в поле 'Фамилия И.О.:' укажите '-'.\n")
    while True:
        name = input('Фамилия И.О.: ').strip()
        if name == '-':
            break
        else:
            algebra = int(input('Алгебра: '))
            physics = int(input('Физика: '))
            russian = int(input('Русский: \n'))
            if (algebra + physics + russian) // 3 == 5:
                exc_students.append(name)
            elif (algebra + physics + russian) // 3 == 4:
                good_students.append(name)
    print('Отличники:')
    if len(exc_students) == 0:
        print('-')
    else:
        for i in exc_students:
            print(i)
    print('\nХорошисты:')
    if len(good_students) == 0:
        print('-')
    else:
        for i in good_students:
            print(i)
    q_classroom = input('\nВвести данные другого класса?(+/-): \n')
    print()
    if q_classroom == '-':
        break
    else:
        # Очищаем списки
        exc_students.clear()
        good_students.clear()
