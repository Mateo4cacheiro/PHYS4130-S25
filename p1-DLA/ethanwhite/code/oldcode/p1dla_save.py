import fcns
import numpy as np
import matplotlib.pyplot as plt
import time

num, size, spawnradius, deathradius, maxdis = 5000, 300, 50, 60, 0 # initializes number of particles, array size
shrub, n, t1 = fcns.create(size) # creates our shrub

shrub, maxdis, t1, num = fcns.program(shrub, n, num, size, spawnradius, deathradius, maxdis, t1)

dim = np.log(num) / np.log(maxdis)

print(np.sum(shrub[0:size,0:size]),"particles in shrub in",round(time.time()-t1),"seconds.\n")
print("total time elapsed:",round(time.time()-t1),"seconds with dimension",dim)
fcns.picture(shrub)
