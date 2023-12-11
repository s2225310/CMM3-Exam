# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 10:18:29 2021

@author: emc1977
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 09:08:57 2020

@author: emc1977
"""

#ALTERNATE SYNTHETIC DIVISION

def poly_horner(A, x):
    p = A[-1]
    i = len(A) - 2
    while i >= 0:
        p = p * x + A[i]
        i -= 1
    return p

def poly_naive(A, x):
    p = 0
    for i, a in enumerate(A):
        p += (x ** i) * a
    return p

def poly_iter(A, x):
    p = 0
    xn = 1
    for a in A:
        p += xn * a
        xn *= x
    return p

A = [1, -2, -3, 5, 1]
x = 0.59
print(poly_horner(A,x))
print(poly_naive(A,x))
print(poly_iter(A,x))

