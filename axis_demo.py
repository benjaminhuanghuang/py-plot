import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# create 50 linear space from -1 to 1
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='r', linewidth=3.0, linestyle='-')

plt.xlim((-1, 2))   # x from -1 to 2
plt.ylim((-2, 3))   # y from -2 to 3

plt.xlabel('i am x')
plt.ylabel('i am y')


# Create ticks -1 to 2
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$',
                                     r'$bad\ \alpha$', 'normal', 'good', 'really good'])

# Change axis location
# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# x axis cross y axis at -1
ax.spines['bottom'].set_position(('data', -1))
ax.spines['left'].set_position(('data', 0))
plt.show()
