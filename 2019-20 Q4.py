# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:30:20 2023

@author: Nick
"""

import numpy as np
from scipy.optimize import fsolve, minimize, rosen, rosen_der

#solving for constants in eq R
#x[0], x[1], x[2] = C, e, alpha respectively
#R is rearranged to the RHS and known theta and R are subbed in
def R_constants(x):
    return [6870 * (1 + x[1]*np.sin(np.deg2rad(-30+x[2]))) - x[0],
            6728 * (1 + x[1]*np.sin(np.deg2rad(0+x[2]))) - x[0],
            6615 * (1 + x[1]*np.sin(np.deg2rad(30+x[2]))) - x[0]]

#storing constants from root solving function
C, e, alpha = fsolve(R_constants, [1, 1, 2])

#R is now a linear function of theta which can be minimised
#defining function, x = theta
R = lambda x: C/(1 + e*np.sin(np.deg2rad(x[0]+alpha)))

#bounds, not sure why i need two conditions
bnds = ((0, None),(0, None))

#minimising R to find x, .x returns the x value from the object returned from the minimize function
x_min = minimize(R, (0), method='SLSQP', bounds=bnds).x
R_min = R(x_min)
print("Smallest radius:",R_min)

#Q4
#The smallest radius of the satellite trajectory is 6553m



