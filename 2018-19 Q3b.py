# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:54:31 2023

@author: Nick
"""

import numpy as np

def synthetic_division(dividend, divisor):
   
    #dividend = [1, 4, -12]
    #divisor = [1, 6]
    out = list(dividend) # Copy the dividend
    normalizer = divisor[0]
    for i in range(len(dividend)-(len(divisor)-1)):
        out[i] /= normalizer # for general polynomial division (when polynomials are non-monic),
                                 # we need to normalize by dividing the coefficient with the divisor's first coefficient
        coef = out[i]
        if coef != 0: # useless to multiply if coef is 0
            for j in range(1, len(divisor)): # in synthetic division, we always skip the first coefficient of the divisor,
                                              # because it's only used to normalize the dividend coefficients
                out[i + j] += -divisor[j] * coef
 
    separator = -(len(divisor)-1)
    return out[:separator], out[separator:] # return quotient, remainder.
 
#defining the function and finds roots
function = [1, 5, 15, 3, -10]
roots = np.roots(function)

for i in range(len(roots)):
    #checks if the current root has only real components
    if np.isreal(roots[i]):
        #factorises function by current root and stores as function
        #remainder is zero in both divisions so redundant
        division = [1, -np.real(roots[i])]
        function, remainder = synthetic_division(function, division)
        print("division by", np.real(roots[i]))
        print(function, remainder)
        
    