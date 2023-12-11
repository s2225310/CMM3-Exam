# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:44:35 2023

@author: Nick
"""

from scipy.optimize import minimize
import numpy as np

#constants
E = 200
H = 2.75
p = 7800
pi = 3.14159

#I = second moment of area
#I = pi/32*(d**4-d1**4)

#finding initial max buckling stress

#x[0], x[1] are diameter and thickness respectively
from scipy.optimize import minimize, rosen, rosen_der
fun = lambda x: pi*E * (pi/32*(x[0]**4-(x[0]-2*x[1])**4)) / (H**2*x[0]*x[1])

#geometric constants of eq
cons = ({'type': 'ineq', 'fun': lambda x: x[0]-2*x[1]})

#bounds?
bnds = ((0.01, 0.1), (0.001, 0.01))

#minimisation
min_d, min_t = minimize(fun, (5, 1), method='SLSQP', bounds=bnds, constraints=cons).x


#finding optimal values
#assume material cost is literally cost*weight + cost*diameter
#cost=0.7*volume*density + cost=0.9*diameter
#x[0], x[1] are diameter and thickness respectively
fun = lambda x: 0.7*p*pi*H*(x[0]**2-(x[0]-2*x[1])**2)/4 + 0.9*x[0]

#geometric constants of eq
#geometric constants of eq
cons = ({'type': 'ineq', 'fun': lambda x: x[0]-2*x[1]},
        {'type': 'ineq', 'fun': lambda x: pi*E * (pi/32*(x[0]**4-(x[0]-2*x[1])**4)) / (H**2*x[0]*x[1]) - 0.8*(pi*E * (pi/32*(min_d**4-(min_d-2*min_t)**4)) / (H**2*min_d*min_t))})

#bounds?
bnds = ((0.01, 0.1), (0.001, 0.01))

#minimisation
res = minimize(fun, (5, 1), method='SLSQP', bounds=bnds, constraints=cons).x
print(res)
