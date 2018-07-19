import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

# create 50 linear space from -1 to 1
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2

# specify legend in plot()
plt.plot(x, y1, label='up')
plt.plot(x, y2, label='down')

plt.legend(loc=1)   # loc values 0 to 10
plt.legend(ncol=2)   # display legend in columns

plt.legend(loc='best')   # show legend

plt.show()