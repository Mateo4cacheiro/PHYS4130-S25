# ******************************************************************************************
#	 Title:  	program.py
# 	 Date:		2/3/2025   
#    Class:     PHYS 4130
#	
#	Purpose:    Make random diffussion structure
#******************************************************************************************


#import function file
import Functions
import numpy as np
import matplotlib.pyplot as plt


#Set Important Variables
ArraySize= 10000                                                            #Matrix Size
Size = 24004                                                               #Total Particles                                                                    
S=1                                                                         #Set Stickiness parameter (0.01,1)
MaxArm = 0                                                                  #Set longest arm length to zero
CreationRadius = 100                                                        #Creation radius will start at 100 units
DeathRadius= CreationRadius + 50                                            #Death Radius will start 50 units larger than creation ring    

#Call a function to create the array that will contain the Structure. Stars with a particle at (XCenter,YCenter)
crystal,XCenter,YCenter,M,N=Functions.CreateArray(ArraySize)

#Once the Array is made, Build the struture. 
crystal,MaxArm=Functions.MainFunction(crystal,Size,MaxArm,CreationRadius,DeathRadius,XCenter,YCenter,M,N,S)

#After struture is created within the array, calculate the fractal dimension.
Dimension=np.log(Size)/np.log(MaxArm)

#output important values
print(MaxArm, Size)
print("Dimension: ", Dimension)

#Create figure of the structure
Functions.CreateImage(crystal,Size,S,MaxArm,Dimension)



