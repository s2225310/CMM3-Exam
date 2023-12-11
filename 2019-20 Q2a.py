# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:31:00 2023

@author: Nick
"""

import numpy as np
import scipy.integrate as integrate
from matplotlib import pyplot as plt 

#initialising range of arrays to store p and integrals of y
p = np.arange(0, 10, 0.01)
y_int = np.arange(0, 10, 0.01)

#integrates y and stores it over the range of p values
for i in range(p.size):
    y = lambda x: np.sin(x)*np.cos(p[i]*x)
    #integrate returns two values so splitting them
    y_int[i], v = integrate.quad(y, 0, np.pi)
 
#graphing to see behaviour of integrated y for p values
#will be mirrored on the other side
plt.plot(p, y_int, '.')

#Q2a
#parameter p that minimises is any odd number. smallest p is p=1

