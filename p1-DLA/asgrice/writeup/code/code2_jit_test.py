# Author: Adam Grice
# Project: P1-DLA
# Date: 02-07-2025

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time
import numba as nb
from scipy import ndimage

# Create grid
x = 10000
spawn_rad = 10
kill_rad = spawn_rad + 6
Nmax = 50000
N = 1
S = 0.5
grid = np.zeros((x,x))
grid[x//2,x//2] = 1

@nb.jit
def generate_on_circle(spawn_rad, x0, y0):

    angle = np.random.rand() * 2*np.pi
    xval = round(spawn_rad * np.cos(angle)) + x0
    yval = round(spawn_rad * np.sin(angle)) + y0

    return xval, yval

# @nb.jit
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
@nb.jit
def get_coords(grid, x0, y0):
    if (np.sum(grid[x0-1:x0+2, y0-1:y0+2]) > 0 ):
        return True
    else:
        return False

@nb.jit
def get_coords2(grid, x0, y0, S):
    stick = np.random.rand()
    if (np.sum(grid[x0-1:x0+2, y0-1:y0+2]) > 0 and stick < S):
        return True
    else:
        return False



# takes in two coordinates and steps them in a random direction.
@nb.jit
def step(a, b):
    new_a = a + np.random.randint(low = -1, high = 2)
    new_b = b + np.random.randint(low = -1, high = 2)
    return new_a, new_b

@nb.jit
def big_fcn(x, spawn_rad, kill_rad, Nmax, N, grid, S):
    while(N < Nmax):
        stuck = False
        x1, y1 = generate_on_circle(spawn_rad, x//2, x//2)
        while not stuck:
            x1, y1 = step(x1, y1)
            dist = np.sqrt(((x/2) - x1)**2 + ((x/2) - y1)**2)
            if(dist > kill_rad):
                x1, y1 = generate_on_circle(spawn_rad, x//2, x//2)
            stuck = get_coords2(grid, x1, y1, S)
        if stuck:
            grid[x1, y1] = 1 + (N/Nmax)
            N+=1
            if(N%500 == 0):
                print(N)
            # x_cm, y_cm = np.round(ndimage.center_of_mass(grid))
            rad = np.sqrt(((x/2) - x1)**2 + ((x/2) - y1)**2)
            if(rad >= spawn_rad):
                spawn_rad = rad + 10
                kill_rad = spawn_rad + 20     
    cap_dim = np.log(N)/np.log(spawn_rad - 10)
    # print(cap_dim)
    return cap_dim
    
D = big_fcn(x, spawn_rad, kill_rad, Nmax, N, grid, S)


#---------------------------------------------
# ripped code for plots from Notes+tips.md
#---------------------------------------------

xslice = np.where(np.sum(grid,axis=0))[0]
yslice = np.where(np.sum(grid,axis=1))[0]

# calculate the size of the cropped aggregate
whitespace = 2  # don't crop exactly to the edges of the DLA
ypixels = yslice[-1]-yslice[0]+2*whitespace
xpixels = xslice[-1]-xslice[0]+2*whitespace

# approximate the size of the generated figure. This is more than good enough almost always.
figure_ppi = 15  # ppi = pixels per inch
figw = xpixels/figure_ppi
figh = ypixels/figure_ppi+0.375  # add extra space for the figure title

# Create a figure/axis object (this makes systematic figure generation much easier)
# NB you should specify the length and width of the figure (in inches) here.
fig, ax = plt.subplots(figsize=(figw, figh))

# slice the "crystal" object on the edges identified with the "where" command.
# NB: you can break a python function call over multiple lines to make it easier to read
_ = ax.imshow(grid[yslice[0]-whitespace:yslice[-1]+whitespace+1,
                      xslice[0]-whitespace:xslice[-1]+whitespace+1],
               origin='upper',
               interpolation='nearest',
               aspect='equal')

# these optional parameters (origin, interpolation, aspect) are automatically set by matshow,
# but matshow also moves the axes to the top of the 
_ = ax.axis('off')
_ = ax.set_title(f'N={Nmax}, D={round(D, 3)}', fontsize=12)  # note the use of an f-string in this command
fig.savefig(f'demo_figure_N{Nmax}.png',bbox_inches='tight',dpi=150)
plt.imshow(grid)
plt.show()