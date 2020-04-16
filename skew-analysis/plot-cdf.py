import re
import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


skewdata = []
f = open("skew-data-sorted-unfenced")
for line in f:
    if line:
        line = line = line.replace(" ","")
        line = line.replace('\n',"")
        num = float(line)
        skewdata.append(num)


plot = sns.distplot(skewdata)
plot.set(xlabel='Thread skew (Iterations)')
plot.set(ylabel='Probability density')
fig = plot.get_figure()
fig.savefig("skew-unfenced.png")
#hist, bin_edges = np.histogram(skewdata)
#for i in range(1,30):
#    print(hist[i],bin_edges[i])        
#p = 100. * np.arange(len(skewdata))/(len(skewdata) - 1)
#fig, ax = plt.subplots(figsize=(8,4))
#ax = plt.plot(skewdata, p)
# tidy up the figure
#n, bins, patches = plt.hist(x=skewdata, bins='auto', color='#0504aa',
#                            alpha=0.7, rwidth=0.85)
#plt.grid(axis='y', alpha=0.75)
#plt.xlabel('Thread skew (iterations)',fontsize=16)
#plt.ylabel('Frequency',fontsize=16)
#plt.text(23, 45, r'$\mu=15, b=3$')
#maxfreq = n.max()
# Set a clean upper y-axis limit.
#plt.ylim(ymax=40000)
#plt.ylim(ymax=np.ceil(maxfreq / 10) * 8 if maxfreq % 10 else maxfreq + 10)
#plt.grid(True)

#locs, labels = xticks()
#plt.legend(loc='right')
#plt.set_title('Cumulative step histograms')
#plt.show()
#plt.savefig('skew-data.png')

