import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim([1,7])
ax.set_ylim([1,5])

ax.text(2, 4, r'$\alpha \beta_j$', size=25)

ax.text(4, 4, r'$ \sin(0)=\cos(\frac{\pi}{2})$', size=25)

ax.text(2, 2, r'$ \lim_{x \rightarrow y} \frac{1}{x^3}$', size=25)

ax.text(4, 2, r'$ \sqrt[4]{x}=\sqrt{y}$', size=25)

plt.show()
