# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# functions that returns dy/dx
# i.e. the equation we want to solve: dy_j/dx = f_j(x,y_j) (j=[1,2] in this case)
def model(x,y_1,y_2):
    f_1 = -0.5 * y_1
    f_2 = 4.0 - 0.3 * y_2 - 0.1 * y_1
    return [f_1 , f_2]
# ------------------------------------------------------


# ------------------------------------------------------
# initial conditions
x0 = 0
y0_1 = 4
y0_2 = 6
# total solution interval
x_final = 20
# step size
h = 0.1
# ------------------------------------------------------


# ------------------------------------------------------
# Euler method

# number of steps
n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
y_1_eul = np.zeros(n_step+1)
y_2_eul = np.zeros(n_step+1)
x_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_1_eul[0] = y0_1
y_2_eul[0] = y0_2
x_eul[0]   = x0 

# Populate the x array
for i in range(n_step):
    x_eul[i+1]  = x_eul[i]  + h

# Apply Euler method n_step times
for i in range(n_step):
    # compute the slope using the differential equation
    [slope_1 , slope_2] = model(x_eul[i],y_1_eul[i],y_2_eul[i]) 
    # use the Euler method
    y_1_eul[i+1] = y_1_eul[i] + h * slope_1
    y_2_eul[i+1] = y_2_eul[i] + h * slope_2
    print(y_1_eul[i],y_2_eul[i])
# ------------------------------------------------------


# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_1_eul , 'b.-',x_eul, y_2_eul , 'r-')
plt.xlabel('x')
plt.ylabel('y_1(x), y_2(x)')
plt.show()
# ------------------------------------------------------
'''
# ------------------------------------------------------
# print results in a text file (for later use if needed)
file_name= 'output_h' + str(h) + '.dat' 
f_io = open(file_name,'w') 
for i in range(n_step+1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_1_eul[i])
    s4 = str(y_2_eul[i])
    s_tot = s1 + ' ' + s2 + ' ' + s3  + ' ' + s4
    f_io.write(s_tot + '\n')
f_io.close()
# ------------------------------------------------------
'''
