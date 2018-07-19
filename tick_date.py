import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import datetime


start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 1, 1)
delta = datetime.timedelta(days=1)

dates = matplotlib.dates.drange(start, end, delta)

values = np.random.rand(len(dates))

fig = plt.figure()
ax = plt.gca()
ax.plot_date(dates, values, linestyle='-')

plt.show()
