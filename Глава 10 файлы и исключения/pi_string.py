import os
dir = os.path.dirname(__file__)
filename = f'{dir}/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

my_birthday = '120372'
say = 'есть' if my_birthday in pi_string else 'нет'
print(f'В первом миллионе числа pi {say} {my_birthday}!')
