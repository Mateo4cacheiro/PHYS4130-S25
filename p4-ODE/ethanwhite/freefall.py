import numpy as np
import matplotlib.pyplot as plt

def freefallheight(t, y0, v0, g, beta):
	height, velocity = np.zeros([len(t)]), np.zeros([len(t)])
	height[0], velocity[0] = y0, v0
	dt = t[1]-t[0]

	for it in range(0,len(height)-1):
		height[it+1] = height[it] + velocity[it]*dt
		velocity[it+1] = velocity[it] + (-g - beta)*dt

	return height

def freefallvelocity(t, y0, v0, g, beta):
	height, velocity = np.zeros([len(t)]), np.zeros([len(t)])
	height[0], velocity[0] = y0, v0
	dt = t[1]-t[0]

	for it in range(0,len(height)-1):
		height[it+1] = height[it] + velocity[it]*dt
		velocity[it+1] = velocity[it] + (-g - beta)*dt

	return velocity

def freefallanalytic(t, y0, v0, g, beta):
	height, velocity = np.zeros([len(t)]), np.zeros([len(t)])
	height[0], velocity[0] = y0, v0

	for it in range(0,len(height)-1):
		height[it+1] = height[0] + velocity[0]*(t[it+1])-(g*t[it+1]**2)/2

	return height

def plot(tmax, tmin, y0, v0, g, beta):
	dtarray, tmaxarray, yfinal = np.zeros([5]), np.zeros([5]), -21.92
	beta, nts = 0, 20
	for k in range(0,5):
		t = [i/(nts / (tmax - tmin)) for i in range(0,nts)]
		t.append(8.0)
		plt.plot(t,freefallheight(t, y0, v0, g, beta),'*',label="Euler Path, nts = "+str(nts))
		tmaxarray[k] = freefallheight(t, y0, v0, g, beta)[nts]
		dtarray[k] = t[1]-t[0]
		nts *= 2

	h0 = [y0 for i in range(0,len(t))]
	plt.plot(t,freefallanalytic(t, y0, v0, g, beta),'-',label="Analytic Path")
	plt.plot(t, h0, y0, v0, g, beta,'-')
	plt.plot(t, np.zeros([len(t)]), y0, v0, g, beta,'-')

	plt.legend()
	plt.title("Freefall Simulation")
	plt.xlim(tmin,tmax)
	plt.show(block=False)

	error = [abs((tmaxarray[i]-yfinal)/yfinal) for i in range(0,5)]
	plt.figure()
	plt.plot(dtarray,error,'*')
	plt.title("Delta t versus error at t_{max}")
	plt.show(block=False)
	plt.legend()

#	print(dtarray,"\n",error)

	slope = (error[4]-error[0])/(dtarray[4]-dtarray[0])
	print("The slope of the t versus dt graph is:", slope)
	return

def dragplot(tmax, tmin, y0, v0, g, beta, nts):
	t = [i/(nts / (tmax-tmin)) for i in range(0,nts)]
	betafib = 2
	t.append(8.0)
	h0 = [y0 for i in range(0,len(t))]


	fig, (y, v) = plt.subplots(1,2)

	for i in range(0,5):
		height = freefallheight(t, y0, v0, g, beta)
		velocity = freefallvelocity(t, y0, v0, g, beta)
		y.plot(t,height,'*',label="Beta = "+str(beta))
		v.plot(t,velocity,'*',label="Beta = "+str(beta))

		beta, betafib = betafib, betafib + beta
		print(beta)

	y.plot(t, h0, y0, v0, g, beta,'-')
	y.plot(t, np.zeros([len(t)]), y0, v0, g, beta,'-')

	y.set_xlim(tmin,tmax)
	y.set_title("Position Graph with varying beta values")
	v.set_title("Velocity Graph with varying beta values")
	plt.legend()
	plt.show(block=False)
	return

y0, v0, g, beta, tmin, tmax, nts = 12.0, 35.0, 9.8, 1, 0, 8, 400

plot(tmax, tmin, y0, v0, g, beta)
dragplot(tmax, tmin, y0, v0, g, beta, nts)


