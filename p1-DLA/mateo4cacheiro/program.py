#******************************************************************************************
#	 Title:  	program.py
# 	 Date:		1/30/2025   
#    Class:     PHYS 4130
#	
#	Purpose:    Make random diffussion structure
#******************************************************************************************

#import libraries
import numpy as np
import random as ran
import math
from PIL import Image

#define function for summing neighbors
def SumNeighbors(arr, row, col):
    total = 0 
    wide = len(arr)
    height = len(arr[0])

    if 0 < row-1 < wide and 0 <= col < height:
            total += arr[row-1][col]
            
    if 0 < row+1 < wide and 0 <= col < height:
            total += arr[row+1][col]
            
    if 0 < row < wide and 0 <= col-1 < height:
            total += arr[row][col-1]

    if 0 < row < wide and 0 <= col+1 < height:
            total += arr[row][col+1]

    return round(total)

#Create a array to represent a 2D space with a stationary particle at the center
xMax=22
yMax=xMax
crystal = np.array([xMax+1,yMax+1])
crystal = np.zeros([xMax+1,yMax+1])
crystal[round(xMax/2),round(yMax/2)]=1
Size = 50
N=1


while N < Size:
    #Randomly create a particle on ring
    CreateionRadius = xMax/2
    CreationAngle = ran.uniform(0,2*math.pi)
    x = round(xMax/2)+round(CreateionRadius*math.cos(CreationAngle))
    y = round(yMax/2)+round(CreateionRadius*math.sin(CreationAngle))
    if crystal[x,y] == 1:
        attached = True
    else:
        crystal[x,y] = 1
    attached = False

    #ensure particle is in bounds
    while 0<=x<xMax+1 and 0<=y<yMax+1 and not attached:
        #find sum of surrounding spaces 
        AdjSum = SumNeighbors(crystal, x, y) #crystal[x+1,y]+crystal[x-1,y]+crystal[x,y+1]+crystal[x,y-1]
        if AdjSum == 0:
            moveDir = ran.randint(1,4)
            if moveDir == 1:
                #move right
                #print("right")
                crystal[x,y]=0
                if y+1<yMax:
                    crystal[x,y+1] =1
                y=y+1
                
            elif moveDir == 2:
                #move down
                #print("down")
                crystal[x,y]=0
                if x+1<xMax:
                    crystal[x+1,y] =1
                x=x+1
            elif moveDir == 3:
                #move left
                #print("left")
                crystal[x,y]=0
                if y-1>0:
                    crystal[x,y-1] =1
                y=y-1

            else:
                #move up
                #print("up")
                crystal[x,y]=0
                if x-1>0:
                    crystal[x-1,y] =1
                x=x-1

        elif AdjSum > 0:
            #increment N because a particle attaches to the crystal
            N = N+1
            #print("connect")
            attached = True

print(N)
print(crystal)
#im = Image.new(mode="?", size=(xMax, yMax))
#im.show()

