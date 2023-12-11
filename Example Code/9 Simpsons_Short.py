# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 11:05:03 2020

@author: emc1977
"""
import numpy as np
def simps(f,a,b,N=50):
    
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    x = np.linspace(a,b,N+1)
    y = f(x)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    print(S)
    return S

f = lambda x: exp(x**-2)
solution = simps(f,1,2,24)
print(solution)

