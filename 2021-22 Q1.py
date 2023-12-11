# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 12:14:41 2023

@author: Nick
"""

import numpy as np
import sympy as sym
import scipy.integrate as integrate

cm = 12
sm = 1500
coeff = [1, 2*cm, 3*sm, cm*sm, sm**2]

# Calculate the roots using numpy.roots()
roots = np.roots(coeff)

# Extract real and imaginary parts of the roots
omega_r = np.real(roots)
omega_i = np.imag(roots)

# Print the results
for i in range(len(roots)):
    print("Root {}: {:.3f} + {:.3f}i".format(i + 1, omega_r[i], omega_i[i]))

#defining constants
A = 0.1
omega_r = omega_r[2]
omega_i = omega_i[2]
phi = np.pi/8
k = 100/A #initial force/initial distance

#defining force function, F=-k*x
F = lambda t: -k*(A*np.exp(omega_r*t)*np.cos(omega_i*t+phi))

#integrate the force over the displacement to find work
w, w_error = integrate.quad(F, 0, 10)

#print results
print("work done", w)

#Q1a
#Root 1: -11.377 + 61.354i
#Root 2: -11.377 + -61.354i
#Root 3: -0.623 + 24.030i
#Root 4: -0.623 + -24.030i
#a numpy function is used to find the roots by computing the 
#eigenvalues of the companion matrix

#Q2a
#the smallest work done is 0.3330514554245878
