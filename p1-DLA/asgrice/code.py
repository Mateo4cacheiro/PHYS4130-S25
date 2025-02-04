# Author: Adam Grice
# Project: P1-DLA
# Date: 02-03-2025

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

# Create grid
x = 30
Nmax = 50
N = 1
grid = np.zeros((x,x))
grid[x//2,x//2] = 1
i = 0


def generate_particle(x):
    s = np.random.randint(low=0, high=4) #choose integer from 0 to 3 to determine which side to generate particle on
    if(s == 0): #generate particle at top of grid
        x0 = np.random.randint(low = 0, high = x - 2)
        y0 = 0
        return x0, y0
    elif(s == 1): #right side of grid
        x0 = x - 2
        y0 = np.random.randint(low=0,high=x-2)
        return x0, y0
    elif(s == 2): #bottom of grid
        x0 = np.random.randint(low=0,high=x-2)
        y0 = x-2
        return x0, y0
    elif(s == 3): #left side of grid
        x0 = 0
        y0 = np.random.randint(low=0,high=x-2)
        return x0, y0


    

# returns coordinates around a point in grid
def get_coords(grid, x0, y0):
    # print stuff just to see what's happening. Not necessary
    # -------------------------------------------------------
    #print(grid[x0 - 1:x0 + 2, y0 - 1: y0 + 2])

   # print(np.sum(grid[x0-1:x0+2, y0-1:y0+2]))
    # -------------------------------------------------------

    if (np.sum(grid[x0-1:x0+2, y0-1:y0+2]) > 1 ):
        return True
    else:
        return False


# takes in two coordinates and steps them in a random direction.
def step(a, b):
    new_a = a + np.random.randint(low = -1, high = 2)
    new_b = b + np.random.randint(low = -1, high = 2)
    return new_a, new_b


while(N < Nmax):
    x1, y1 = generate_particle(x)

    while(i < 1000):
        get_coords(grid, x1, y1)
        if(x1 > x - 1 or x1 < 1 or y1 > x - 1 or y1 < 1):
            grid[x1, y1] = 0
            break
        elif(get_coords(grid, x1, y1) == True):
            N += 1
            break
        else:
            grid[x1, y1] = 0 #zero current position
            # print(x1, y1)
            x1, y1 = step(x1, y1) #update position
            print(step(x1,y1))
            #print(x1, y1)
            if(x1 > x - 1 or x1 < 1 or y1 > x - 1 or y1 < 1):
                x1, y1 = generate_particle(x)
            
            grid[x1, y1] = 1 #update value of new position
            plt.imshow(grid)
            plt.draw()
            plt.pause(0.0001)
    i += 1



# grid = np.zeros((x,x))
# for m in range(1000):
#    x2, y2 = generate_particle(x)
#    grid[x2,y2] = 1
#    print(f'{x2},{y2}')

    
plt.imshow(grid)
plt.show()