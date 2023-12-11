# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:21:56 2023

@author: Nick
"""

import numpy as np
import math

def bisection(f,a,b,N,epsilon):
    # Check if a and b bound a root
    if f(a)*f(b) >= 0:
       print("a and b do not bound a root.")
       return None 
    a_n = a
    b_n = b
    m_n = 0
    for n in range(1,N+1):
        oldm_n = m_n
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
           a_n = a_n
           b_n = m_n
        elif f(b_n)*f_m_n < 0:
           a_n = m_n
           b_n = b_n
        elif f_m_n == 0:
           print("Found exact solution in", n, "iterations.")
           return m_n
        else:
           print("Bisection method fails.")
           return None
        if abs((oldm_n-m_n)/m_n) < epsilon: 
            print("Found solution within error margins in", n, "iterations.")
            break
    return (a_n + b_n)/2

def secant(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails.")
            return None
    return a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))

# we solve equation
f = lambda x: 1/np.sin(x) + 1/4 - x
# finding roots from closed and open techniques
closed_root = bisection(f,0.01,4,8,0.001) 
open_root = secant(f,1,2,2) # changed boundaries
print("closed root:",closed_root)
print("open root:",open_root)
print()


#Q3b
#Using the bisection technique with the domain 0.01 to 4 (0 yields division by 0)
#The root found in the domain using the bisection technique
#with 100 iterations is 1.290482177734375

#Q3c
#Using the secant technique with modified domain 1 to 2
#As boundaries of 0 and 4 would yield other roots
#with 25 iterations is 1.290585737222227

#Q3di
#Find absolute root from running secant 100 iterations?
#Find error comparisons and talk about difference due to method

#Q3dii
#|Technique              |Iterations for final answer within 0.01
#----------------------------------------------------------------
#|Brute force iterations |5
#|Bisection              |8
#|Secant                 |2
#----------------------------------------------------------------
#There is a difference in iterations due to the method in the technique
#The brute force iterations are reliant on the number of inputs
#But for the correct input it will tend towards the right answer very quickly

#The bisection technique changes the boundaries around its root estimate
#The secant technique approximates the derivative and projects

#A line to find the root so given the right boundaries
#Can find the root very quickly