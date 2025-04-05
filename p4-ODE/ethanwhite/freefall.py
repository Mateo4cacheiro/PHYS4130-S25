import numpy as np
import matplotlib.pyplot as plt

def freefall(t, y0, v0, g, beta):
	height, velocity = np.zeros([len(t)]), np.zeros([len(t)])
	height[0], velocity[0] = y0, v0
	dt = t[1]-t[0]

	for it in range(0,len(height)-1):
		height[it+1] = height[it] + velocity[it]*dt
		velocity[it+1] = velocity[it] + (-g - beta)*dt

	return height

def freefallanalytic(t, y0, v0, g, beta):
	height, velocity = np.zeros([len(t)]), np.zeros([len(t)])
	height[0], velocity[0] = y0, v0

	for it in range(0,len(height)-1):
		height[it+1] = height[0] + velocity[0]*(t[it+1])-(g*t[it+1]**2)/2

	return height

def plot(tmax, tmin, y0, v0, g, beta):
	tmax, yfinal = np.zeros([5]), -21.92
	nts = 20
	for k in range(0,5):
		t = [i/(nts / (tmax - tmin)) for i in range(0,nts)]
		t.append(8.0)
		plt.plot(t,freefall(t, y0, v0, g, beta),'*',label="Euler Path, nts = "+str(nts))
		tmax[k] = freefall(t, y0, v0, g, beta)[nts]
		nts *= 2

	error = [abs((tmax[i]-yfinal)/yfinal) for i in range(0,5)]
	print(error)

	h0 = [y0 for i in range(0,len(t))]
	plt.plot(t,freefallanalytic(t, y0, v0, g, beta),'-',label="Analytic Path")
	plt.plot(t, h0, y0, v0, g, beta,'-')
	plt.plot(t, np.zeros([len(t)]), y0, v0, g, beta,'-')

	plt.legend()
	plt.title("Freefall Simulation")
	plt.xlim(tmin,tmax)
	plt.show(block=False)
	return

y0, v0, g, beta, tmin, tmax, nts = 12.0, 35.0, 9.8, 0, 0, 8, 200

t = [i/(nts / (tmax-tmin)) for i in range(0,nts)]
t.append(8.0)

y_euler = freefall(t, y0, v0, g, beta)
y_analytic = freefallanalytic(t, y0, v0, g, beta)

plot(tmax,tmin, y0, v0, g, beta)


