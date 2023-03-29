# plottask.py
# Author Niall Horgan

import matplotlib.pyplot as plt
import numpy as np
import statistics

np.random.seed(1)
norm_data = np.random.normal(size=1000, )

plt.hist(norm_data, edgecolor = 'k')

m = statistics.mean(norm_data)
sd = statistics.stdev(norm_data)

plt.axvline(m, color ='k', linestyle = 'dashed')

plt.axvline(sd, color ='k', linestyle = 'dashed')
plt.axvline(sd, color ='k', linestyle = 'dashed')

plt.show()