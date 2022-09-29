import os
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

dir = os.path.dirname(__file__) + '/'

# Создание кубиков D6 и D10.
d1 = Die()
d2 = Die(8)

# Моделирование серии бросков с сохранением результатов в списке.
results = []
rolls = 500000
results = [d1.roll() + d1.roll() + d1.roll() for i in range(rolls)]
min_result = 3
max_result = d1.num_sides*3

# Анализ результатов.
frequencies = []
for value in range(min_result, max_result+1): 
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
x_values = [f'Сумма={a}' for a in range(min_result, max_result+1)]
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title=f'Results of rolling three D6 {rolls} times',
        xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename=dir+'d6.html')

