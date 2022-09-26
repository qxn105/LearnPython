def f1(a, *args):
    """args - список произвольного количества параметров """
    print(args)
    for a in args: print(a)

def f2(a, *args, **kwargs):
    """args - словарь произвольного количества параметров """
    print(args)
    print(kwargs)
    for a in kwargs: print(a)

f2('0', '1', b='111', c='222')

# import имя_модуля
# from имя_модуля import имя_функции
# from имя_модуля import имя_функции as псевдоним
# import имя_модуля as псевдоним
# from имя_модуля import *