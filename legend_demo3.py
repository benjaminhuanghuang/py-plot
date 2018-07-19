import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

x = np.arange(1,11,1)

fig = plt.figure()
ax = fig.add_subplot(111)

l, = plt.plot(x, x)

# Method 1
# ax.legend('ax legend')

# Method 2
l.set_label('lable via plot')

# Method 3
#l, = plt.plot(x, x, lable='inline label')
# ax.legend()

plt.show()