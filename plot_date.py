import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# convert col 0 to date
date, open, close = np.loadtxt('1.csv', delimiter=',', converters={0: mdates.strpdate2num('%m/%d/%Y')},
                skiprows=1, usecols=(0, 1, 4), unpack=False)

# two lines on plot
plt.plot_date(date, open, close, linestyle='--')
plt.show()
