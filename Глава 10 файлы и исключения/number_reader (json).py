#Функции json.dump() и json.load()

import json
import numbers
import os
dir = os.path.dirname(__file__) + '/'
filename = 'numbers.json'

with open(dir+filename) as f:
    data = json.load(f)
print(data)
filename = data['filename']
print(filename)
numbers = data['numbers']
print(numbers)
