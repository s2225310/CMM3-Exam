# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:51:55 2020

@author: emc1977
"""

def adaptive_simpson( f, a, b, tol ):
    """
    Evaluates the integral of f(x) on [a,b].

    USAGE:
        s = adaptive_simpson( f, a, b, tol )

    INPUT:
        f         - function to integrate
        a, b      - left and right endpoints of interval of integration
        tol       - desired upper bound on allowable error

    OUTPUT:
        float     - the value of the integral

    NOTES:
        Integrates the function f(x) on [a,b] with an error bound of
        given by tol using an adaptive Simpson's rule to approximate
        the value of the integral.  Notice that this is not very
        efficient -- it is recursive and recomputes many function
        values that have already been computed.  The code in this
        function is meant to be clear and explain the ideas behind
        adaptive schemes rather than to be an efficient implementation
        of one.

    AUTHOR:
        Jonathan Senning <jonathan.senning@gordon.edu>
        Gordon College, Department of Mathematics and Computer Science
        Written in Octave February 19, 1999
        Converted to Python March 5, 2008
    """

    # Theory says the factor to multiply the tolerance by should be 15, but
    # since that assumes that the fourth derivative of f is fairly constant,
    # we want to be a bit more conservative...
    
    tol_factor = 10

    h = 0.5 * ( b - a )

    x0 = a
    x1 = a + 0.5 * h
    x2 = a + h
    x3 = a + 1.5 * h
    x4 = b

    f0 = f( x0 )
    f1 = f( x1 )
    f2 = f( x2 )
    f3 = f( x3 )
    f4 = f( x4 )

    s0 = h * ( f0 + 4.0 * f2 + f4 ) / 3.0
    s1 = h * ( f0 + 4.0 * f1 + 2.0 * f2 + 4.0 * f3 + f4 ) / 6.0

    if abs( s0 - s1 ) >= tol_factor * tol:
        s = adaptive_simpson( f, x0, x2, 0.5 * tol ) + \
            adaptive_simpson( f, x2, x4, 0.5 * tol )
    else:
        s = s1 + ( s1 - s0 ) / 15.0
        print(s0, s1)
    return s

import numpy as np

def f(x):
    return np.exp(-x**2)

print(adaptive_simpson(f,0,10,1e-6))
