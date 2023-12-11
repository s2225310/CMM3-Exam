# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:25:48 2023

@author: Nick
"""
import numpy as np 
from matplotlib import pyplot as plt 

ao = 0.05
b = 0.1
m = 1
wo = 5
phi = 0

w = np.sqrt(wo**2-(b/(2*m))**2)
t = np.arange(0, 100, 0.1)
x = np.arange(0, 100, 0.1)
#x = np.linspace(0,999,1000)

for i in range(1000):
    x[i] = ao * np.exp(-(b*t[i]/(2*m))) * np.cos(wo*t[i]+phi)

fig = plt.figure(1)    
plt.plot(t[700:], x[700:], '-')
plt.axhline(y=0.01*ao)


# Q4c
# by inspection of the graph and changing plotting boundaries
# the time taken to reach 0.01*Ao is 92s
# this could also be found by reading x where t is a multiple of 2pi/5 and checking...

# Q4d
# b = 0.2 is required to half the time for the amplitude to reach 0.01*Ao

#-----------------------------------------------------------------------

#Q4c can also be solved by rearranging eq
#equation of damped frequency is wd = sqrt(w0^2 - (b/2m)^2)

#theta(t) = A*exp(-bt/2m)
#time solved for reduction to 1% of original size of amplitude
##Only interested in amplitude, 0.01 = exp(-b/2m * t) = ln(0.01) = -b/2m * t

#by rearranging eqn: t = 2m * ln(0.01)/0.1

delta_t = 2 * m *np.log(0.01)/-b
print("time to reach 1% oscillation amplitude",delta_t)

#To halve the time simply use the same equation with b as unknown and time as 92.1034/2
time = delta_t/2
b = -2 * m *np.log(0.01)/time
print("damping ratio required is", b)