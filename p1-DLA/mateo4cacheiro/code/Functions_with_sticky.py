#import libraries
import numpy as np
import random as ran
import math
import matplotlib.pyplot as plt
from PIL import Image
  


#define function for creating array with Size "ArraySize"
def CreateArray(ArraySize):
        global crystal
        global N 
        global M
        global XCenter 
        global YCenter 
        Width=ArraySize+1
        Height=ArraySize+1
        crytal = np.array([Width,Height])                                       #Create array
        crystal = np.zeros([Width,Height])                                      #Set all values in array to zero
        XCenter = round((Width)/2)
        YCenter = round((Height)/2)                                             #Find Center point of Array (find origin point)
        crystal[XCenter,YCenter]=1                                              #Set ceterpoint of array to 1 (Create Particle at origin)
        N = 1                                                                   #Increment Particle count
        M = 1
        return()





#define function for creating particles
def CreateParticle(Radius):
        global x 
        global y
        global XCenter
        global YCenter
        CreationAngle = np.random.uniform(0,2*math.pi)                                #Select random point on Creation ring
        x = XCenter+round(Radius*math.cos(CreationAngle))                       #convert (with rounding) from polar to cartisean coordinates
        y = YCenter+round(Radius*math.sin(CreationAngle))                       
        return()





#define function for summing neighbors
def CheckAttached(): 
    global x
    global y
    boolian = False

    if crystal[x-1,y]==1 or crystal[x+1,y]==1 or crystal[x,y-1]==1 or crystal[x,y+1]==1:
        boolian = True


    return(boolian)





#define function for moving
def move(Direction):
    global x
    global y
    if Direction == 0:
        x += 1
                
    elif Direction == 1:
        y -= 1

    elif Direction == 2:
        x -= 1

    else:
        y += 1
    return()


#defin NotFull function
def NotFull(Size):
    if (N == Size):
        return(False)
    else:
        return(True)



#define dis function
def dis():
    return((x-XCenter)**2 + (y-YCenter)**2)



#define DestoryPart function
def des():
    crystal[x,y]=0
    return()

#define ShowStructure function
def ShowStructure():
    plt.matshow(crystal)

#define Increment function
def increment():
    
    global N
    global M
    S = 9
    reroll = True
    rng = np.random.default_rng()
    roll=rng.integers(1,11)
    if roll >= S:
        M += 1
        N += 1
        crystal[x,y] = 1
        if M == 500:
            print(N)
            plt.matshow(crystal)
            M = 0
    else:
        #determine where the adjecent particle(s) is(are). 
        Move = 0
        Up = False
        Down = False
        Left = False
        Right = False
        if crystal[x+1,y]==1:
            Right = True
        if crystal[x-1,y]==1:
            Left = True
        if crystal[x,y+1]==1:
            Up = True    
        if crystal[x,y-1]==1:
            Down = True
        while reroll == True:
            MOVE=rng.integers(0,4)
            reroll = False
            if Right and MOVE == 0:
               reroll == True 
            if Left and MOVE == 2:
               reroll == True 
            if Up and MOVE == 3:
               reroll == True 
            if Down and MOVE == 1:
               reroll == True 
        move(Move)
        