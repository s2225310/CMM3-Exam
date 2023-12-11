# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:11:46 2023

@author: Nick
"""
import numpy as np
from scipy.optimize import fsolve
from matplotlib import pyplot as plt 

#plotting function y
y = lambda b: (np.cosh(b)) * (np.cos(b)) + 1

b = np.arange(-2, 2, 0.1)
fig = plt.figure(1)    
plt.plot(b, y(b), '.')

#can be observed smallest unique b for y=0 around (1.5,2) and 5
#as b^4 so searching for different b as eq is symmetric
#using fsolve to find roots at each point
b1 = (fsolve(y,2))
b2 = fsolve(y,5)
#print(b1.item(),b2)

#defining new function by rearranging equation 3 for f
f = lambda b: np.sqrt(b**4*E*I/(4*np.pi**2*m*L**3))

#defining constants for f
E = 200
I = 3.255*10**(-11)
m = 7850
L = 0.9

#f can be graphed where it resembles an even polynomial that gets greater
#for larger +- b values so the smallest b values found equal to 0 are smallest f values
print('smallest f values that satisfy equation:',f(b1),f(b2))

#Q2 smallest f values that satisfy equation: 5.96846685e-07, 5.96846685e-07