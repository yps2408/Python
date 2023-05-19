# Даны две функции:
# f(x) = x^3 - 50x и g(x) = -x^4 + 88x^2 - 241
# Требуется:
# Найти точки пересечения
# Построить графики функций в одной системе координат
# Построить график общей функции
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString
x = np.arange(-11, 12, 0.1)
y1 = x**3 - 50*x
y2 =-x**4 + 88*x**2 - 241
fig, ax = plt.subplots(figsize = (12, 6))

ax.plot(x, y1, x, y2)
ax.fill_between(x, y1, y2, where=y2>y1, color='green', alpha=0.3)

lgnd = ax.legend(['y1', 'y2'], loc='lower center', shadow=False)
lgnd.get_frame().set_facecolor('#ffb19a')

first_line = LineString(np.column_stack((x, y1)))
second_line = LineString(np.column_stack((x, y2)))
intersection = first_line.intersection(second_line)

if intersection.geom_type == 'MultiPoint':
    plt.plot(*LineString(intersection).xy, 'o')
elif intersection.geom_type == 'Point':
    plt.plot(*intersection.xy, 'o')

x, y = LineString(intersection).xy

print('Координаты пересечения функций (X, Y):')
data = tuple(zip([i for i in x], [i for i in y]))
for i in data:
    print(i)
plt.show()