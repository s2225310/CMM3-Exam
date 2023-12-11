# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:56:16 2023

@author: Nick
"""

import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = sp.exp(-x)

# Define the point of expansion
a = 1

# Calculate the derivatives
f_diff = sp.diff(f, x)
f_double_diff = sp.diff(f_diff, x)

# Write the Taylor series expansion up to the second degree
taylor_series = f.subs(x, a) + f_diff.subs(x, a)*(x - a) + (f_double_diff.subs(x, a)/2)*(x - a)**2

# Display the Taylor series expansion
print("Taylor series expansion up to the second degree:")
print(taylor_series)