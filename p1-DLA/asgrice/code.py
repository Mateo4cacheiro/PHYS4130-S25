# Author: Adam Grice
# Project: P1-DLA
# Date: 02-06-2025

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

# Create grid
x = 1000
spawn_rad = 10
Nmax = 1000
N = 1
grid = np.zeros((x,x))
grid[x//2,x//2] = 1
i = 0


def generate_on_circle(spawn_rad, x0, y0):

    angle = np.random.rand() * 2*np.pi
    xval = round(spawn_rad * np.cos(angle)) + x0
    yval = round(spawn_rad * np.sin(angle)) + y0

    return xval, yval


def generate_particle(spawn_rad):
    s = np.random.randint(low=0, high=4) #choose integer from 0 to 3 to determine which side to generate particle on
    if(s == 0): #generate particle at top of grid
        x0 = np.random.randint(low = x//2 - spawn_rad, high = x // 2 + spawn_rad)
        y0 = spawn_rad
        return x0, y0
    elif(s == 1): #right side of grid
        x0 = spawn_rad
        y0 = np.random.randint(low = x//2 - spawn_rad, high = x//2 + spawn_rad)
        return x0, y0
    elif(s == 2): #bottom of grid
        x0 = np.random.randint(low = x//2 - spawn_rad, high = x // 2 + spawn_rad)
        y0 = spawn_rad
        return x0, y0
    elif(s == 3): #left side of grid
        x0 = x - spawn_rad
        y0 = np.random.randint(low = x//2 - spawn_rad, high = x // 2 + spawn_rad)
        return x0, y0


    

# determines whether there is a nonzero point in vicinity of another nonzero point

def get_coords(grid, x0, y0):
    if (np.sum(grid[x0-1:x0+2, y0-1:y0+2]) > 0 ):
        return True
    else:
        return False


# takes in two coordinates and steps them in a random direction.

def step(a, b):
    new_a = a + np.random.randint(low = -1, high = 2)
    new_b = b + np.random.randint(low = -1, high = 2)
    return new_a, new_b

# Commenting this out to try something else
# while(N < Nmax):
#     x1, y1 = generate_particle(x)

#     while(i < 1000):
#         get_coords(grid, x1, y1)
#         if(x1 > x - 1 or x1 < 1 or y1 > x - 1 or y1 < 1):
#             grid[x1, y1] = 0
#             break
#         elif(get_coords(grid, x1, y1) == True):
#             N += 1
#             break
#         else:
#             grid[x1, y1] = 0 #zero current position
#             # print(x1, y1)
#             x1, y1 = step(x1, y1) #update position
#             #print(step(x1,y1))
#             #print(x1, y1)
#             if(x1 > x - 1 or x1 < 1 or y1 > x - 1 or y1 < 1):
#                 x1, y1 = generate_particle(x)
            
#             grid[x1, y1] = 1 #update value of new position
#             # plt.imshow(grid)
#             # plt.draw()
#             # plt.pause(0.0001)
#     i += 1


#------Diagnostic-------
# grid = np.zeros((x,x))
# for m in range(1000):
#    x2, y2 = generate_particle(x)
#    grid[x2,y2] = 1
#    print(f'{x2},{y2}')


kill_rad = spawn_rad+6
while(N < Nmax):
    stuck = False
    x1, y1 = generate_on_circle(spawn_rad, x//2, x//2)
    while not stuck:
        x1, y1 = step(x1, y1)
        dist = np.sqrt(((x//2) - x1)**2 + ((x//2) - y1)**2)
        if(dist > kill_rad):
            x1, y1 = generate_on_circle(spawn_rad, x//2, x//2)
        stuck = get_coords(grid,x1,y1)
    if stuck:
        grid[x1, y1] = 1
        N+=1
        rad = np.sqrt(((x//2) - x1)**2 + ((x//2) - y1)**2)
        if(rad >= spawn_rad):
            spawn_rad = rad + 10
            kill_rad = spawn_rad + 6

plt.imshow(grid)
plt.show()
# plt.draw()
# plt.pause(0.0001)

        




# -----------Diagnostic----------------------
# while(N < Nmax):
#     x1, y1 = generate_particle(spawn_rad)
#     if(x1 > x - 1 or x1 < 1 or y1 > x - 1 or y1 < 1):
#         x1, y1 = generate_particle(spawn_rad)
#     print(x1, y1)
#     x1, y1 = step(x1, y1)
#     print(x1, y1)
#     if(x1 > x - 1 or x1 < 1 or y1 > x - 1 or y1 < 1):
#         x1, y1 = generate_particle(spawn_rad)

#     N+=1