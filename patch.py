import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots()

xy1 = np.array([0.2, 0.2])
circle = mpatches.Circle(xy1, 0.1)   # r = 0.1
ax.add_patch(circle)


xy2 = np.array([0.2, 0.8])
rect = mpatches.Rectangle(xy2, 0.2, 0.1, color='r')
ax.add_patch(rect)

xy3 = np.array([0.8, 0.2])
polygon = mpatches.RegularPolygon(xy3, 5, 0.1, color='g')  # 5 borders
ax.add_patch(polygon)

xy4 = np.array([0.8, 0.8])
ellipse = mpatches.Ellipse(xy4, 0.4, 0.2, color='y')  # width, height
ax.add_patch(ellipse)

plt.axis('equal')

plt.show()