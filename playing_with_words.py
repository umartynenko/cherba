print("Для завершения игры укажите ' - ' вместо слова.\n")
alphabet_games = tuple(input('Введите буквы: '))
print('Алфавит игры:', alphabet_games)
print('Буквы можно использовать неоднократно.\n')
username_1 = input('Имя первого участника: ')
username_2 = input('Имя второго участника: ')
print()
list_user_1 = []
list_user_2 = []

count = 1


def check_word_alfabet(word):
    flag = True
    for i in list(word.lower()):
        if i not in alphabet_games:
            flag = False
            break
    return flag


flag = 0
while True:
    user_1 = input(f'{username_1} (ход {count}): ')
    if user_1 == '-':
        flag += 1
    elif not check_word_alfabet(user_1):
        print(f'Слово "{user_1}" не удовлетворяет условиям игры.')
    elif user_1 in list_user_1 and list_user_2:
        print(f'Слово "{user_1}" уже было.')
    else:
        list_user_1.append(user_1)

    user_2 = input(f'{username_2} (ход {count}): ')
    if user_2 == '-':
        flag += 1
    elif not check_word_alfabet(user_2):
        print(f'Слово "{user_2}" не удовлетворяет условиям игры.')
    elif user_2 in list_user_1 and list_user_2:
        print(f'Слово "{user_2}" уже было.')
    else:
        list_user_2.append(user_2)
    count += 1
    if flag > 0:
        break

print(f'Корзина слов ({user_1}): {list_user_1}')
print(f'Корзина слов ({user_2}): {list_user_2}')

if len(list_user_1) > len(list_user_2):
    print(f'{username_1.title()}, поздравляем! Вы выиграли!')
else:
    print(f'{username_2.title()}, поздравляем! Вы выиграли!')
