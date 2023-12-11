# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,x):
    k= - 1
    dydx = k * y
    return dydx

# initial conditions
x0 = 0
y0 = 1
# total solution interval
x_final = 1
# step size
h = 0.2
# ------------------------------------------------------

# ------------------------------------------------------
# Fourth Order Runge-Kutta method

# number of steps
n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
y_rk = np.zeros(n_step+1)
x_rk = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_rk[0] = y0
x_rk[0] = x0 

# Populate the x array
for i in range(n_step):
    x_rk[i+1]  = x_rk[i]  + h

# Apply RK method n_step times
for i in range(n_step):
   
    # Compute the four slopes
    x_dummy = x_rk[i]
    y_dummy = y_rk[i]
    k1 =  model(y_dummy,x_dummy)
    
    x_dummy = x_rk[i]+h/2
    y_dummy = y_rk[i] + k1 * h/2
    k2 =  model(y_dummy,x_dummy)

    x_dummy = x_rk[i]+h/2
    y_dummy = y_rk[i] + k2 * h/2
    k3 =  model(y_dummy,x_dummy)

    x_dummy = x_rk[i]+h
    y_dummy = y_rk[i] + k3 * h
    k4 =  model(y_dummy,x_dummy)

    # compute the slope as weighted average of four slopes
    slope = 1/6 * k1 + 2/6 * k2 + 2/6 * k3 + 1/6 * k4 

    # use the RK method
    y_rk[i+1] = y_rk[i] + h * slope  
# ------------------------------------------------------

# ------------------------------------------------------
# super refined sampling of the exact solution c*e^(-x)
# n_exact linearly spaced numbers
# only needed for plotting reference solution

# Definition of array to store the exact solution
n_exact = 1000
x_exact = np.linspace(0,x_final,n_exact+1) 
y_exact = np.zeros(n_exact+1)

# exact values of the solution
for i in range(n_exact+1):
    y_exact[i] = y0 * math.exp(-x_exact[i])
# ------------------------------------------------------

# ------------------------------------------------------
# print results on screen
print ('Solution: step x y-eul y-exact error%')
for i in range(n_step+1):
    print(i,x_rk[i],y_rk[i], y0 * math.exp(-x_rk[i]),
            (y_rk[i]- y0 * math.exp(-x_rk[i]))/ 
            (y0 * math.exp(-x_rk[i])) * 100)
# ------------------------------------------------------
'''
# ------------------------------------------------------
# print results in a text file (for later use if needed)
file_name= 'output_h' + str(h) + '.dat' 
f_io = open(file_name,'w') 
for i in range(n_step+1):
    s1 = str(i)
    s2 = str(x_rk[i])
    s3 = str(y_rk[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
# ------------------------------------------------------
'''
# ------------------------------------------------------
# plot results
plt.plot(x_rk, y_rk , 'b.-',x_exact, y_exact , 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------


