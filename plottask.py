# plottask.py
# Author Niall Horgan

import matplotlib.pyplot as plt
import numpy as np
import statistics

m = 10
sd = 2

np.random.seed(1)
norm_data = np.random.normal(m, sd, size=1000 )

plt.hist(norm_data, edgecolor = 'k')

plt.axvline(m, color ='k', linestyle = 'dashed')
plt.title('Normal Distribution (Mean = 10, STD = 2)', fontsize = 15, color = 'red')
plt.xlabel('Values of random Varible X', fontsize = 10, color = 'red')
plt.ylabel('Probability', fontsize = 10, color = 'red')

xpoints = np.array(range(1,10))
ypoints = xpoints * xpoints * xpoints

plt.plot(xpoints, ypoints)

plt.show()