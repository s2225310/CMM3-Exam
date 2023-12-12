import sympy as sym
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import math

def bisection(f,a,b,N,tol):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a     # set a and b to new variables
    b_n = b     # that can change to move the domain
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2     # bisect the domain
        f_m_n = f(m_n)          # y value at midpoint
        if abs(f(m_n)) < tol:
            return [m_n, n]
        elif f(a_n)*f_m_n < 0:    # does it cross the x-axis between a_n and midpoint
            b_n = m_n           # if yes, shrink the window on the other side
        elif f(b_n)*f_m_n < 0:  # does it cross the x-axis between midpoint and b_n
            a_n = m_n           # if yes, shrink the window on the other side
        elif f_m_n == 0:        # if the midpoint exactly 0, that is a root
            print("Found exact solution.")
            return [m_n, n]
        else:                   # the root lies outside of the window 
            print("Bisection method fails.")
            return [None, n]
        

def calculate_drain_time(s, A, b, g, h_0):

    # create function for the new height of the water level
    V_s = lambda h_s : h_s*np.pi*(b+0.5*s*h_s) - h_0*np.pi*b**2

    # soped height must lie somewhere between original height and 0
    # as it solpes OUT therefore reducting the original height.
    h_sloped_0 = h_0
    if s != 0: # because it fails when a root is on a boundary
        h_sloped_0 = bisection(V_s, 0, h_0, 100, 0.001)[0]
    
    def model(z):
        dzdt = -((A*np.sqrt(2*g*z))/(np.pi*(b+s*z)))
        return dzdt



    # initial conditions
    t0 = 0
    z0 = h_sloped_0

    # total solution interval
    x_final = 100

    # step size

    h = 1

    # number of steps
    n_step = math.ceil(x_final/h)

    # Definition of arrays to store the solution
    z_eul = [0]#np.zeros(n_step+1)
    t_eul = [0]#np.zeros(n_step+1)

    # initial condition
    z_eul[0] = z0
    t_eul[0] = t0 


    # Apply Euler method n_step times
    for i in range(n_step):
        # compute the slope using the differential equation
        slope = model(z_eul[i]) 
        # use the Euler method
        t_eul.append(t_eul[i]  + h)
        z_eul.append(z_eul[i] + h * slope) 
        if z_eul[-1] <= 0.0001:
            break
    return t_eul[-1]

A = 0.03
b = 1
g = 9.81
h_0 = 1

time_no_slope = time = calculate_drain_time(0, A, b, g, h_0)

durations = []
s_vals = []
s = 0
time_with_slope = 0
first_run = True 
while time_with_slope <= 2*time_no_slope:
    first_run = False
    time_with_slope = calculate_drain_time(s, A, b, g, h_0)
    durations.append(time_with_slope)
    s_vals.append(s)
    s += 1
print() 
print(f"time is doubled from {durations[0]:.2f}s to {durations[-1]:.2f}s at a slope of {s_vals[-1]:.2f}")

fig, ax = plt.subplots()

ax.plot(s_vals, durations)
ax.set_xlabel('Slope')
ax.set_ylabel('Drain time duration')
ax.set_xlim(0, max(s_vals))
ax.set_ylim(0, max(durations))
plt.show()

print(f"time is doubled from {durations[0]:.2f}s to {durations[-1]:.2f}s at a slope of {s_vals[-1]:.2f}")

# ------------------------------------------------------
