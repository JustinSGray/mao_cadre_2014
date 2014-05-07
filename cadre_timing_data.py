"""N = 750
Problem Size (CADRE) = 179205
Time = 126 sec

N = 1500
Problem Size (CADRE) = 358305
Time = 254 sec

N = 3000
Problem Size (CADRE) = 716505
Time = 539 sec


With Pruning and Zero-vector Detection
----------------------------------------

N = 750
Problem Size (CADRE) = 146942
Time = 86.6 sec

N = 1500
Problem Size (CADRE) = 293792
Time = 173 sec

N = 3000
Problem Size (CADRE) = 587492
Time = 364 sec"""


import numpy as np
from matplotlib import pyplot as plt

full_graph_vars = np.array([179205, 358305, 716505])*6
full_graph_times = np.array([126,254,539])


prune_graph_vars = np.array([146942, 293792, 587492])*6
prune_graph_times = np.array([86.6,173,364])


plt.plot(full_graph_vars, full_graph_times)
plt.plot(prune_graph_vars, prune_graph_times)
plt.xlim([10**5.5,10**6.6])
plt.xticks([10**5.5,10**6,10**6.5])

ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')

plt.show()
