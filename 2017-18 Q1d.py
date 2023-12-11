# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:00:59 2023

@author: Nick
"""
import sympy as sp
from sympy import symbols, series

# Define the symbols
x, h = symbols('x h')

# Define the function
f = sp.exp(-x)

# Initial value of x and perturbation value
x0 = 1
h_value = 0.1

# Taylor series expansion around x=1 for the given perturbation h=0.1
taylor_expansion = series(f, x, 1)
taylor_expansion_with_h = taylor_expansion.subs(x, 1 + h)

print('Without the perturbation the series is', taylor_expansion) 
print('With the perturbation the series is',taylor_expansion_with_h)

# Calculate the function value at the initial x and at the perturbed x
f_x0 = f.subs(x, x0)
f_x0_perturbed = f.subs(x, x0 + h_value)

# Calculate the change in the function value
delta_f = f_x0_perturbed - f_x0

# Calculate the sensitivity
sensitivity = delta_f / h_value

# Nicely formatted print statement
print(f"Value of f(x) at x = {x0}: {f_x0.evalf():.6f}")
print(f"Value of f(x) at x = {x0 + h_value}: {f_x0_perturbed.evalf():.6f}")
print(f"Change in f(x) due to perturbation: {delta_f.evalf():.6f}")
print(f"Sensitivity of f(x) to perturbation: {sensitivity.evalf():.6f}")


