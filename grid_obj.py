import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.arange(0, 10, 1)   # create an array

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, x**2)
ax.grid(color='g')

plt.show()