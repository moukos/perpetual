import numpy as np
#import matplotlib.pyplot as plt

data = np.loadtxt('skew-data')

sorted_data = np.sort(data)
f = open('skew-data-sorted-unfenced',"w+")
for i in range(0,len(sorted_data)):
    f.write(str(int(sorted_data[i])))
    f.write('\n')
f.close()
#yvals=np.arange(len(sorted_data))/float(len(sorted_data)-1)

#plt.plot(sorted_data,yvals)

#plt.show()
