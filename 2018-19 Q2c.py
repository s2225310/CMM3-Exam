# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 17:33:41 2023

@author: Nick
"""

# Fixed Point Iteration Method
# Importing math to use sqrt function
import math

# Input Section
x0 = 0.05
e = 1e-3
N = 100

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Fixed Point Iteration Method
# Importing math to use sqrt function
import math

def f(x):
    return 150*(1-x)/500 + 1.75 - 20*x**3/(1-x)

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return ((150*(1-x)/500 + 1.75) * (1-x)/20)**(1/3)

    
# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)

# Starting Newton Raphson Method
fixedPointIteration(x0,e,N)

#Qc
#The porosity is 0.38930547