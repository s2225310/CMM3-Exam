# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:41:35 2020

@author: emc1977
"""

def extended_synthetic_division(dividend, divisor):
   
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
 
if __name__ == '__main__':
    print ("POLYNOMIAL SYNTHETIC DIVISION")
    N = [1, -2, -3, 5, 1]
    D = [1, -1.5]
    print ("  %s / %s =" % (N,D),)
    print (" %s remainder %s" % extended_synthetic_division(N, D))
  
