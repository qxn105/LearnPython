import os
filename = 'guest.txt'
dir = os.path.dirname(__file__)
filename = f'{dir}/{filename}'

with open(filename, 'w', encoding='utf8') as f:
    f.write(F'Ваше имя: {input("Введите своё имя: ")}')