# сохраните имя пользователя в переменной и выведите сообщение, предназначенное для конкретного человека.
# Сообщение должно быть простым — например, «Hello Eric, would you like to learn some Python today?”.

name = 'Eric'
message = f'Hello {name}, would you like to learn some Python today?'
print(message)
message = f"Hello {name}, would you like to learn some Python today?"
print(message)
# в версии ниже 3.6 форматирование строк выглядит следующим образом
# full_name = "{} {}".format(first_name, last_name)
message = "Hello {}, would you like to learn some Python today?".format(name)
print(message)
