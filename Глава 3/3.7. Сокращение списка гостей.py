# только что выяснилось, что новый обеденный стол привезти вовремя не успеют и места хватит только для двух гостей.
#   • Начните с программы из упражнения 3.6. Добавьте команду для вывода сообщения о том, что на обед приглашаются всего два гостя.
#   • Используйте метод pop() для последовательного удаления гостей из списка до тех пор, пока в списке не останутся только два человека. 
#       Каждый раз, когда из списка удаляется очередное имя, выведите для этого человека сообщение о том, что вы сожалеете об отмене приглашения
#   • Выведите сообщение для каждого из двух человек, остающихся в списке. Сообщение должно подтверждать, что более раннее приглашение остается в силе.
#   • Используйте команду del для удаления двух последних имен, чтобы список остался пустым. 
#       Выведите список, чтобы убедиться в том, что в конце работы программы список действительно не содержит ни одного элемента.
from queue import Empty

guests = ['Alexandr', 'Pavel', 'Ilya', 'Artem']
for guest in guests:
    print(f'{guest.title()}, I would like to invite you on my party at 10th november.')

print("\nWe extendet the list of guests.\n")
guests.insert(0, 'oleg')
guests.insert(2, 'Anna')
guests.append('Valya')

for guest in guests:
    print(f'{guest.title()}, I would like to invite you on my party at 10th november.')

print("\nWe must shrink the list of guests to 2 persons.\n")

while  len(guests) != 2:
    print(f"{guests.pop(2).title()}, I'm sorry for cancele your invitation on my party.")

print()
for guest in guests:
    print(f'{guest.title()}, I happy to approve your invitation on my party at 10th november.')

while  len(guests) != 0:
    del guests[0]

print(f"\nSize of guest list is {len(guests)}")
for guest in guests:
    print(f'{guest.title()}, I would like to invite you on my party at 10th november.')
