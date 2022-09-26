#Функции json.dump() и json.load()

import json
import os
dir = os.path.dirname(__file__) + '/'
filename = 'numbers.json'
numbers = [2, 3, 5, 7, 11, 13]

data = {'filename':filename, 'numbers':numbers}

with open(dir+filename, 'w') as f:
    json.dump(data, f)
