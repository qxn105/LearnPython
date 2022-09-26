# При запуске выводит имена сохраненных пользователей 
# и предлагает выбрать из списка либо указать имя нового 
# Программа запоминает пользователей в JSON
import os
import json

dir = os.path.dirname(__file__)+'/'
filename = 'username.json'


def get_stored_usernames():
    """Получает хранимое имя пользователя, если оно существует."""
    try:
        with open(dir+filename, encoding='utf8') as f:
            usernames = json.load(f)['usernames']
    except FileNotFoundError: return None
    else: return usernames        

def ask_new_username():
    """Спрашивает и сохраняет имя пользователя."""
    usernames = get_stored_usernames()
    if not usernames: usernames = []
    username = input("What is your name? ")
    if username in usernames:
        print('There is such username yet!')
    else:
        usernames.append(username)
        with open(dir+filename, 'w', encoding='utf8') as f:
            json.dump({'usernames':usernames}, f)
            print(f"We'll remember you when you come back, {username}!")
    return username

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
def greet_user():
    """Приветствует пользователя по имени."""
    usernames = get_stored_usernames()
    if usernames:
        i = 1
        print('Remembered users:')
        for username in usernames:
            print(f'{i}: {username}')
            i += 1
        print('0: New user')
        user = input('Select, who are you: ')
        if user == '0':
            username = ask_new_username()
        else:
            username = usernames[int(user)-1]
            print(f"Welcome back, {username}!")
    else:
        username = ask_new_username()
    print(f"Go on, {username}!")

greet_user()