# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 15:55:53 2023

@author: Nick
"""
# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,t):
    dydt = 10*y**2 - y**3
    return dydt

# initial conditions
t0 = 0
y0 = 0.02
# total solution interval
t_final = 20
# step size
h = 0.02
# ------------------------------------------------------

# ------------------------------------------------------
# Euler method

# number of steps
n_step = math.ceil(t_final/h)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step+1)
t_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_eul[0] = y0
t_eul[0] = t0 

# Populate the x array
for i in range(n_step):
    t_eul[i+1]  = t_eul[i]  + h

# Apply Euler method n_step times
for i in range(n_step):
    # compute the slope using the differential equation
    slope = model(y_eul[i],t_eul[i]) 
    # use the Euler method
    y_eul[i+1] = y_eul[i] + h * slope  
# ------------------------------------------------------

# ------------------------------------------------------
# print results on screen
print ('Solution: step t y-eul y-exact error%')

for i in range(n_step+1):

        print(i,t_eul[i],y_eul[i], y0 * math.exp(-t_eul[i]),
                (y_eul[i]- y0 * math.exp(-t_eul[i]))/ 
                (y0 * math.exp(-t_eul[i])) * 100)
    

# ------------------------------------------------------

# ---------------------------------------
# plot results
plt.plot(t_eul, y_eul , 'b.-')
plt.xlabel('t')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------

# Q2a
# solutions of y, found by adjusting the total solution interval
# t=4, y=0.09693978594694215
# t=5, y=1.2151433144669004
# t=10, y= 10.0
# the step used was h = 0.01 as it was found steps above 0.02 would become unstable

# Q2b
# ignition delay found by changing initial condition and reading the graph output
# y(0)=0.02, delay = 5
# y(0)=0.01, delay = 10
# y(0)=0.005, delay = 20

# Q2c
# threshold value for h=0.02

# Q2d
# numerical methods are unstable when the solution is wrong and diverges from the true solution
# this happens for larger steps of h as the euler method is unstable when the product -kh is within a region in the complex plane
# the implicit euler method uses the derivative for the next t value to estimate the slope, with unknowns occuring on both sides of the equation
# the implicit euler method is stable even for large steps of h