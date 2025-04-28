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
    N[0]=N_initial

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

def Verlet_solver(Pos0, Vel0, tmin, tmax, nts, Acel):
    t = np.linspace(tmin, tmax, nts)
    Pos = np.zeros(len(t))
    Vel = np.zeros(len(t))
    dt= t[1]-t[0]

    #Do Verlet for position
    Pos[0]=Pos0
    Pos[1]=Pos[0]+Vel0*dt+0.5*Acel(Pos[0])*dt**2
    for i in range(1,len(t)-1):
        Pos[i+1]= 2*Pos[i]-Pos[i-2]+Acel(Pos[i])*dt**2
    
    #Find Velocities from Position
    Vel[0]=Vel0
    for i in range(1,len(t)-1):
        Vel[i]=(Pos[i-1]-Pos[i+1])/(2*dt)

    return(t, Pos, Vel)

def acceleration(x):
    k=1
    m=1
    return(-1*k/m*x)

Pos0=0
Vel0=5
Acel=acceleration
tmin=0
tmax=10
nts=1000
t, Verlet_P, Verlet_V = Verlet_solver(Pos0, Vel0, tmin, tmax, nts, Acel)

p.plot(t, Verlet_P)
p.show



