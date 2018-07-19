import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
	  
data = [20, 10, 30,25,15]
index = np.arange(5)   

#
pl = plt.barh(y=index, width=data)

plt.show()