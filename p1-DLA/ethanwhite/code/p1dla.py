import fcns
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

num, size, spawnradius, stickyness, deathradius, maxdis = 100000, 10000, 20, 1, 60, 0 # initializes number of particles, array size
shrub, n, t1 = fcns.create(size) # creates our shrub

while np.sum(shrub[0:size,0:size]) < num: # keepss filling in the graph until num amount of particles are in
	if np.sum(shrub[0:size,0:size]) % 1000 == 0: fcns.timekeeping(shrub,np.sum(shrub[0:size,0:size]),t1) # prints stuff
	n, x, y, distance, stick, shrub = fcns.spawn(shrub, size, spawnradius, n) # spawns a particle

	while distance < deathradius and not stick: # makes sure its in the range
		stick = fcns.stuck(shrub, x, y) # checks if its stuck
		if not stick:
			shrub, x, y, stick = fcns.move(shrub, x, y) # moves it if its not stuck
			distance = fcns.distance(x, y, size) # finds new distance
		if stick:
			if distance > maxdis: # adjusts max distance from origin
				maxdis = distance
				spawnradius = 20 + maxdis # which adjusts spawn radius
				deathradius = 60 + spawnradius
				if round(maxdis) % 10 == 0: print("maxdis updated to",round(maxdis)) # prints stuff
	if distance >= deathradius: # kills the particle if it goes out of bounds
		shrub[x,y] = 0
		n -= 1

dim = np.log(num) / np.log(maxdis) # calculates capacity dimension

print(np.sum(shrub[0:size,0:size]),"particles in shrub in",round(time.time()-t1),"seconds.\n")
print("total time elapsed:",round(time.time()-t1),"seconds with dimension",dim)
fcns.picture(shrub) # makes pretty picture

