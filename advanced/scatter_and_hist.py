'''
    disply scatter and hist in one figure
'''
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

plt.style.use('ggplot')


x = np.random.randn(200)
y = x + np.random.randn(200) * 0.5

margin_border = 0.1
width = 0.6
margin_between = 0.02
height = 0.2

# size of scatter
left_s = margin_border
bottom_s = margin_border
height_s = width
width_s = width

# size of hist 1
left_x = margin_border
bottom_x = margin_border + width + margin_between
height_x = height
width_x = width

# size of hist 2
left_y = margin_border + width + margin_between
bottom_y = margin_border
height_y = width
width_y = height


plt.figure(1, figsize=(8, 8))
rect_s = [left_s, bottom_s, width_s, height_s]
rect_x = [left_x, bottom_x, width_x, height_x]
rect_y = [left_y, bottom_y, width_y, height_y]

axScatter = plt.axes(rect_s)
axScatter.scatter(x, y)

bin_width = 0.25
xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
lim = int(xymax / bin_width + 1)

axHisX = plt.axes(rect_x)
axHisX.set_xticks([])


axHisY = plt.axes(rect_y)
axHisY.set_yticks([])

plt.show()
