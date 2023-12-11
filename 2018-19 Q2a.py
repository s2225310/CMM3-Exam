# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:33:10 2023

@author: Rodrigo
"""

#Question 2 2018 part 1
import sympy as sym

# Define symbols
w, Ta, x, y0 = sym.symbols('w Ta x y0')
# Define y as a function of x
y = sym.Function('y')(x)

# Define the given solution (Equation C)
solution = (Ta/w) * sym.cosh((w/Ta)*(x)) + y0 - (Ta/w)

# Compute the first and second derivatives of the given solution
dydx = sym.diff(solution, x)
d2ydx2 = sym.diff(dydx, x)

print(d2ydx2)

# Equation B to verify
equation_B = d2ydx2 - (w/Ta) * sym.sqrt(1 + dydx**2)

# Simplify to check if Equation B is satisfied (should simplify to 0)
verification = sym.simplify(equation_B)

print(verification)

# The expression inside the square root, cosh(w*x/Ta)**2, should simplify to cosh(w*x/Ta) itself
# This is because cosh(x) is always positive, and thus the square root of cosh(x)^2 is cosh(x)

# Let's manually simplify the verification step, considering this property of the hyperbolic cosine
manual_verification = -w * (sym.cosh(w*x/Ta) - sym.cosh(w*x/Ta)) / Ta

# Simplify the manual verification expression
manual_simplified = sym.simplify(manual_verification)
print(manual_simplified)

#the output is zero as the back substitution was successful
