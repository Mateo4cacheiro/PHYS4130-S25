# Author: Adam Grice
# Project: Ordinary Differential Equations
# Date: 04-22-2025

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def rk4(p0, x0, tmin, tmax, nts):
    t_array = np.linspace(tmin, tmax, nts, endpoint=False)  
    dt = t_array[1] - t_array[0]

    p_array = np.zeros_like(t_array)
    x_array = np.zeros_like(t_array)

    p_array[0] = p0
    x_array[0] = x0

    for i in range(0, len(t_array)-1):
        j1 = p_array[i]
        k1 = -(x_array[i])

        j2 = p_array[i] + dt * 0.5 * j1
        k2 = -(x_array[i] + dt * 0.5 * k1)

        j3 = p_array[i] + dt * 0.5 * j2
        k3 = -(x_array[i] + dt * 0.5 * k2)

        j4 = p_array[i] + dt * j3
        k4 = -(x_array[i] + dt * k3)

        p_array[i+1] = p_array[i] + (1.0/6.0)*(k1 + 2*k2 + 2*k3 + k4)
        x_array[i+1] = x_array[i] + (1.0/6.0)*(j1 + 2*j2 + 2*j3 + j4)

    return p_array, x_array, t_array

def verlet(x0, tmin, tmax, nts):
    t_array = np.linspace(tmin, tmax, nts, endpoint=False)  
    dt = t_array[1] - t_array[0]

    x_array = np.zeros_like(t_array)
    x_array[0] = x0

    for i in range(0, len(t_array)-1):
        x_array[i+1] = 2*x_array[i] - x_array[i-1] - x_array[i]*(dt**2)

    return x_array, t_array



def eqns(state, t):
    x, v = state
    dx = v
    dv = -x
    return [dx, dv]

t = np.linspace(0, 50, 100, endpoint=False)
initial = [2, 2]

soln = odeint(eqns, initial, t)

x_scipy = soln[:, 0]
p_scipy = soln[:, 1]


xv, tv = verlet(2, 0, 50, 100)

pr, xr, tr = rk4(2, 2, 0, 50, 100)


plt.plot(tr, pr, 'x:', label = 'momentum rk4')
plt.legend()
plt.show()
plt.plot(tr, xr, '.:', label = 'position rk4')
plt.legend()
plt.show()
plt.plot(tv, xv, '3:', label = 'position verlet')
plt.legend()
plt.show()
plt.plot(t, x_scipy, '4:', label='position linear multistep')
plt.legend()
plt.show()
plt.plot(t, p_scipy, '2:', label='momentum linear multistep')

plt.legend()
plt.show()

Er = (pr**2) + (xr**2)
Es = (x_scipy**2) + (p_scipy**2)
plt.plot(tr, Er/2, '.:', label = 'energy rk4')
plt.legend()
plt.show()
plt.plot(t, Es/2, ',:', label = 'energy linear multistep')

plt.legend()
plt.show()

plt.plot(xr, pr, '.:', label = 'momentum vs. position rk4')
plt.legend()
plt.show()
plt.plot(x_scipy, p_scipy, 'x:', label = 'momentum vs. position linear multistep')
plt.legend()
plt.show()