import os
import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from pyparsing import identbodychars

dir = os.path.dirname(__file__) + '/'

# Изучение структуры данных.
#filename = dir + 'data/eq_data_1_day_m1.json'
#filename = dir + 'data/1.0_day.geojson'
filename = dir + 'data/1.0_month.geojson'

with open(filename, encoding='utf8') as f:
    all_eq_data = json.load(f)
with open(dir+'data/metadata.json', 'w') as f:
    json.dump(all_eq_data['metadata'], f, indent=2)
all_eq_dicts = all_eq_data['features']

all_eq_dicts = filter(lambda d: d['properties']['mag']>6, all_eq_dicts)
all_eq_dicts = sorted(all_eq_dicts, key=lambda d: d['properties']['mag'])

with open(dir+'data/readable_eq_data.json', 'w') as f:
    json.dump(all_eq_dicts, f, indent=2)

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']["coordinates"][0]
    lat = eq_dict['geometry']["coordinates"][1]
    hover_text = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(hover_text)

# Нанесение данных на карту.
# data = [Scattergeo(lon=lons, lat=lats)]
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text':hover_texts,
    'marker': {
        'size': [3*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
with open(dir+'data/data.json', 'w') as f:
    json.dump(data, f, indent=2)

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=dir+'global_earthquakes.html')

