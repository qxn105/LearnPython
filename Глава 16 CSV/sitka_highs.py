import os
import csv
from datetime import datetime

from matplotlib import pyplot as plt

dir = os.path.dirname(__file__) + '/'
#filename = dir+'data/sitka_weather_07-2018_simple.csv'
#filename = dir+'data/sitka_weather_2018_simple.csv'
filename = dir+'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        # Чтение максимальных температур
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = (int(row[4])-32)/1.8
            low = (int(row[5])-32)/1.8
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Печать заголовков и их позиций (выясним индекс нужных нам данных)
# for index, column_header in enumerate(header_row):
#    print(index, column_header)

# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#title = "Daily high temperatures, July 2018"
#title = "Daily high temperatures - 2018"
title = "Daily high and low temperatures - 2018 Death Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
# print(f'{highs:.0f}')


