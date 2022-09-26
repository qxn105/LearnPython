# сохраните имя пользователя в переменной 
# и выведите его в нижнем регистре, в верхнем регистре и с капитализацией начальных букв каждого слова.

name = 'EriC BUsh'
message = f"Hello {name.lower()}, would you like to learn some Python today?"
print(message)
message = f"Hello {name.upper()}, would you like to learn some Python today?"
print(message)
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)
