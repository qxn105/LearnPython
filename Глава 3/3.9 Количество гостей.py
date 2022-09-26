# D одной из программ из упражнений с 3.4 по 3.7 используйте len()  для вывода сообщения с количеством людей, приглашенных на обед.

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
i = 0
while i < len(guests):
    print(f'{guests[i].title()}, I would like to invite you on my party at 10th november.')
    i += 1

while  len(guests) != 0:
    del guests[0]

print(f"\nSize of guest list is {len(guests)}")
i = 0
while i < len(guests):
    print(f'{guests[i].title()}, I would like to invite you on my party at 10th november.')
    i += 1
