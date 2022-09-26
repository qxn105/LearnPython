s = {1:'123',2:'456',3:'789'}
print('s:', s)
print('s.items():\t', s.items())
print('s.keys():\t',s.keys())
print('s.values():\t',s.values())

print('for a in s:  а = ключ каждого жлемента словаря')
for a in s:
    print('\t', a, end='')
print()

print('for a in s.keys():  а = ключ каждого жлемента словаря')
for a in s.keys():
    print('\t', a, end='')
print()

print('for a in s.items():  а = кортедж пар (ключ, значение) каждого жлемента словаря')
for a in s.items():
    print('\t', a, end='')
print()

print('for a,b  in s.items():  а = ключ, b = значение для каждого жлемента словаря')
for a, b in s.items():
    print('\t', a, b, end='')
print()

print('for a  in s.values():  а = значение для каждого жлемента словаря')
for a in s.values():
    print('\t', a, end='')
print()

for a, b, c in s.values():
    print(f'\t{a} {b} {c}', end='')
print()

# множества содержат кникальные элементы
# множество - частный случай словаря (ключи без значений). 
# создается либо командой set(список) 
# либо {'елем1', 'елем2', ...}