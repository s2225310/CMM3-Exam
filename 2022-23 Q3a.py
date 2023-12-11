# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 18:41:19 2023

@author: Nick
"""
import numpy as np
from matplotlib import pyplot as plt 

# Fixed Point Iteration Method
# Importing math to use sqrt function
import math
import numpy as np

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
    return 1/np.sin(x) + 0.25 - x

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 1/np.sin(x) + 0.25
    
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
e = 0.0001
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

#Q3a
#the value of x in the domain is 1.29056173


'''
#by solving a 100 iterations of the function for different initial
#inputs it can be observed the function eventually tends to 
#different values where xn = xn+1

#we can define two arrays to store the initial and final outputs

x_initial = np.arange(0.01,np.pi,0.01)
x_final = np.arange(0.01,np.pi,0.01)

#we can run a loop for the size of the array and for each loop
#run 100 iterations for the initial value in the array
#and store the final value from that iteration

for i in range(x_initial.size):
    x_value = x_initial[i]
    for j in range(5):
        x_value = 1/np.sin(x_value) + 1/4
    x_final[i] = x_value
    print(i,x_initial[i],x_final[i])

# plots the range of final iterations for initial inputs
#we can observe the iterative function tends to two values
#around -0.9 and 1.3
plt.plot(x_initial, x_final, '.')

#Q3a
#the value of x in the domain is 1.29
'''
