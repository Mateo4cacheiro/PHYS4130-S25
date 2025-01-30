import numpy as np
import random

###Initializing the tree

particles = 1
part_tot = 35
radius = 5 #edge radius
size = 15 #size of the grid
x0 = int((size - 1) / 2)
tree = np.zeros([size, size]) # n X n array means array center is [(n-1)/2,(n-1)/2] when n is odd
tree[x0, x0] = 1
print("Initial Tree:\n", tree)

#Spawn function definition

def Spawn():
    x = random.randrange(x0 - radius, x0 + radius)
    rand1 = random.randrange(2)
    if rand1 == 0:
        y = np.sqrt(radius*radius - (x - x0)*(x - x0)) + x0
        #print("x =", x, "| y =", round(y))
    else:
        y = -np.sqrt(radius*radius - (x - x0)*(x - x0)) + x0
        #print("x =", x, "| y =", round(y))
    return x, round(y)

#Main function body, might break up into smaller functions later

i=0
while particles <= part_tot:
    x = 0
    y = 0
    x, y = Spawn()
    tree[x, y] = 1
    while i < 10000:
        if np.sqrt((x - x0)*(x - x0) + (y - x0)*(y - x0)) > 1.2*radius:
            tree[x,y] = 0
            break
        elif tree[x + 1, y] == 1 or tree[x - 1, y] == 1 or tree[x, y + 1] == 1 or tree[x, y - 1] == 1:
            particles += 1
            break
        else:
            rand2 = random.randrange(4)
            if rand2 == 0:
                tree[x, y] = 0
                x+=1
                tree[x, y] = 1
                #print("down")
            elif rand2 == 1:
                tree[x, y] = 0
                x-=1
                tree[x, y] = 1
                #print("up")
            elif rand2 == 2:
                tree[x, y] = 0
                y+=1
                tree[x, y] = 1
                #print("right")
            elif rand2 == 3:
                tree[x, y] = 0
                y-=1
                tree[x, y] = 1
            i+=1
print("\nFinal Tree:\n", tree)