import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def relativity_photon_geodesic(t, y):
	px, py, vx, vy = y
	r = np.sqrt(px**2 + py**2)
	dot_product = px * vx + py * vy
	ax = -G * M * px / r**3 * (1 + (3 * dot_product**2) / (r**2 * c**2))
	ay = -G * M * py / r**3 * (1 + (3 * dot_product**2) / (r**2 * c**2))
	return [vx, vy, ax, ay]

def newtonian_photon_geodesic(t, y):
	px, py, vx, vy = y
	r = np.sqrt(px**2 + py**2)
	ax = -G * M * px / r**3
	ay = -G * M * py / r**3
	return [vx, vy, ax, ay]

def newtonian(G,M,c,R,newtonian_photon_geodesic):
	y0 = [-5 * R, R, c, 0]  # [x0, y0, vx0, vy0]
	times = (0, 20*R/c) # time span
	time_eval = np.linspace(times[0], times[1], 10000) # evaluating at 10000 diff points

	sol = solve_ivp(newtonian_photon_geodesic, times, y0, t_eval=time_eval, rtol=1e-9, atol=1e-9) # solving
	vx, vy = sol.y[2,9999], sol.y[3,9999] # final velocities
	px, py = sol.y[0], sol.y[1]

	theta = np.degrees(np.arctan2(vy, vx)) * 3600 # calculating angle from final velocity tangent values
	return theta, px, py

def relativity(G,M,c,R,relativity_photon_geodesic):
	y0 = [-5*R,R,c,0]  # photon starts at x = -5R, y = R with velocity (c, 0)
	times = (0, 20*R/c)
	time_eval = np.linspace(times[0], times[1], 10000)

	sol = solve_ivp(relativity_photon_geodesic, times, y0, t_eval=time_eval, rtol=1e-9, atol=1e-9)
	vx, vy = sol.y[2,9999], sol.y[3,9999]
	px, py = sol.y[0], sol.y[1]

	theta = np.degrees(np.arctan2(vy, vx)) * 3600  # arcseconds
	return theta, px, py

def plotting(Npx,Npy,Gpx,Gpy):
	fig, ax = plt.subplots(figsize=(6, 6))
	ax.plot(Npx, Npy, 'r-', label='Newtonian Photon Path') # plotting newtonian
	ax.plot(Gpx, Gpy, 'b-', label='Relativity Photon Path') # plotting relativity
	sun = plt.Circle((0, 0), R, color='gold', alpha=0.5, label='Sun')
	ax.add_patch(sun) # adding the sun

	ax.set_xlim(-5*R, 5*R)
	ax.set_ylim(-2*R, 2*R)
	ax.set_aspect('equal')
	ax.set_title("Photon Trajectory")
	ax.legend()
	plt.show(block=False)
	return

G,M,c,R,npg,rpg = 6.674e-11, 1.989e30, 3.0e8, 6.96e8, newtonian_photon_geodesic, relativity_photon_geodesic

thetaN,Npx,Npy = newtonian(G,M,c,R,npg)
thetaGR,Gpx,Gpy = relativity(G,M,c,R,rpg)
plotting(Npx,Npy,Gpx,Gpy)
print(f"Newtonian deflection angle: {thetaN:.2f} arcseconds","\n"+f"Relativistic deflection angle: {thetaGR:.2f} arcseconds")

