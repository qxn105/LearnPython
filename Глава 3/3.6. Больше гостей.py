# вы решили купить обеденный стол большего размера. Дополнительные места позволяют пригласить на обед еще трех гостей.
#   • Начните с программы из упражнения 3.4 или 3.5. Добавьте в конец программы команду print, которая выводит сообщение о расширении списка гостей.
#   • Добавьте вызов insert() для добавления одного гостя в начало списка.
#   • Добавьте вызов insert() для добавления одного гостя в середину списка.
#   • Добавьте вызов append() для добавления одного гостя в конец списка.
#   • Выведите новый набор сообщений с приглашениями — по одному для каждого участника, входящего в список.

guests = ['Alexandr', 'Pavel', 'Ilya', 'Artem']
for guest in guests:
    print(f'{guest.title()}, I would like to invite you on my party at 10th november.')

print("\nWe extendet the list of guests.\n")
guests.insert(0, 'oleg')
guests.insert(2, 'Anna')
guests.append('Valya')

for guest in guests:
    print(f'{guest.title()}, I would like to invite you on my party at 10th november.')
