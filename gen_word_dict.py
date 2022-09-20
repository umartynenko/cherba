title = "Чтобы закончить ввод, в поле 'Введите слово:' укажите '-'."
print("#" * (len(list(title))))
print(title)
print("#" * (len(list(title))))
print()

dict_word = {}
id_word = 1
while True:
    word = input('Введите слово: ')
    if word == '-':
        break
    else:
        for _ in range(len(dict_word)+1):
            if (str(len(list(word)))+'-'+str(id_word)) in dict_word:
                id_word += 1
        dict_word[str(len(list(word)))+'-'+str(id_word)] = word
        print(f'Слову "{word}" присвоен ключ {len(list(word))}-{id_word}\n')
        id_word = 1

list_key = list(dict_word.keys())
list_key.sort()
print('Словарь:')
for i in list_key:
    print(i, ':', dict_word[i])
print('\nОбщее количество слов в словаре:', len(dict_word))