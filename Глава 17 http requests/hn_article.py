# Следующий вызов возвращает информацию о текущей самой популярной статье 
# (на момент написания книги):
from math import fabs
import os
import requests
import json

dir = os.path.dirname(__file__) + '/'

# Вызов API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url, verify=False)
print(f"Status code: {r.status_code}")

# Анализ структуры данных.
response_dict = r.json()
readable_file = dir+'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=2)