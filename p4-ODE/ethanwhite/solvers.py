from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

def Euler_solver(N0, tmin, tmax, nts, decay_deriv):
	N, t = np.zeros(nts+1), np.linspace(tmin, tmax, nts+1)
	dt = t[1] - t[0]

	N[0] = N0
	for i in range(0,nts):
		N[i+1] = N[i] + dt * decay_deriv(N[i], t[i])

	return N, t

def RK2_solver(N0, tmin, tmax, nts, decay_deriv):
	N, t = np.zeros(nts+1), np.linspace(tmin, tmax, nts+1)
	dt, dt2 = t[1] - t[0], (t[1] - t[0])/2

	Nh, th = np.zeros(nts+1), [t[i] + dt/2 for i in range(0, len(t))]
	N[0] = N0
	for i in range(0,nts):
		Nh[i] = N[i] + dt2 * decay_deriv(N[i],t[i])
		N[i+1] = N[i] + dt * decay_deriv(Nh[i],th[i])

	return N, t

def odeint_solver(N0, tmin, tmax, nts, decay_deriv):
	t = np.linspace(tmin, tmax, nts)
	N = odeint(decay_deriv, N0, t)
	return N, t

def decay_deriv(N,t):
	N1 = -(1./tau) * N
	return N1

def errorplotting(N0, tmin, tmax, nts, decay_deriv):
	nts, trueVal = 10, 0.3298505755
	error, nfinal, ntsarray, dt = np.zeros([5]), np.zeros([5]), np.zeros([5]), np.zeros([5])

	for i in range(0,5):
		ntsarray[i] = nts
		N, t = RK2_solver(N0, tmin, tmax, nts, decay_deriv)
		dt[i] = (t[1] - t[0])**2
		error[i] = abs((N[nts]-trueVal)/(trueVal))
		logE = np.log10(error)
		logt = np.log10(dt)
		plt.plot(logt,logE,'.',label="")
		nts *= 2

	plt.title("Error vs Nts")
	plt.legend()
	plt.show(block=False)
	return

tau, tmin, tmax, N0, nts = 0.7, 0.0, 4.0, 100.0, 5

N_euler, t_euler = Euler_solver(N0, tmin, tmax, nts, decay_deriv)
N_RK2, t_RK2 = RK2_solver(N0, tmin, tmax, nts, decay_deriv)
N_odeint, t_odeint = odeint_solver(N0, tmin, tmax, nts, decay_deriv)

t_analytic = np.linspace(tmin, tmax, nts+1)
N_analytic = [N0*math.exp(-t_analytic[i]/tau) for i in range(0,nts+1)]
print(N_analytic)

errorplotting(N0, tmin, tmax, nts, decay_deriv)

plt.figure()
plt.plot(t_analytic, N_analytic,label="Analytic Solution")
plt.plot(t_euler, N_euler, "*",label="Euler Solution")
plt.plot(t_RK2, N_RK2, ".",label="RK2 Solution")
plt.plot(t_odeint, N_odeint, '-',label="ODE Int Solution")

plt.legend()
plt.title("Different Integrator Methods, nts = " + str(nts))
plt.show(block=False)
