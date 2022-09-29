import os
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

dir = os.path.dirname(__file__) + '/'

# Создание кубика D6.
die = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
rolls = 10000
for roll_num in range(rolls):
    result = die.roll()
    results.append(result)
 
# Анализ результатов.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
x_values = [f'Грань {a}' for a in range(1, die.num_sides+1)]
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title=f'Results of rolling one D6 {rolls} times',
        xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename=dir+'d6.html')

