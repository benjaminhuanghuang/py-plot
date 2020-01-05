import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
	  
  
plt.figure
# 2 * 2 subplots
plt.subplot(2,2,1)
plt.plot([0,1], [0,1])

plt.subplot(2,2,2)
plt.plot([0,1], [0,1])

plt.subplot(2,2,3)
plt.plot([0,1], [0,1])

plt.subplot(2,2,4)
plt.plot([0,1], [0,1])

plt.show()