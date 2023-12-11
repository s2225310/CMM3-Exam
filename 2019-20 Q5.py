# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:05:06 2023

@author: Nick
"""

from scipy.optimize import minimize
import numpy as np

#constants
l1 = 1.2
l2 = 1.5
l3 = 1
B = 3.5
H = 0
w1 = 20
w2 = 30

#x[0], x[1], x[2] are theta1, theta2 and theta3 respectively
from scipy.optimize import minimize, rosen, rosen_der
fun = lambda x: -w1*l1*np.sin(x[0]) - w2*(l1*np.sin(x[0]) + l2*np.sin(x[1]))

#geometric constants of eq
cons = ({'type': 'ineq', 'fun': lambda x: l1*np.cos(x[0]) + l2*np.cos(x[1]) + l3*np.cos(x[2]) - B},
        {'type': 'ineq', 'fun': lambda x: l1*np.sin(x[0]) + l2*np.sin(x[1]) + l3*np.sin(x[2]) - H})

#bounds, theta/x is between 0 and pi
bnds = ((0, np.pi), (0, np.pi), (0, np.pi))

#minimising the function to find the min theta, .x returns the x value from the minimise
min_theta = minimize(fun, (0, 0, 0), method='SLSQP', bounds=bnds, constraints=cons).x

print("theta 1:",np.rad2deg(min_theta[0]),"degrees")
print("theta 2:",np.rad2deg(min_theta[1]),"degrees")
print("theta 3:",np.rad2deg(min_theta[2]),"degrees")

#Q5
#theta 1: 27.246860419172496 degrees
#theta 2: 17.1700350775848 degrees
#theta 3: 0 degrees
#When double checking using the constants B is accurate but H is slightly off at 0.1
