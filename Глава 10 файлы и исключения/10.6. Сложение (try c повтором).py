# при вводе числовых данных часто встречается типичная проблема: 
# пользователь вводит текст вместо чисел. 
# При попытке преобразовать данные в int происходит исключение ValueError. 
# Напишите программу, которая запрашивает два числа, складывает их и выводит результат. 
# Перехватите исключение ValueError, если какое-либо из входных значений не 
# является числом, и выведите удобное сообщение об ошибке. 
# Протестируйте свою программу: сначала введите два числа, а потом введите текст вместо 
# одного из чисел.


def input_digit(msg='Введите первое число:', retries = 0):
    if retries > 2: return
    try:
        dig = input(msg)
        if dig == '': return None
        dig = int(dig)
    except:
        dig = input_digit(msg, retries + 1)
    return dig

while 1:
    print('Для выхода, просто нажмите Enter.')
    first = input_digit(msg='Введите первое число:')
    if not first: break
    second = input_digit(msg='Введите второе число:')
    if not second: break
    print(f'{first} + {second} = {first + second}')
