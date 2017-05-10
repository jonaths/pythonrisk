import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
 
a = np.arange(90).reshape(15,6)
print "a"
print a

b = a[0:2,1:14]
c = a[2:4,1:14]
d = a[4:6,1:14]

print "b"
print b

print "c"
print c

print "d"
print d

n = 2
m = 5
b = 3

for bi in range(b):
	print a[bi*n:bi*n+n,1:m]
