# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:39:51 2023

@author: Nick
"""

import numpy as np
from scipy.optimize import fsolve
from matplotlib import pyplot as plt 


x = 50
y = 15
y0 = 5
w = 10

#plotting function f in terms of T
f = lambda T: T/w*np.cosh(w*x/T) + y0 - T/w - y
T = np.arange(1000, 10000, 1)  
plt.plot(T, f(T), '.')

#can be observed root around 1500
#using fsolve to find root
T_a = (fsolve(f,1500))
print("Tension Ta:",T_a)

#Qb
#The tension Ta is 1266.3243604

#substituting T_a into function y to demonstrate value
y = lambda T: T/w*np.cosh(w*x/T) + y0 - T/w
print("y at Ta",y(T_a))

#Confirmed y at T_a is 15

