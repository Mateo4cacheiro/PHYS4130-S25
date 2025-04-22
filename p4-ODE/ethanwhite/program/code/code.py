import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
import numpy as np
import math

def Verlet_solver(tmin, tmax, nts, v0, y0, m, k, b):
	t = np.linspace(tmin, tmax, nts + 1)
	y_pos, y_vel, dt = np.zeros(len(t)), np.zeros(len(t)), t[1] - t[0] # declaring arrays, dt

	y_pos[0], y_vel[0] = y0, v0 # setting initial conditions
	y_pos[1] = y_pos[0] + y_vel[0]*dt + (y_accel(y_pos[1], y_vel[0], m, k, b)*dt**2)/2 # stromers method requires y[0] and y[i]
	for i in range(1, nts):
		y_pos[i+1] = 2*y_pos[i]-y_pos[i-1]+y_accel(y_pos[i], y_vel[i-1], m, k, b)*dt**2 # Stromer's method
		y_vel[i] = (y_pos[i+1]-y_pos[i-1])/(2*dt) # finite difference approx for first deriv of y

#	y_vel[nts] = ((2*y_pos[nts-1]+y_vel[nts-1]*dt + (y_accel(y_pos[nts],y_vel[nts-1], m, k, b)*dt**2)/2)-y_pos[nts-2])/(2*dt)
	y_vel[nts] = y_vel[nts-1]

	U = potential(t, y_pos, k)
	T = kinetic(t, y_vel, m)
	H = T + U

	return t, y_pos, y_vel, H

def RK45_solver(tmin, tmax, nts, v0, y0, k, m, f):
	w = np.sqrt(k/m)
	initials, time = [y0, v0], [tmin, tmax]
	t = np.linspace(tmin, tmax, nts+1)

	RK45 = solve_ivp(f, time, initials, args=(w,), t_eval=t, method='RK45')
	y_pos, y_vel = RK45.y[0], RK45.y[1]

	U = potential(t, y_pos, k)
	T = kinetic(t, y_vel, m)
	H = T + U

	return t, y_pos, y_vel, H

def Adams_solver(tmin, tmax, nts, v0, y0, k, m, f):
	w = np.sqrt(k/m)
	initials, time = [y0, v0], [tmin, tmax]
	t = np.linspace(tmin, tmax, nts+1)

	Adams = solve_ivp(f, time, initials, args=(w,), t_eval=t, method='LSODA')
	y_pos, y_vel = Adams.y[0], Adams.y[1]

	U = potential(t, y_pos, k)
	T = kinetic(t, y_vel, m)
	H = T + U

	return t, y_pos, y_vel, H

def y_accel(y,v,m,k,b):
	a = -(k*y+b*v)/m
	return a

def potential(t,y,k):
	potential = np.array([1/2 * k * y[i] ** 2 for i in range(0,len(t))])
	return potential

def kinetic(t,v,m):
	kinetic = np.array([1/2 * m * v[i] ** 2 for i in range(0,len(t))])
	return kinetic

def ODE(t, y, w):
	x, v = y
	return [v, -x * w**2]

def plotphasespaces(m,y_verlet,y_rk45,y_adams,v_verlet,v_rk45,v_adams):
	plt.figure()
	plt.plot(y_verlet,m*v_verlet,'.',label="Verlet Phase")
	plt.plot(y_rk45,m*v_rk45,'.',label="RK45 Phase")
	plt.plot(y_adams,m*v_adams,'.',label="Adams' Phase")

	plt.title("Phase Space Diagram")
	plt.xlabel("Position [m]")
	plt.ylabel("Momentum [kg*m/s]")
	plt.legend()
	plt.show(block=False)
	return

def plothamiltonian(tmin,tmax,nts,verlet,rk45,adams):
	t = np.linspace(tmin, tmax, nts+1)

	plt.plot(t,verlet,'.',label="Verlet Hamiltonian")
	plt.plot(t,rk45,'.',label="RK45 Hamiltonian")
	plt.plot(t,adams,'.',label="Adams Hamiltonian")

	plt.title("Hamiltonian vs. Time")
	plt.xlabel("Time [s]")
	plt.ylabel("Hamiltonian [J]")
	plt.xlim(tmin,tmax)
	plt.legend()
	plt.show(block=False)
	return

def plotpositions(tmin,tmax,nts,verlet,rk45,adams):
	t = np.linspace(tmin, tmax, nts+1)
	plt.figure()

	plt.plot(t,verlet,'.',label="Verlet Position")
	plt.plot(t,rk45,'.',label="RK45 Position")
	plt.plot(t,adams,'.',label="Adams Position")

	plt.title("Position vs. Time")
	plt.xlabel("Time [s]")
	plt.ylabel("Position [m]")
	plt.xlim(tmin,tmax)
	plt.legend()
	plt.show(block=False)
	return

def dampening(tmin, tmax, nts, v0, y0, m, k, b):
	nts = 5000
	tmax = 25

	plt.figure()
	for i in range(0,5):
		t,y,v,E = Verlet_solver(tmin, tmax, nts, v0, y0, m, k, b)
		plt.plot(y,m*v,'.',label="Verlet, Dampening = " + f"{b:.1f}")
		b += 0.2

	plt.title("Phase Space Diagram")
	plt.xlabel("Position [m]")
	plt.ylabel("Momentum [kg*m/s]")
	plt.legend()
	plt.show(block=False)

	b = 0.0
	plt.figure()
	for i in range(0,5):
		t,y,v,E = Verlet_solver(tmin, tmax, nts, v0, y0, m, k, b)
		plt.plot(t,y,'.',label="Verlet, Dampening = " + f"{b:.1f}")
		b += 0.2

	plt.title("Position vs. Time")
	plt.xlabel("Time [s]")
	plt.ylabel("Position [m]")
	plt.legend()
	plt.show(block=False)

	b = 0.0
	plt.figure()
	for i in range(0,5):
		t,y,v,E = Verlet_solver(tmin, tmax, nts, v0, y0, m, k, b)
		plt.plot(t,E,'.',label="Verlet, Dampening = " + f"{b:.1f}")
		b += 0.2

	plt.title("Hamiltonian vs. Time")
	plt.xlabel("Time[s]")
	plt.ylabel("Hamiltonian [J]")
	plt.legend()
	plt.show(block=False)
	return


tmin, tmax, nts, v0, y0, m, k, b, func = 0.0, 25.0, 300, 0.0, 1.0, 1.0, 1.0, 0.0, ODE

t_verlet, y_verlet, v_verlet, E_verlet = Verlet_solver(tmin, tmax, nts, v0, y0, m, k, b)
t_rk45, y_rk45, v_rk45, E_rk45 = RK45_solver(tmin, tmax, nts, v0, y0, k, m, func)
t_adams, y_adams, v_adams, E_adams = Adams_solver(tmin, tmax, nts, v0, y0, k, m, func)

plothamiltonian(tmin,tmax,nts,E_verlet,E_rk45,E_adams)
#plotpositions(tmin,tmax,nts,y_verlet,y_rk45,y_adams)
plotphasespaces(m,y_verlet,y_rk45,y_adams,v_verlet,v_rk45,v_adams)

#dampening(tmin,tmax,nts,v0,y0,m,k,b)
