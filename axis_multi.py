'''
    Tow y axis in plot with different scale
'''
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.arange(2, 20, 1)
y1 = x*x
y2 = np.log(x)

plt.plot(x, y1)

plt.twinx()     # add more y axis
plt.plot(x, y2, 'r')



plt.show()
