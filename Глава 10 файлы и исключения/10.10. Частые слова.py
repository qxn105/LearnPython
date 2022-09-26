#  зайдите на сайт проекта «Гутенберг» (http://gutenberg.org/) и найдите 
# несколько книг для анализа. Загрузите текстовые файлы этих произведений или 
# скопируйте текст из браузера в текстовый файл на вашем компьютере.
# Для подсчета количества вхождений слова или выражения в строку можно 
# воспользоваться методом count(). 
# Например, следующий код подсчитывает количество вхождений 'row' в строке:
# >>> line = "Row, row, row your boat" 
# >>> line.count('row') 
# 2 
# >>> line.lower().count('row')
# 3 
# Обратите внимание: преобразование строки к нижнему регистру функцией lower() 
# позволяет найти все вхождения искомого слова независимо от регистра.

# Напишите программу, которая читает файлы из проекта «Гутенберг» и определяет 
# количество вхождений слова 'the' в каждом тексте. 
# Результат будет приближенным, потому что программа также будет учитывать такие 
# слова, как 'then' и 'there'. Попробуйте повторить поиск для строки 'the ' 
# (с пробелом в строке) и посмотрите, насколько уменьшится количество найденных результатов.

import os
dir = os.path.dirname(__file__)
book_list = ['siddhartha.txt', 'alice.txt', 'moby_dick.txt', 'little_women.txt']

def count_word(filename, word):
    try:
        with open(dir+'/'+filename, 'r', encoding='utf8') as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        count = content.lower().count(word+" ")
        print(f'In file "{filename}" word "{word}" met {count} times.')

for book in book_list: 
    count_word(filename=book, word='the')