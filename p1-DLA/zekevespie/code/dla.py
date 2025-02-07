import numpy as np
import random
import matplotlib.pyplot as plt
import time

t0 = time.time()
particles = 1
part_tot = 10000
size = 751 #size of the grid, must be odd for a center
x0 = int((size - 1) / 2)
e_radius = 15 #edge radius
d_radius = 25 # death radius
tree = np.zeros([size, size]) # n X n array means array center is [(n-1)/2,(n-1)/2] when n is odd
tree[x0, x0] = 1
#print("Initial Tree:\n", tree)

def Spawn():
    rand1 = random.randrange(360)
    angle = rand1 * np.pi / 180
    x = e_radius * np.cos(angle) - x0 - 1
    y = e_radius * np.sin(angle) - x0 - 1
    #print("x =", round(x), "| y =", round(y))
    return round(x), round(y)

i=0
#print(tree)

while particles <= part_tot:
    x = 0
    y = 0
    x, y = Spawn()
    if tree[x, y] == 1:
        print("*** SPAWN OVERLAP ***")
    else:
        tree[x, y] = 1
        #print("##############################################################")
        #print("##############################################################")
        #print("##############################################################")
        #print(tree)
        #print("##############################################################")
        #print("##############################################################")
        #print("##############################################################")
        while i < 1:
            if np.sqrt((x + x0)*(x + x0) + (y + x0)*(y + x0)) > d_radius:
                tree[x,y] = 0
                #print("DEAD***********************************************")
                break
            elif tree[x + 1, y] == 1 or tree[x - 1, y] == 1 or tree[x, y + 1] == 1 or tree[x, y - 1] == 1:
                particles += 1
                if (particles / 100) == int(particles /100):
                    print("N =", particles)
                if d_radius > np.sqrt((x + x0)*(x + x0) + (y + x0)*(y + x0)) > e_radius and d_radius < x0:
                    e_radius += 5
                    d_radius += 5
                    print("*** DEATH RADIUS INCREASED TO", d_radius, "***")
                break
            else:
                #print("##############################################################")
                
                rand2 = random.randrange(4)
                if rand2 == 0:
                    tree[x, y] = 0
                    x += 1
                    tree[x, y] = 1
                    #print("down")
                elif rand2 == 1:
                    tree[x, y] = 0
                    x -= 1
                    tree[x, y] = 1
                    #print("up")
                elif rand2 == 2:
                    tree[x, y] = 0
                    y += 1
                    tree[x, y] = 1
                    #print("right")
                elif rand2 == 3:
                    tree[x, y] = 0
                    y -= 1
                    tree[x, y] = 1
                    #print("left")
                
                #print(tree)
                #i+=1
                #print("i =", i)
    #print("\n\n", tree)
t1 = time.time()
print("*** TIME ELAPSED :", t1 - t0, "***")
plt.matshow(tree)