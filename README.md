# cherba

****exc_or_good.py**:** Программа определяет отличников и хорошистов по
введенным оценкам для неограниченного количества классов и выводит их в
отсортированном порядке.

**playing_with_words.py:** Небольшая игра в слова для двух человек

**gen_word_dict.py:** Программа генерирует ключи для словаря согласно шаблону
для каждого нового слова, введенного пользователем с клавиатуры, затем выводит
все значения отсортированного по ключам словаря и общее количество слов.

**test.py** Учащийся написал программу, которая вычисляет индекс
первого вхождения максимального элемента матрицы (количе-
ство строк, столбцов, а также элементы матрицы вводятся поль-
зователем самостоятельно). Найдите и исправьте допущенные
в коде ошибки.
def max(l):
max = 0
r = 0
for i in range(len(l)):
for j in range(len(l[0])):
if l[i][j] > max:
max = l[i][j]Практикум
for i in range(len(l)):
for j in range(len(l[0])):
if l[i][j] = max:
r = '('+i+';'+j+')'
print('Максимальный элемент:', max)
return r
n = int(input('Количество строк матрицы: '))
m = int(input('Количество столбцов матрицы: '))