import fcns
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

num, size = 1000, 100 # initializes number of particles, array size
shrub, spawnradius, deathradius, n, t1 = fcns.create(size) # creates our shrub

while np.sum(shrub[0:size,0:size]) < num:
	if np.sum(shrub[0:size,0:size]) % 500 == 0: fcns.timekeeping(np.sum(shrub[0:size,0:size]),t1)
	n, x, y, dis, stick, shrub = fcns.spawn(shrub, size, round(spawnradius), n)

	while dis < deathradius and not stick:
		stick = fcns.stuck(shrub, x, y)
		if not stick:
			shrub, x, y, stick = fcns.move(shrub, x, y)
			dis = fcns.distance(x, y, size)

#                       if dis >= step:
#                               step += 1
#                               spawnradius += 1
#                               print(step)
#               else:
#                       attach(shrub, x, y)
#                       dis = distance(x, y, size)
#       if stick:
#               if round(distance(x, y, size) + 2) == spawnradius:
#                       spawnradius = round(distance(x, y, size) + 2)
#                       print(spawnradius)
	if dis >= deathradius:
		shrub[x,y] = 0
		n -= 1

print(np.sum(shrub[0:size,0:size]),"particles in shrub in",round(time.time()-t1),"seconds.\n")
print("total time elapsed:",round(time.time()-t1),"seconds")
fcns.picture(shrub)
