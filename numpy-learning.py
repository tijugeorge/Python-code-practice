import numpy as np
a = np.array([0,1,2,3,4,5])
b = a.reshape((3,2))
b[1][0] = 77
c = a.reshape((3,2)).copy()
c[0][0] = -99
z=a[np.array([2,3,4])].copy()
