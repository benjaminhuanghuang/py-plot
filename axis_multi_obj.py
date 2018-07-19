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

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y1)
ax1.set_ylabel('Y1')

ax2 = ax1.twinx()   # creat y 
ax2.plot(x, y2, 'r')
ax2.set_ylabel('Y2')

ax1.set_xlabel('Compare y1 and y2')

plt.show()
