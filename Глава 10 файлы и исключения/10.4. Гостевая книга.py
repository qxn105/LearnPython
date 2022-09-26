import os
filename = 'guest_book.txt'
filename = f'{os.path.dirname(__file__)}/{filename}'

name = '.'
while name:
    name = input('Введите Асвоё имя. (Enter - выход из цикла). ')
    with open(filename, 'a', encoding='utf8') as f:
        f.write(f'{name}\n')