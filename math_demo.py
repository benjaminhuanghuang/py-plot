import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return -(x-2)*(x-8) + 40


x = np.linspace(0, 10)
y = func(x)

fig, ax = plt.subplots()

a = 2
b = 9

ax.set_xticks([a, b])  # value of the ticks on x axis
# label of the ticks $ display a, b as math fomular
ax.set_xticklabels(['$a$', '$b$'])
ax.set_yticks([])      # no ticks on y axis

# shadow is a Polygon
ix = np.linspace(a, b)
iy = func(ix)
ixy = zip(ix, iy)
verts = [(a, 0)] + list(ixy)+[(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

# text nearby axis
plt.figtext(0.9, 0.05, '$x$')
plt.figtext(0.1, 0.9, '$y$')

# fomular
x_math = (a+b) / 3
y_math = 20
plt.text(x_math, y_math, r'$\int_a^b (-(x-2)*(x-8)+40)dx$')

plt.plot(x, y, 'r', linewidth=2)

# should be after plt.plot
plt.ylim(ymin=25)


plt.show()
