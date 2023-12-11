# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 15:19:05 2023

@author: Nick
"""

from scipy.integrate import quad
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import numpy as np

# Constants given in the problem
L = 1000  # in meters
C1 = 30  # in meters
C2 = 5  # in meters

# a) ----------------------------------------------------------

# Hill's elevation function
def z(x):
    if abs(x) > L:
        return 0
    else:
        return C1 * (1 - abs(x)/L)**2 + C2 * (1 - abs(x)/L)**4

# Road's elevation function (initial guess)
def z_R(x, a, b):
    if abs(x) > L:
        return 0
    else:
        return a + b * abs(x)

# Volume integral between the hill and the road
# Integrate the absolute difference between the hill and the road elevation
# Since the function is symmetric, integrate from 0 to L and multiply by 2


# b) ----------------------------------------------------------

# Initial guess for the parameters a and b
initial_guess = [0, 0]

# Objective function to minimize (volume of earth moved)
def objective(params):
    a, b = params
    integral, _ = quad(lambda x: abs(z(x) - z_R(x, a, b)), 0, L)
    return 2 * integral  # multiply by 2 due to symmetry

# Constraints for the optimization (road at ground level at x = ±L)
def constraint(params):
    a, b = params
    return z_R(L, a, b)

# The constraint that the road must be at ground level at x = ±L
con = {'type': 'eq', 'fun': constraint}

# Perform the optimization
result = minimize(objective, initial_guess, constraints=con)

# c) ----------------------------------------------------------

# Print the optimization result
print('Optimization result:', result)

# If the optimization is successful, plot the hill and the road
if result.success:
    optimal_a, optimal_b = result.x
    x_values = np.linspace(-L, L, 4000)
    z_values = [z(x) for x in x_values]
    z_R_values = [z_R(x, optimal_a, optimal_b) for x in x_values]

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, z_values, label='Hill Elevation $z(x)$')
    plt.plot(x_values, z_R_values, label='Road Elevation $z_R(x)$', linestyle='--')
    plt.title('Hill and Road Elevation')
    plt.xlabel('Position $x$ (m)')
    plt.ylabel('Elevation (m)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
    
    
    
    
    