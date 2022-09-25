import os
dir = os.path.dirname(__file__)
filename = f'{dir}/pi_digits.txt'

# Чтение файла целиком
# with open(filename) as file_object:
#     contents = file_object.read()
# print(contents)

# Чтение файла построчно
# with open(filename) as file_object:
#     for line in file_object:
#         print(line, end='')

# Создание списка строк по содержимому файла
# with open(filename) as file_object:
#     lines = file_object.readline()
# print(lines)
# for line in lines:
#     print(line, end='')

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string[:10]) # вывод первых 10 символов
print(len(pi_string))