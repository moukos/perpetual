import re
import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt



skewdata = []
f = open("skew-data-sorted")
for line in f:
    if line:
        line = line = line.replace(" ","")
        line = line.replace('\n',"")
        num = float(line)
        skewdata.append(num)
        
p = 100. * np.arange(len(skewdata))/(len(skewdata) - 1)
#fig, ax = plt.subplots(figsize=(8,4))
ax = plt.plot(skewdata, p)
# tidy up the figure
plt.grid(True)

#locs, labels = xticks()
#plt.legend(loc='right')
#plt.set_title('Cumulative step histograms')
plt.xlabel('Thread execution skew (iterations)',fontsize=10)
plt.ylabel('Cumulative distribution of litmus test executions (%)',fontsize=10)

#plt.show()
plt.savefig('skew-data.png')

