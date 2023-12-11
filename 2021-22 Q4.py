# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:38:33 2023

@author: Nick
"""

# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve:
def model(y,x):
    gamma = -10
    dydx = gamma*y + (1-gamma)*np.cos(x) - (1+gamma)*np.sin(x)
    return dydx

# initial conditions
x0 = 0
y0 = 1
# total solution interval
x_final = 4*np.pi
# step size
h = 0.01
# ------------------------------------------------------

# ------------------------------------------------------
# Euler method

# number of steps
n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step+1)
x_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_eul[0] = y0
x_eul[0] = x0 

# Populate the x array
for i in range(n_step):
    x_eul[i+1]  = x_eul[i]  + h

# Apply Euler method n_step times
for i in range(n_step):
    # compute the slope using the differential equation
    slope = model(y_eul[i],x_eul[i]) 
    # use the Euler method
    y_eul[i+1] = y_eul[i] + h * slope  
# ------------------------------------------------------

# ------------------------------------------------------
# super refined sampling of the exact solution 
# n_exact linearly spaced numbers
# only needed for plotting reference solution

# Definition of array to store the exact solution
n_exact = x_eul.size-1
x_exact = np.linspace(0,x_final,n_exact+1) 
y_exact = np.zeros(n_exact+1)
true_error = np.zeros(n_exact+1)

# exact values of the solution
for i in range(n_exact+1):
    y_exact[i] = np.sin(x_exact[i])+np.cos(x_exact[i])
    
# ------------------------------------------------------

# ------------------------------------------------------
# print results on screen
print ('Solution: step x y-eul y-exact error%')
for i in range(n_step+1):
    
    if x_exact[i] == 0: #avoid division by 0
        true_error[i] = 0
    else:
        
        true_error[i] = np.abs((y_eul[i]-y_exact[i])/y_exact[i])*100
    
   # print(i,x_eul[i],y_eul[i],x_exact[i], y_exact[i])
    #print(i,"error:",true_error[i])
    '''
    print(i,x_eul[i],y_eul[i], y0 * math.exp(-x_eul[i]),
            (y_eul[i]- y0 * math.exp(-x_eul[i]))/ 
            (y0 * math.exp(-x_eul[i])) * 100)
    '''

print("max error:",np.max(true_error))
# ------------------------------------------------------

# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_eul , 'b.-',x_exact, y_exact, 'r.-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------


#Q4a
#step h=0.01, was found to be stable under ~h=0.2 but kept the step lower
#to get closer to specific t values
#solution at t=2*pi, dy/dx = 0.9972554437435043
#solution at t=4*pi, dy/dx = 0.9940532175161191

#Q4b
#for step h=0.01
#max error in t=(0:2*pi) is 
#max error in t=(0:4*pi) is 
#error was calculated as abs((y- true y)/true y)*100
#when graphing error instead of linear it makes a v with origin at like x=4?

#Q4c
#error found by using max error function and changing step sizes for time ranges
#step h/error at t=2*pi/error at t=4*pi
#0.025/180/3381
#0.05/113/202
#0.1/112/201
#0.15/152/120
#0.2/4349/239
#0.25/170761/6163410195
#0.3/3180596/6691672024182

#Q4di
#error varies for different h but dramatically changes above h=0.2
#where the euler function becomes unstable
#errors are larger for smaller h, become smaller around h=0.1
#and become larger at h=0.2
#smaller h steps allow even smaller y values allowing larger errors
#larger h also can diverge due to inaccurate euler y values

#Q4dii
#error trend is different for different ranges of h
#when the y values are checked at max error points
#error trend similar for h=0.1 and h=0.05 but different for
#every other step h