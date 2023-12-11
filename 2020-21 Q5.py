# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:13:45 2023

@author: Oscar
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm

# Constants
b = 1 # Width of the tank is 2 meters, so radius b is 1 meter
A = 0.01 # Area of the drainage slot in square meters
g = 9.81 # Acceleration due to gravity in m/s^2
h0 = 1 # Initial height of the water in meters

# Bernoulli's equation for flow rate Q
Q = lambda h: A * np.sqrt(2 * g * h)

# Differential equation for the cylindrical tank
dh_dt_cylindrical = lambda t, h: -Q(h) / (np.pi * b**2)

# Solve the differential equation for the cylindrical tank
time_span = [0, 10000] # Arbitrary long time to ensure the tank can drain
initial_conditions = [h0]
solution_cylindrical = solve_ivp(dh_dt_cylindrical, time_span, initial_conditions, method='RK45', max_step=0.1)

# Time to drain the cylindrical tank
t_drain_cylindrical = solution_cylindrical.t[-1]

print('Time to drain the cylindrical tank:', t_drain_cylindrical, 'seconds')

# Plot the height of water over time for the cylindrical tank
plt.figure(figsize=(10, 6))
plt.plot(solution_cylindrical.t, solution_cylindrical.y[0])
plt.title('Water Height vs. Time for Cylindrical Tank')
plt.xlabel('Time (seconds)')
plt.ylabel('Water Height (meters)')
plt.grid(True)
plt.show()


# Function to calculate the radius at a given height z
s = 0.1 # Initial guess for the slope
radius_at_z = lambda z: b + s * z

# Differential equation for the truncated cone-shaped tank
dh_dt_cone = lambda t, h: -Q(h) / (np.pi * radius_at_z(h)**2)

# Solve the differential equation for the truncated cone-shaped tank with initial guess for slope
solution_cone = solve_ivp(dh_dt_cone, time_span, initial_conditions, method='RK45', max_step=0.1)

# Time to drain the truncated cone-shaped tank with initial guess for slope
t_drain_cone = solution_cone.t[-1]

print('Time to drain the truncated cone-shaped tank with initial guess for slope s =', s, ':', t_drain_cone, 'seconds')

# Function to find the slope s that doubles the drain time
# We will use a simple iterative approach to adjust s until the time to drain the cone is approximately double that of the cylindrical tank
def find_slope(s, t_target):
    for i in tqdm(range(1000)): # Iteration limit
        radius_at_z = lambda z: b + s * z
        dh_dt_cone = lambda t, h: -Q(h) / (np.pi * radius_at_z(h)**2)
        solution_cone = solve_ivp(dh_dt_cone, time_span, initial_conditions, method='RK45', max_step=0.1)
        t_drain_cone = solution_cone.t[-1]
        if np.isclose(t_drain_cone, t_target, rtol=1e-2): # 1% tolerance
            return s
        elif t_drain_cone < t_target:
            s += 0.001 # Increment s if the time is less than target
        else:
            s -= 0.001 # Decrement s if the time is more than target
    return s

# Target time is double the cylindrical tank drain time
target_time = 2 * t_drain_cylindrical
s_optimal = find_slope(s, target_time)

print('Optimal slope s to double the drain time:', s_optimal)