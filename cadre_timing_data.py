


import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter


full_graph_vars = np.array([179205, 358305, 716505,1432905, 2865705],dtype=float)*6
full_graph_times = np.array([96,191,404,863,1934])


prune_graph_vars = np.array([146942, 293792, 587492,1174892,2349692])*6

prune_graph_times = np.array([76,149,306,635,1375])


plt.rcParams.update({
    'font.size': 15,
    'font': 'serif' 
    })

fig = plt.figure()

plt.loglog(full_graph_vars, full_graph_times, label="Full")
plt.loglog(full_graph_vars, prune_graph_times, label="Reduced")
plt.xlim([10**6,2*10**7])
plt.ylim([5*10**1,2.5*10**3])
plt.xlabel('Number of Variables')
plt.ylabel('Time (sec)')
#plt.xticks([10**5.5,10**6,10**7.5])
plt.legend(loc="best")

ax = plt.gca()

def sci(x, pos):
    'The two args are the value and tick position'
    return '%.0e' % (x)

ax.xaxis.set_major_formatter(FuncFormatter(sci))

#plt.show()

fig.set_size_inches(6,5)
fig.tight_layout()
plt.savefig('cadre_var_scaling.pdf', dpi=1000,bbox_inches="tight")

