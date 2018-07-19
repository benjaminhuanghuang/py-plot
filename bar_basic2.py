import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
	  
data = [20, 10, 30,25,15]
index = np.arange(5)   

#
pl = plt.bar(x=index, height = data, color='b', width=0.5)

plt.show()