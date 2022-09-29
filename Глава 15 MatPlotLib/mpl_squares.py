import matplotlib.pyplot as plt
import os
dir = os.path.dirname(__file__)

print(plt.style.available)
plt.style.use('seaborn')

x_values = list(range(1, 1001))
y_values = [a**4 for a in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, cmap=plt.cm.Reds, c=y_values, s=30)

#ax.plot(x_values, y_values, linewidth=3,color='lime')

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', labelsize=14)

# Назначение диапазона для каждой оси.
#ax.axis([0, 1100, 0, 1100000])

#plt.show()
plt.savefig(f'{dir}/squares_plot.png', bbox_inches='tight')