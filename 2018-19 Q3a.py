# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:49:22 2023

@author: Nick
"""

def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

f = lambda x: x**2 + 10*x + 25
df= lambda x: 2*x + 10
x0=1
epsilon=0.0000001
max_iter=100
solution = newton(f,df,x0,epsilon,max_iter)
print(solution)

#Q3a
#Using the Newton Raphson method the roots are found at x=-5
