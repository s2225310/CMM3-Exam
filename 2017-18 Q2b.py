# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 22:37:29 2023

@author: Nick
"""

import numpy as np
import scipy.integrate as integrate

#define function and constants
u = 1.8*10**3
m = 160*10**3
q = 2.5*10**3

v = lambda t: u*np.log(m/(m-q*t))

#integrate the velocity over 30 seconds to find distance
d, d_error = integrate.quad(v, 0, 30)

print("distance", d)

#Qb
#The distance travelled by the rocket is 15289.6m