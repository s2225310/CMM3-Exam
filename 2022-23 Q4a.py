# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:20:19 2023

@author: Jason
"""

from sympy import Function, dsolve, Eq, Derivative, symbols

# Define symbols
t, m, b, k = symbols('t m b k')
x = Function('x')

# Define the differential equation for a mass-spring-damper system
diff_eq = Eq(m * Derivative(x(t), t, t) + b * Derivative(x(t), t) + k * x(t), 0)

# Solve the differential equation
solution = dsolve(diff_eq)

# Print the general solution
print("Solution:")
print(solution)

#Q1a
#By solving the differential equation 4.1 with the dsolve function
#the solution is x(t) = C1*exp(t*(-b + sqrt(b**2 - 4*k*m))/(2*m)) + C2*exp(-t*(b + sqrt(b**2 - 4*k*m))/(2*m)))
#which is of the form of the general solution when rearranged


"""
Created on Wed Dec  6 15:41:58 2023

@author: Ben

from sympy import symbols, diff, cos, exp, sqrt, Eq, solve, Function, init_printing
import math
import numpy as np

A0, b, m, t, w, k , phi  = symbols('A0 b m t w k phi')

#define eq 4.1 and differentials
x_function = Function('x')(t)
equation_42 = Eq(x_function, A0*exp(-b*t/2*m)*cos(w*t+phi))
dx_dt = diff(x_function, t)
d2x_dt2 = diff(dx_dt, t)

#solve and simplify for eq 4.1
equation_41 = Eq(0,  m*d2x_dt2 + b*dx_dt + k*equation_42.rhs)
equation_41_simplified = equation_41.simplify()

#solve eq 4.1 for Ao
solutions_for_A0 = solve(equation_41_simplified, A0)
print("eq 4.1",equation_41_simplified)
print()
print("solutions for Ao",solutions_for_A0)

#somehow compares and checks if it's the general solution
if all(equation_41_simplified.subs(A0, sol).simplify() == True for sol in solutions_for_A0):
    print("Equation 1B is the general solution to Equation 1A.")
else:
    print("Equation 1B is not the general solution to Equation 1A.")
"""  


"""
#DOESNT WORK

from sympy import Function, dsolve, Eq, Derivative, symbols, cos, exp, sqrt
from sympy.abc import A, alpha, w

# Define symbols
t, m, b, k = symbols('t m b k')
x = Function('x')

# Given solution
A, alpha, w = symbols('A alpha w')
x_t = A * exp(-b/(2*m) * t) * cos(w * t + alpha)

# Define the relations
omega = sqrt(k/m)
damping_ratio = b/(2*m*omega)

# Substitute into the given solution
x_t = x_t.subs({w: omega, b/(2*m): damping_ratio})

# Differentiate x(t) with respect to t
dx_dt = x_t.diff(t)
dx2_dt2 = x_t.diff(t, 2)

# Substitute x(t), dx/dt, and d^2x/dt^2 into the dynamics equation
dynamics_eq = m * dx2_dt2 + b * dx_dt + k * x_t

# Simplify the result
dynamics_eq_simplified = dynamics_eq.simplify()

# Display the results
print("Given solution:")
print(x_t)

print("\nFirst derivative:")
print(dx_dt)

print("\nSecond derivative:")
print(dx2_dt2)

print("\nDynamics equation:")
print(dynamics_eq_simplified)
"""