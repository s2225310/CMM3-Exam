# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:33 2020

@author: emc1977
"""
# Fixed Point Iteration Method
# Importing math to use sqrt function
import math

# Input Section
x0 = 0
e = 1e-3
N = 1000

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Fixed Point Iteration Method
# Importing math to use sqrt function
import math

def f(x):
    return x**2 -5*x + 6

# Rearrange f(x)=0 to x = g(x)
def g(x):
    return (x**2+6)/5
    
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

# Input Section
x0 = 1
e = 0.01
N = 100

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)


#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
fixedPointIteration(x0,e,N)