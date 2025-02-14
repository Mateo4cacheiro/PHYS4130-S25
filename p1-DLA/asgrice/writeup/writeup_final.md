# Project 1: Diffusion-Limited Aggregation

## Background
Diffusion-limited aggregation (DLA) was first proposed in 1981 by T.A. Witten Jr. and L.M. Sander as a model for random motion of particles suspended in a medium, whose primary motion in the system is diffusion. Some number of particles _N_ are allowed to diffuse one-by-one around a single "seed" particle. They will wander randomly and eventually collide with the seed and stick to it, creating a fractal structure as the process repeats. The version created for this assignment assumes particles wandering in from infinity from random directions, simulating a low density of particles moving randomly. 

## The Program
This DLA simulation works by creating a 2-D array populated with zeros, except for the seed particle at the center, which is given a value of one. Particles are generated at random points on a spawn radius by generating a random number between 0 and 2pi to get their angular position. Each particle is then allowed to step in a random direction by adding a random integer [0,1] to its horizontal and vertical coordinates. After each step, three checks are performed: the first is to check whether the particle has stepped outside of the "kill radius" where it is too far away from the aggregate to collide in a reasonable amount of time. If a particle passes this radius it is killed and a new particle is generated on the spawn radius. This is a time efficient way to represent the idea that on an infinite time scale the particle will travel back towards the aggregate. The second check is to determine whether the particle has collided with the aggregate. The 8 array points around the particle are summed and if the sum is greater than zero, the particle has contacted the aggregate. The third check is to decide if the particle will stick to the aggregate or continue stepping. A random number between 0 and 1 is generated, and if it is greater than the stickiness factor specified earlier in the program, it sticks. When a particle sticks to the aggregate, the value of the array at that position is changed to one and the number of particles is incremented by one. This process repeats until some maximum number of particles have stuck to the aggregate. For each new particle that is added to the aggregate, its distance from the origin is compared to the spawn radius. If the aggregate has grown to or beyond the spawn radius, both the spawn radius and kill radius are increased. The radius of the aggregate is also used to determine the capacity dimension D by D = ln(N)/ln(R).

## Results
Currently this simulation can create a 50,000 particle aggregate. Larger aggregates can be done, but have not been due to long runtimes. After 10 runs with 20,000 particles and the stickiness factor S ranging from 0.1 to 0.99, the average capacity dimension was determined to be 1.807, larger than Witten and Sander's published value of 1.7. A plot of capacity dimension vs. stickiness factor is shown below: 

![](https://github.com/asgrice/PHYS4130-S25/blob/main/p1-DLA/asgrice/N%3D20000/D_vs_S.png)


A slight upward trend is visible. Normally it would be expected that a slight downward trend would appear, but the way in which stickiness factor is implemented in this project inverts the relationship between dimension and stickiness. A sample aggregate with 50,000 particles is shown below: 

![](https://github.com/asgrice/PHYS4130-S25/blob/main/p1-DLA/asgrice/N%3D50000_D%3D1.488_S%3D0.5.pdf)


At smaller N the images produced more closely resemble those published by Witten and Sander, and the values calculated for capacity dimension are also closer to 1.7.

## Problems
Currently there are several areas where this simulation can be improved. The first is to determine and update the aggregate's center of mass as opposed to having the radius be relative to the center of the grid. This would help prevent the long branches which appear at higher particle counts. Another issue is that when checking each new particle's proximity to the aggregate, there are no measures implemented to keep new particles from stepping into or through the aggregate. 

## Attribution
The major breakthroughs on this project were made with a good deal of help from Dr. Reid. Mateo Cacheiro also had several helpful suggestions. Online resources used include wikipedia.org, geeksforgeeks.org, numpy.org, numba.pydata.org, stackoverflow.com, and matplotlib.org.

## Timekeeping
Approximately 20-30 hours have been spent working on this project.

## Languages, Libraries, Lessons Learned
This project was written in python using numpy, matplotlib, and numba, all of which were useful and fairly simple to implement.