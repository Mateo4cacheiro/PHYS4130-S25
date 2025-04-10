import numpy as np
import pylab as p
from scipy.integrate import odeint

def Euler_solver(N_initial, tmin, tmax, nts, deriv):
    N = np.zeros(nts)
    t = np.linspace(tmin, tmax, nts)
    
    # Note: a way of defining dt that is less error-prone
    dt = t[1] - t[0]
    N[0] = N_initial
    for it in range(0,nts-1):
        N[it+1] = N[it] + dt * deriv(N[it], t[it])
    return t, N
    
def RK2_solver(N_initial, tmin, tmax, nts, deriv):
    t = np.linspace(tmin, tmax, nts)
    dt=t[1]-t[0]
    N=np.zeros(len(t))
    N[0]=N0

    #Do Runge Kutta:
    for i in range (1,len(t)):
        N_h=N[i-1]+(dt/2)*deriv(N[i-1],t[i-1])
        N[i]=N[i-1]+dt*deriv(N_h,t[i-1])
    return(t,N)

def diffeq_solver_from_scipy(N_initial, tmin, tmax, nts, deriv):
    t = np.linspace(tmin, tmax, nts+1)
    
    # Note that the order of arguments matches the documentation
    N = odeint(deriv, N_initial, t)
    
    return t,N

