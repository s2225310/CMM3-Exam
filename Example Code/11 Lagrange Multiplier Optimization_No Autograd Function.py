# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 12:25:44 2020

@author: emc1977
"""

import numpy as np
from scipy.optimize import minimize

# This s the objective function without any constraints inserted yet.
# Function F below combines this objective function with the constraint in eq just below
# to form an Augmented Lagrange Function.
def objective(X):
    x, y, z = X
    return x**2 + y**2 + z**2

#This is the constraint function that has lambda as a coefficient.
def eq(X):
    x, y, z = X
    return 2 * x - y + z - 3

sol = minimize(objective, [1, 4, 5], constraints={'type': 'eq', 'fun': eq})
sol

print(sol)
