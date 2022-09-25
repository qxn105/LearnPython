import os
dir = os.path.dirname(__file__)
filename = f'{dir}/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")