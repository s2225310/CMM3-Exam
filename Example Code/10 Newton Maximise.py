import numpy as np
import math
import matplotlib.pyplot as plt
def f(x):
    return x**3-6*x**2+4*x+2
x = np.linspace(-1, 1)
fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()

def fprime(x):
    return 3*x**2-12*x+4
def fsecond(x):
    return 6*x - 12
def quadratic_approx(x, x0, f, fprime, fsecond):
    return f(x0)+fprime(x0)*(x-x0)+0.5*fsecond(x0)*(x-x0)**2

x = np.linspace(-1, 1)
fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()
ax.plot(x, quadratic_approx(x, 0, f, fprime, fsecond), color='red', label='quadratic approximation')
ax.set_ylim([-2,3])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.legend()

def newton(x0, fprime, fsecond, maxiter=100, eps=0.0001):
    x=x0
    for i in range(maxiter):
        xnew=x-(fprime(x)/fsecond(x))
        if xnew-x<eps:
            return xnew
            print('converged')
            break
        x = xnew
    return x

x_star=newton(0, fprime, fsecond)
print(x_star)
fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()
ax.plot(x, quadratic_approx(x, x_star , f, fprime, fsecond), color='red', label='quadratic approximation')
ax.set_ylim([-2,3])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.axvline(x = x_star, color='green')
plt.legend()

#Valentina Alto: See: https://medium.com/swlh/optimization-algorithms-the-newton-method-4bc6728fb3b6
