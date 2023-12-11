# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:10:35 2023

@author: Nick
"""

#Q3a
#The algorithm is the false position which projects two triangles
#over the interval bound to represent the function
#and estimates the root from the common point of the triangles
#with the boundaries of the triangles adjusted over iterations
#and converging on a root

from scipy.optimize import fsolve

MAX_ITER = 1000000
MAX_ITER = 100
def func(x): #mispelt def
    #return (x**3 - 4*(x*2) + 10)
    return (x**2 + 5*(x) - 4)

def Code(a, b): #wrong initial parameters and syntax
    if func(a) * func(b) >= 0: #changed inequality symbol
        print("You have not assumed correct values of a and b")
        return 0
    for i in range(MAX_ITER):
        c = (a * func(b) - b * func(a))/ (func(b) - func(a)) #equation uses wrong variables in places
        if func(c) == 0: # wrong variables
            break
        elif func(c) * func(a) < 0:
            b = c # wrong variables
        else:
            a = c
    print("The value of root is : " , '%.4f' %c)
    return c
    
#true roots found using fsolve
#error found from root- true root/true root * 100

true_root1 = fsolve(func,1)
true_root2 = fsolve(func,-5)
root1 = Code(0,5)
error1 = abs((root1-true_root1)/root1)*100
print("error",error1)
root2 = Code(-10,-5)
error2 = abs((root2-true_root2)/root2)*100
print("error",error2)

#Q3d 
#Newton raphson would find an improved approximation under
#fewer iterations