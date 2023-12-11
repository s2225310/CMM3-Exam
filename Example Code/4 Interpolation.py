# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import scipy
from scipy import interpolate

x = np.array([0.  , 0.06666667, 0.13333333, 0.2 ,  0.26666667, 0.33333333,
     0.4 , 0.46666667, 0.53333333, 0.6 ,  0.66666667, 0.73333333,
     0.8 , 0.86666667, 0.93333333, 1.  , ])

y = np.array([ 0.00000000e+00,  7.78309056e-01,  1.24040577e+00,  1.24494914e+00,
      8.90566050e-01,  4.33012702e-01,  1.12256994e-01,  4.54336928e-03,
     -4.54336928e-03, -1.12256994e-01, -4.33012702e-01, -8.90566050e-01,
     -1.24494914e+00, -1.24040577e+00, -7.78309056e-01, -4.89858720e-16])

plt.plot(x,y, "o")
xnew = np.linspace(0,1,num=128)
splinex = interpolate.splev(xnew,interpolate.splrep(x,y))
plt.plot(xnew,splinex,"b.")