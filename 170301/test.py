import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
 
def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')
 
x = [1,2,3,4,5,6,7,8,9,10]
y = [3,5,2,4,9,1,7,5,9,1]
 
yMA = movingaverage(y,3)
print yMA
 
plt.plot(x[len(x)-len(yMA):],yMA)
plt.plot(x,y)
plt.show()