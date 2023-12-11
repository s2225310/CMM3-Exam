# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 13:31:22 2023

@author: Nick
"""

import numpy as np
from scipy.optimize import fsolve
from matplotlib import pyplot as plt 

#defining constants
P = 115000
A = 25500
n = 6

#moving function to RHS and defining function f in terms of i
f = lambda i: P*i*(1+i)**n/((1+i)**n-1)-A

#plotting function
i_range = np.arange(0, 0.2, 0.01)  
plt.plot(i_range, f(i_range), '.')


#can be observed root around 0.1
#using fsolve to find root
i = (fsolve(f,0.1))
print("interest rate",i)

#Q2a
#The interest rate is 0.0855947

#substituting i into function A to demonstrate 25500 annual payment
A = lambda i: P*i*(1+i)**n/((1+i)**n-1)
print("P for interest rate",A(i))

#Confirmed 25500 annual payment for current interest rate
