# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:23:37 2023

@author: Nick
"""

import numpy as np
from scipy.optimize import fsolve
from matplotlib import pyplot as plt 

L = 800
E = 40000
I = 40000
wo = 3.5

#function y
y = lambda x: wo/(120*E*I*L) * (-x**5 + 2*L**2*x**3 - L**4*x)

#plotting the function
x = np.linspace(0,800,100)
plt.plot(x,y(x))
plt.show()

#Q1a
#The maximum deflection occurs around 350

