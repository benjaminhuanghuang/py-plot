import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
	  
      
index = np.arange(4)

data1 = [52,55,63,53]
data2 = [44,66,55,41]

bar_width = 0.3

plt.bar(index, data1, bar_width, color='b')
plt.bar(index, data2, bar_width, color='r', bottom = data1)

plt.show()