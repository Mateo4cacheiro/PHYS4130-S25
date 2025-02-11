import fcns
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

num, size = 250, 30 # initializes number of particles, array size
shrub, spawnradius, deathradius, n, t1 = fcns.create(size) # creates our shrub

while np.sum(shrub[0:size,0:size]) < num:
	if np.sum(shrub[0:size,0:size]) % 500 == 0: fcns.timekeeping(shrub,np.sum(shrub[0:size,0:size]),t1)
	n, x, y, distance, stick, shrub = fcns.spawn(shrub, size, spawnradius, n)

	while distance < deathradius and not stick:
		stick = fcns.stuck(shrub, x, y)
		if not stick:
			shrub, x, y, stick = fcns.move(shrub, x, y)
			distance = fcns.distance(x, y, size)
#		if stick:
#			if fcns.distance(x, y, size) > spawnradiu:
#				spawnradius = round(fcns.distance(x, y, size)) + 5
#				print("radius updated to",spawnradius)
	if distance >= deathradius:
		shrub[x,y] = 0
		n -= 1

print(np.sum(shrub[0:size,0:size]),"particles in shrub in",round(time.time()-t1),"seconds.\n")
print("total time elapsed:",round(time.time()-t1),"seconds")
fcns.picture(shrub)
