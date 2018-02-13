import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

# create 50 linear space from -1 to 1
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.plot(x, y1, label='up')
plt.plot(x, y2, label='down')
plt.legend(labels=['aaa', 'bbb'], loc='best')   # show legend

plt.show()