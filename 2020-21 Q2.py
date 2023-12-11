# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:23:28 2023

@author: Nick
"""

# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# eq2b
def non_linear_model(t, theta, omega):
    dtheta_dt= omega
    domega_dt = -g/l*np.sin(theta)
    return [dtheta_dt , domega_dt]

# eq2c
def linear_model(t, theta, omega):
    dtheta_dt= omega
    domega_dt = -g/l*theta
    return [dtheta_dt , domega_dt]
# ------------------------------------------------------


# ------------------------------------------------------
# initial conditions
t0 = 0
theta0 = np.pi/4
omega0 = 0
# total solution interval
t_final = 30
# step size
h = 0.001
#constants
g = 9.81
l = 9.81
# ------------------------------------------------------


# ------------------------------------------------------
# Euler method

# number of steps
n_step = math.ceil(t_final/h)

# Definition of arrays to store the solution
non_linear_theta_eul = np.zeros(n_step+1)
non_linear_omega_eul = np.zeros(n_step+1)
linear_theta_eul = np.zeros(n_step+1)
linear_omega_eul = np.zeros(n_step+1)
t_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
non_linear_theta_eul[0] = theta0
non_linear_omega_eul[0] = omega0
linear_theta_eul[0] = theta0
linear_omega_eul[0] = omega0
t_eul[0] = t0 

# Populate the x array
for i in range(n_step):
    t_eul[i+1]  = t_eul[i]  + h

# Apply Euler method n_step times
for i in range(n_step):
    #print([i],t_eul[i],non_linear_theta_eul[i],non_linear_omega_eul[i])
    #print([i],t_eul[i],linear_theta_eul[i],linear_omega_eul[i])
    # compute the slope using the differential equation    
    
    [slope_1 , slope_2] = non_linear_model(t_eul[i],non_linear_theta_eul[i],non_linear_omega_eul[i])
    [slope_3 , slope_4] = linear_model(t_eul[i],linear_theta_eul[i],linear_omega_eul[i]) 

    # use the Euler method
    non_linear_theta_eul[i+1] = non_linear_theta_eul[i] + h * slope_1
    non_linear_omega_eul[i+1] = non_linear_omega_eul[i] + h * slope_2  
    linear_theta_eul[i+1] = linear_theta_eul[i] + h * slope_3
    linear_omega_eul[i+1] = linear_omega_eul[i] + h * slope_4
# ------------------------------------------------------

print("non linear system")
print("theta at 10s:" ,non_linear_theta_eul[9999])
print("omega at 10s:", non_linear_omega_eul[9999])
print("theta at 20s:" ,non_linear_theta_eul[19999])
print("omega at 20s:", non_linear_omega_eul[19999])
print("theta at 30s:" ,non_linear_theta_eul[29999])
print("omega at 30s:", non_linear_omega_eul[29999])
print("linear system")
print("theta at 10s:" ,linear_theta_eul[9999])
print("omega at 10s:", linear_omega_eul[9999])
print("theta at 20s:" ,linear_theta_eul[19999])
print("omega at 20s:", linear_omega_eul[19999])
print("theta at 30s:" ,linear_theta_eul[29999])
print("omega at 30s:", linear_omega_eul[29999])

plt.subplot(2, 2, 1)
plt.plot(t_eul,non_linear_theta_eul)
plt.plot(t_eul,linear_theta_eul)
plt.subplot(2, 2, 2)
plt.plot(t_eul,non_linear_omega_eul)
plt.plot(t_eul,linear_omega_eul)
                                        
#Q2a
'''
non linear system
theta at 10s: -0.7756060017236538
omega at 10s: 0.13823283075609785
theta at 20s: 0.7396282405164263
omega at 20s: -0.271891495906316
theta at 30s: -0.679728388103547
omega at 30s: 0.39672378009050063
linear system
theta at 10s: -0.662738695069429
omega at 10s: 0.42874994961137786
theta at 20s: 0.32445678149285834
omega at 20s: -0.7239051309112791
theta at 30s: 0.12218400764274975
omega at 30s: 0.7878493420830437
'''

#Q2b
#Period of oscillation found by changing graph parameters and dividing time for # waves/#waves
#Period of oscillation for the different omega conditions...

#Q2c
#The non linear periods are slightly greater than the linear periods by %
#Period of oscillation becames greater for greater initial omega conditions by %



