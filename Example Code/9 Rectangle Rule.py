# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:34:29 2020

@author: emc1977
"""
import numpy as np
def calculate_dx (a, b, n):
	return (b-a)/float(n)

def rect_rule (f, a, b, n):
	total = 0.0
	dx = calculate_dx(a, b, n)
	for k in range (0, n):
        	total = total + f((a + (k*dx)))
	return dx*total

def f(x):
    return np.exp(-x**2)

print(rect_rule(f, 0, 1, 1000))
