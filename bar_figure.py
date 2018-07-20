import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fig = plt.figure()

# basic bar
ax_bar = fig.add_subplot(423)   # creat y 
data = [20, 10, 30,25,15]
index = np.arange(5)   

ax_bar.bar(x=index, height = data, color='b', width=0.5)


# bar with legend
ax1 = fig.add_subplot(421)
ax1.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one")
ax1.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')

ax1.legend()


# bar
ax2 = fig.add_subplot(422)  
index = np.arange(4)

data1 = [52,55,63,53]
data2 = [44,66,55,41]

bar_width = 0.3

ax2.bar(index, data1, bar_width, color='b')
ax2.bar(index, data2, bar_width, color='r', bottom = data1)

plt.show()
