import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
	  
data = [20, 10, 30,25,15]
index = np.arange(5)   

#
pl = plt.bar(x=0, bottom=index, width=data, color='b', height=0.5, orientation='horizontal')

plt.show()