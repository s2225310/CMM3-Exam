# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:31:00 2023

@author: Nick
"""

import numpy
from scipy.optimize import fsolve
from matplotlib import pyplot as plt 

#initialising range of arrays to store x and y function
x = np.arange(0, np.pi, 0.01)
p = 1
y = lambda x: np.sin(x)*np.cos(p*x)

#graphing to see behaviour of function in domain
plt.plot(x, y(x), '.')

#function is zero in domain around x=0, 1.5, 3.1 which can be checked
#using scipy root solver
x1 = fsolve(y,0)
x2 = fsolve(y,1.5)
x3 = fsolve(y,3.1)

print(x1,x2,x3)

#Q2b
#values of x where function=0 in integration domain
#are at 0, 1.571, 3.141


