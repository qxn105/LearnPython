import matplotlib.pyplot as plt

from random_walk import RandomWalk

    
# Новые блуждания строятся до тех пор, пока программа остается активной.
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 8), dpi=100)
    
# Построение случайного блуждания.
rw = RandomWalk(50000)
rw.fill_walk()
point_numbers = range(rw.num_points)
# Нанесение точек на диаграмму.
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=1)
#ax.scatter(rw.x_values, rw.y_values, s=15)
#ax.plot(rw.x_values, rw.y_values, linewidth=1)
# Выделение первой и последней точек.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
# Удаление осей.
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
    

