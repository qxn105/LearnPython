# вы только что узнали, что один из гостей прийти не сможет, поэтому вам придется разослать новые приглашения.
# Отсутствующего гостя нужно заменить кем-то другим.
#   • Начните с программы из упражнения 3.4. Добавьте в конец программы команду print для вывода имени гостя, который прийти не сможет.
#   • Измените список и замените имя гостя, который прийти не сможет, именем нового приглашенного.
#   • Выведите новый набор сообщений с приглашениями — по одному для каждого участника, входящего в список.

guests = ['Alexandr', 'Pavel', 'Ilya', 'Artem']
for guest in guests:
    print(f'{guest.title()}, I would like to invite you on my party at 10th november.')
num = 2
print(f"{guests[2].title()} can't come.")
guests[num] = "Oleg"
for guest in guests:
    print(f'{guest.title()}, I would like to invite you on my party at 10th november.')
