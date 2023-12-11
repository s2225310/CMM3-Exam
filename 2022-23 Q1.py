# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:28:54 2023

@author: Nick
"""

import numpy as np

def piapprox(n):
    pi = 0
    oldpi = 0
    
    for i in range(1, n+1):
        oldpi = pi
        pi = pi + 1/i**2
        
    oldpi = np.sqrt(6*oldpi)
    pi = np.sqrt(6*pi)
    
    trueerror = np.abs(pi - np.pi)/pi*100
    estimatederror = np.abs(pi - oldpi)/pi*100
    print("true error", trueerror)
    print("estimated error", estimatederror)
    return pi

print("pi, 10 iterations",piapprox(10))
print("pi, 100 iterations",piapprox(100))
print("pi, 1000 iterations",piapprox(1000))

