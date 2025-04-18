import numpy as np
import pylab as p
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

def Verlet_solver(Pos0, Vel0, tmin, tmax, nts, Acel,m,k,c):
    t = np.linspace(tmin, tmax, nts)
    Pos = np.zeros(len(t))
    Vel = np.zeros(len(t))
    dt= t[1]-t[0]

    #Do Verlet for position
    Pos[0]=Pos0
    Vel[0]=Vel0
    Pos[1]=Pos[0]+Vel0*dt+0.5*Acel(Pos[0],Vel[0],m,k,c)*dt**2
    for i in range(1,nts-1):
        Pos[i+1]= 2*Pos[i]-Pos[i-1]+Acel(Pos[i],Vel[i-1],m,k,c)*dt**2
        Vel[i]=(Pos[i+1]-Pos[i-1])/(2*dt)
    nextPos= 2*Pos[nts-1]-Pos[nts-2]+Acel(Pos[nts-1],Vel[nts-2],m,k,c)*dt**2
    Vel[len(t)-1]=(nextPos-Pos[len(t)-2])/(2*dt)    

    return(t, Pos, Vel)

def acceleration(x,v,m,k,c):
    return((1/m)*(-k*x-c*v))

# Define the system of equations
def ODE(t, y, w):
    x, v = y
    return [v, -w**2*x]

def Find_Kin(t,V,m):
    T = np.zeros(len(t))
    for i in range(0,len(t)):
        T[i]=0.5*m*V[i]**2
    return(T)

def Find_Pot(t,x,m):
    U = np.zeros(len(t))
    for i in range(0,len(t)):
        U[i]=0.5*k*x[i]**2
    return(U)

Pos0=1
Vel0=0
Acel=acceleration
c=0
m=1
k=1
tmin=0
tmax=20
nts=10000

#Solve using Verlet
t_V, Verlet_P, Verlet_V = Verlet_solver(Pos0, Vel0, tmin, tmax, nts, Acel,m,k,c)
T_V=Find_Kin(t_V,Verlet_V,m)
U_V=Find_Pot(t_V,Verlet_P,k)

#plot position using Verlet
p.plot(t_V, Verlet_P, label="Verlet")
p.xlabel("Time [s]")
p.ylabel("Position [m]")
p.ylim(-Pos0-0.1,Pos0+0.1)
p.title("Position vs. Time")
p.legend()
p.savefig('Position_Verlet.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot simple harmonic oscillator's velocity using Verlet
p.plot(t_V, Verlet_V, label="Verlet")
p.xlabel("Time [s]")
p.ylabel("Velocity [m/s]")
p.title("Velocity vs. Time")
p.legend()
p.savefig('Velocity_Verlet.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot simple harmonic oscillator in phasespace using Verlet
p.plot(Verlet_P, Verlet_V*m, label="Verlet")
p.xlabel("Position [m]")
p.ylabel("Momentum [kg*m/s]")
p.title("Position vs. Momentum (Phase space Diagram)")
p.legend()
p.savefig('Phasespace_Verlet.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot simple harmonic oscillator's Hamiltonian using Verlet
p.plot(t_V, T_V+U_V, label="Verlet")
p.xlabel("Time [s]")
p.ylabel("Hamiltonian [J]")
p.title("Hamiltonian vs. Time")
p.ylim(0,2*(T_V[0]+U_V[0]))
p.legend()
p.savefig('Hamiltonian_Verlet.png', bbox_inches='tight', pad_inches=0)
p.show()

#Solve using Scipy integrators
w = np.sqrt(k/m)  # Angular frequency
initial_P_and_V = [Pos0, Vel0]  # Initial position and velocity
time = [tmin, tmax]  # Time interval

# Solve the system using RK45
t_RK45 = np.linspace(time[0], time[1], nts)  # Time points for solution
RK45_Integrator = solve_ivp(ODE, time, initial_P_and_V, args=(w,), t_eval=t_RK45, method='RK45')

# Extract the solution
P_RK45 = RK45_Integrator.y[0]
V_RK45 = RK45_Integrator.y[1]
T_RK45=Find_Kin(t_RK45,V_RK45,m)
U_RK45=Find_Pot(t_RK45,P_RK45,k)

# Solve the system using RK23
t_RK23 = np.linspace(time[0], time[1], nts)  # Time points for solution
RK23_Integrator = solve_ivp(ODE, time, initial_P_and_V, args=(w,), t_eval=t_RK23, method='RK23')

# Extract the solution
P_RK23 = RK23_Integrator.y[0]
V_RK23 = RK23_Integrator.y[1]
T_RK23=Find_Kin(t_RK23,V_RK23,m)
U_RK23=Find_Pot(t_RK23,P_RK23,k)

# plot position using RK23
p.plot(t_RK23, P_RK23, label='RK23')
# plot position using RK45
p.plot(t_RK45, P_RK45, label='RK45')
#plot position using Verlet
p.plot(t_V, Verlet_P, label="Verlet")
p.xlabel("Time [s]")
p.ylabel("Position [m]")
p.ylim(-Pos0-0.1,Pos0+0.1)
p.title("Position vs. Time")
p.legend()
p.savefig('Position_All.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot simple harmonic oscillator's velocity using RK23
p.plot(t_RK23, V_RK23, label="RK23")
#plot simple harmonic oscillator's velocity using RK45
p.plot(t_RK45, V_RK45, label="RK45")
#plot simple harmonic oscillator's velocity using Verlet
p.plot(t_V, Verlet_V, label="Verlet")
p.xlabel("Time [s]")
p.ylabel("Velocity [m/s]")
p.title("Velocity vs. Time")
p.legend()
p.savefig('Velocity_All.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot simple harmonic oscillator in phasespace using RK23
p.plot(P_RK23, V_RK23*m, label="RK23")
#plot simple harmonic oscillator in phasespace using RK45
p.plot(P_RK45, V_RK45*m, label="RK45")
#plot simple harmonic oscillator in phasespace using Verlet
p.plot(Verlet_P, Verlet_V*m, label="Verlet")
p.xlabel("Position [m]")
p.ylabel("Momentum [kg*m/s]")
p.title("Position vs. Momentum (Phase space Diagram)")
p.legend()
p.savefig('Phasespace_All.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot simple harmonic oscillator's Hamiltonian using RK23
p.plot(t_RK23, T_RK23+U_RK23, label="RK23")
#plot simple harmonic oscillator's Hamiltonian using RK45
p.plot(t_RK45, T_RK45+U_RK45, label="RK45")
#plot simple harmonic oscillator's Hamiltonian using Verlet
p.plot(t_V, T_V+U_V, label="Verlet")
p.xlabel("Time [s]")
p.ylabel("Hamiltonian [J]")
p.title("Hamiltonian vs. Time")
p.legend()
p.savefig('Hamiltonian_All.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot position for different dampening ratios using Verlet
for i in range(0,4):
    c=i
    t_V, Verlet_P, Verlet_V = Verlet_solver(Pos0, Vel0, tmin, tmax, nts, Acel,m,k,c)
    R=(c)/(2*np.sqrt(m*k))
    p.plot(t_V, Verlet_P/Verlet_P[0], label="Verlet w/ Damping Ratio = "+str(R))
p.xlabel("Time [s]")
p.ylabel("x(t)/x(0)")
p.ylim(-1.1,1.1)
p.title("Position vs. Time")
p.legend()
p.savefig('Dampened_Position_Verlet.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot phasespace for different dampening ratios using Verlet
for i in range(0,4):
    c=i
    t_V, Verlet_P, Verlet_V = Verlet_solver(Pos0, Vel0, tmin, tmax, nts, Acel,m,k,c)
    R=(c)/(2*np.sqrt(m*k))
    p.plot(Verlet_P, m*Verlet_V, label="Verlet w/ Dampening Ratio = "+str(R))
p.xlabel("Position [m]")
p.ylabel("Momentum [kg*m/s]")
p.ylim(-1.1,1.1)
p.title("Phasespace")
p.legend()
p.savefig('Dampened_Phasespace_Verlet.png', bbox_inches='tight', pad_inches=0)
p.show()

#plot Hameltonian for different dampening ratios using Verlet
for i in range(0,4):
    c=i
    t_V, Verlet_P, Verlet_V = Verlet_solver(Pos0, Vel0, tmin, tmax, nts, Acel,m,k,c)
    R=(c)/(2*np.sqrt(m*k))
    T=Find_Kin(t_V,Verlet_V,m)
    U=Find_Pot(t_V,Verlet_P,k)
    p.plot(t_V, T+U, label="Verlet w/ Dampening Ratio = "+str(R))
p.xlabel("time [s]")
p.ylabel("Hamiltonian [J]")
p.ylim(0,(T[0]+U[0])+0.1)
p.title("Hamiltonian vs. time")
p.legend()
p.savefig('Dampend_Hamiltonian_Verlet.png', bbox_inches='tight', pad_inches=0)
p.show()

