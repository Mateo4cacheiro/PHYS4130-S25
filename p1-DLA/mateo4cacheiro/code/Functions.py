#************************************************************************************************
#File containting all Functions for DLA code
#************************************************************************************************


#import Libraries
import math
import matplotlib.pyplot as plt
from PIL import Image
import numba as nb
import numpy as np
import random as ran

#***********************************************************************************************
#
#
#
#***********************************************************************************************
@nb.jit
def MainFunction(crystal,Size,MaxArm,CreationRadius,DeathRadius,XCenter,YCenter,M,N,S): 
    #Loop until the structure has "Size" number of particles
    while N < Size:      
    
        #Creates a new particle 
        x,y=CreateParticle(CreationRadius,XCenter,YCenter)
        Distance = dis(x,XCenter,y,YCenter) 
        
        #print("D: ", Distance)
        adjacent = False
        attached = False
        
        #Move particle until it attaches or goes out of bounds
        while not attached and Distance < DeathRadius:
        
            #Determine if particle is next to the structure 
            adjacent = CheckAttached(crystal,x,y)
        
            #if particle is not adjacent to the structure, move particle normally.
            if adjacent == False:
                moveDir = np.random.randint(0,4)                             #roll rand walk direction
                x,y=move(x,y,moveDir)                                      #move particle
                #print("move")
                Distance = dis(x,XCenter,y,YCenter)
                #print(Distance)
            
            #method for if particle is adjacent to the structure    
            else:
                #Check if particle sticks
                roll = (np.random.randint(1,101))/100
                if roll <= S:
                    #print("Attached")
                    #Adjust MaxArm length and creation radius
                    if Distance > MaxArm:
                        MaxArm = Distance
                        CreationRadius = 100 + MaxArm
                        #print("CreationRadius: ", CreationRadius)
                        DeathRadius = 50 + CreationRadius  
                    N += 1
                    attached = True
                    crystal[x,y] = 1 + N/Size
                    M += 1
                    if M == 1000:
                        print(N)
                        M = 0
                else:
                    x,y = Stickymove(crystal,x,y)

    return(crystal,MaxArm)




#*************************************************************************************************************
#
#
#
#*************************************************************************************************************
def CreateArray(ArraySize: int):
    Width=ArraySize+1
    Height=ArraySize+1
    crystal = np.zeros([Width,Height])                                      #Set all values in array to zero
    XCenter = round((Width)/2)
    YCenter = round((Height)/2)                                             #Find Center point of Array (find origin point)
    crystal[XCenter,YCenter]=1                                              #Set ceterpoint of array to 1 (Create Particle at origin)
    N = 1                                                                   #Increment Particle count
    M = 1
    return(crystal, XCenter, YCenter, M, N)




#**************************************************************************************************************
#
#
#
#**************************************************************************************************************
@nb.jit
def CreateParticle(CreationRadius,XCenter,YCenter): 
    #print("xRad: ", CreationRadius)
    x = np.random.randint(-CreationRadius,CreationRadius+1)
    #print("X: ",x)
    flip = np.random.randint(0,2)
    if flip == 0:
        #print("up")
        y = CreationRadius-abs(x)
    else:
        y= -(CreationRadius-abs(x))
        #print("down")
    #print("X: ",x,"Y: ",y)
    x+=XCenter
    y+=YCenter
    #print("X: ",x,"Y: ",y)
    return(x,y)




#*******************************************************************************************************************
#
#
#
#*******************************************************************************************************************
@nb.jit
def CheckAttached(crystal, x,y): 
    boolian = False
    if crystal[x-1,y]!=0 or crystal[x+1,y] !=0 or crystal[x,y-1]!=0 or crystal[x,y+1]!=0:
        boolian = True
    return(boolian)




#********************************************************************************************************************
#
#
#
#********************************************************************************************************************
@nb.jit
def move(x,y,Direction):
    if Direction == 0:
        y += 1
                
    elif Direction == 1:
        x += 1

    elif Direction == 2:
        y -= 1

    else:
        x -= 1
    return(x,y)




#********************************************************************************************************************
#
#
#
#********************************************************************************************************************
@nb.jit
def dis(x, XCenter, y, YCenter):
    return(abs(x-XCenter) + abs(y-YCenter))




#********************************************************************************************************************
#
#
#
#********************************************************************************************************************
@nb.jit
def Stickymove(crystal,x,y):
    #print("didn't Attach")
    re_roll = True
    locate = [crystal[x,y+1],crystal[x+1,y],crystal[x,y-1],crystal[x-1,y]]
    #print(locate)
    while re_roll == True:
        roll2 = np.random.randint(0,4)
        #print(roll2)
        if locate[0] == 0 and roll2 == 0:
            x,y = move(x,y,roll2)
            re_roll = False
        elif locate[1] == 0 and roll2 == 1:
            x,y = move(x,y,roll2)
            re_roll = False
        elif locate[2] == 0 and roll2 == 2:
            x,y = move(x,y,roll2)
            re_roll = False
        elif locate[3] == 0 and roll2 == 3:
            x,y = move(x,y,roll2)
            re_roll = False
    return(x,y)





#********************************************************************************************************************
#
#
#
#********************************************************************************************************************
def CreateImage(crystal,N,S,R,D):
    # sum columns and rows, identify which elements are not zero
    xslice = np.where(np.sum(crystal,axis=0))[0]
    yslice = np.where(np.sum(crystal,axis=1))[0]

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
    _ = ax.imshow(crystal[yslice[0]-whitespace:yslice[-1]+whitespace+1,
                        xslice[0]-whitespace:xslice[-1]+whitespace+1],
                origin='upper',
                interpolation='nearest',
                aspect='equal')

    # these optional parameters (origin, interpolation, aspect) are automatically set by matshow,
    # but matshow also moves the axes to the top of the 
    _ = ax.axis('off')
    _ = ax.set_title(f'N={N}', fontsize=12)  # note the use of an f-string in this command
    fig.savefig(f'figure_S{S}_N{N}_R{R}_D{D}.png',bbox_inches='tight',dpi=150)

    # If you *only* want to save the array, and you want to add the title and all figure details separately
    # you can call imsave instead:
    '''
    plt.imsave(f'demo_figure_N{Size}_direct.png',
            crystal[yslice[0]-whitespace:yslice[-1]+whitespace+1,
                    xslice[0]-whitespace:xslice[-1]+whitespace+1],
            )
    # This shifts the overhead, and now you'll have to figure out how to scale the resulting png so the figure
    # is exactly as large as you want. It's not easier per se, but it's predictable and good to know for LaTeX
    # manuscripts especially.
    '''    
    pass






