import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.linspace(0, 5*np.pi, 100)
y1 = np.sin(x)
y2 = np.sin(2*x)

fig = plt.figure()
ax = fig.gca()
ax.plot(x, y1, x, y2, color='k')

# ax.fill_between(x, y1, y2, facecolor='b')
ax.fill_between(x, y1, y2, where=y1 > y2, facecolor='b', interpolate=True)
ax.fill_between(x, y1, y2, where=y1 < y2, facecolor='g', interpolate=True)


plt.show()
