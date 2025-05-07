

---
    Author: Mateo Cacheiro
    Topic: ODEs
    Course: TN Tech PHYS4130
    Term: Spring 2025
---


## The Writeup

In the previous Python notebooks, I created and implemented Euler and low-order Runga Kutta numerical ODE solvers. While both of these integrators are easy to implement and understand, they are low-order and have large errors. One source of error for these solvers is that they are both non-symplectic.

> [!NOTE]
> Sympletic integrators are numerical ODE solvers that conserve total energy.
>
> $$\Delta(T+U)=0$$

The program.py file contains a code that compares the accuracy of symplectic vs. non-symplectic integrators in the context of simple harmonic motion. The program compares the results of a verlet, RK4, and an RK2 integrator. 

To begin, the program defines the essential variables. These variables determine the initial position, initial velocity, time range, mass of the object, dampening coefficient, restoring constant, and the number of time steps. This code block will also set the second derivate of the function to the acceleration function. Once the variables are defined, they are sent to the Verlet_solver function. This function uses verlet integration to find the position of a simple harmonic oscillator. During each iteration of the for loop, the program uses the following equation to find the position of the particle at the next time step. 

$$x_{n+1}=2x_n-x_{n-1}+a_{n}\Delta t^2$$

After the position at each future time step is found, the velocity at the current time step is found using the following: 

$$v_{n}=\frac{x_{n+1}-x_{n-1}}{2dt}$$

The loop will run until the position array is filled. Unfortunately, the velocity array does not have a value at the final time stamp. To accommodate this, the position at the next time step is calculated and then used to fill the last entry in the velocity array. 

Once the velocity and position array are complete, the function will return the position, velocity, and time array to the main program. The position and velocity values will then be used to find the kinetic and potential energy as a function of time. Once these values are calculated, the program outputs the following plots:

<figure>
  <img src=Images/Position_Verlet.png>
  <figcaption align="center">Plot of position vs time for a SHO using the verlet integrator.</figcaption>
</figure>
<p>&nbsp;</p>

<figure>
  <img src=Images/Velocity_Verlet.png>
  <figcaption align="center">Plot of velocity vs time for a SHO using the verlet integrator.</figcaption>
</figure>
<p>&nbsp;</p>

<figure>
  <img src=Images/Phasespace_Verlet.png>
  <figcaption align="center">Plot of the SHO's path through phasespace using the verlet integrator.</figcaption>
</figure>
<p>&nbsp;</p>

<figure>
  <img src=Images/Hamiltonian_Verlet.png>
  <figcaption align="center">Plot of total engery vs time for a SHO using the verlet integrator.</figcaption>
</figure>
<p>&nbsp;</p>


As expected, both the position vs. time and the velocity vs. time plots exhibit oscillatory behavior, indicating that the verlet integrators are working correctly. It is also worth noting that the total energy stays constant in the system, which proves the verlet integrator is symplectic. Lastly, the system's path in phase space is a circle.

After the Verlet plots are generated, the program then uses the RK4(5) and RK2(3) integrators from the scipy library to again find the position, velocity, and energy of a simple harmonic oscillator. Using these new solutions and the previous verlet solution, the following plots were created to compare the different integrators. 


<figure>
  <img src=Images/Position_All.png>
  <figcaption align="center">Plot of positions vs time for a SHO.</figcaption>
</figure>
<p>&nbsp;</p>

<figure>
  <img src=Images/Velocity_All.png>
  <figcaption align="center">Plot of velocities vs time for a SHO.</figcaption>
</figure>
<p>&nbsp;</p>

<figure>
  <img src=Images/Phasespace_All.png>
  <figcaption align="center">Plot of the SHO's paths through phasespace.</figcaption>
</figure>
<p>&nbsp;</p>

<figure>
  <img src=Images/Hamiltonian_All.png>
  <figcaption align="center">Plot of total engeries vs time for a SHO.</figcaption>
</figure>
<p>&nbsp;</p>

Once again, the first two plots display oscillatory motion, which is expected and proves that all three integrators do a sufficient job approximating this system when 10000-time steps are used. The paths in phase space are the first indication that these integrators produced different solutions. Runga Kutta paths shrink slightly while the verlet solver stays at a constant radius. This indicates that the RK methods are not symplectic and are losing energy (the area in phase space is shrinking). To investigate this claim further, the Hamiltonian vs. time graph shows how the RK integrators do not have constant energy in time. The RK4 integrator's total energy is oscillatory and slowly lowers compared to the constant total energy found by the verlet integrator. Meanwhile, the RK2 integrator found the energy to decrease quickly compared to the other methods. These results indicate that non-symplectic integrators will produce inaccurate results as they slowly lose energy. 

Since Verlet integration is the only simpletic integrator of the three, the verlet integrator was then used to investigate the behavior of an SHO with a dampening force. Finally the program explores the behavior of four dampened oscillations with the following coefficients:

$$R_{1}=0 \hspace{1cm} R_{2}=\frac{1}{2} \hspace{1cm} R_{3}=1 \hspace{1cm} R_{4}=\frac{3}{2}$$

The position and velocity solutions are then found for each system using the same verlet integrator. Finally, the following three plots were made to compare the motion of SHOs with varying dampening coefficients.

<figure>
  <img src=Images/Dampened_Position_Verlet.png>
  <figcaption align="center">Plot of positions vs time for a SHO.</figcaption>
</figure>
<p>&nbsp;</p>

<figure>
  <img src=Images/Dampened_Phasespace_Verlet.png>
  <figcaption align="center">Plot of the SHO's paths through phasespace.</figcaption>
</figure>
<p>&nbsp;</p>

<figure>
  <img src=Images/Dampend_Hamiltonian_Verlet.png>
  <figcaption align="center">Plot of total engeries vs time for a SHO.</figcaption>
</figure>
<p>&nbsp;</p>

### Attribution
[1] https://en.wikipedia.org/wiki/Harmonic_oscillator

[2] https://www.algorithm-archive.org/contents/verlet_integration/verlet_integration.html

[3] https://en.wikipedia.org/wiki/Verlet_integration

[4] https://docs.scipy.org/doc/scipy/reference/integrate.html

[5] Google AI overview was briefly used to help with syntax and formating when troubleshooting issues with Scipy integrators. the following was entered into the google searchbar: "scipy rk45 with harmonic oscillator"

### Timekeeping
I have spent between 15 and 25 hours on this assignment.

### Languages, Libraries, Lessons Learned
 1. What language did you use for your submission? Is it the same one you started using? If not, why'd you change?

    I used Python for this program. The overall idea of the project was very approachable, considering the support provided by the jupyter notebooks assigned before the project. I could quickly transfer into the project after learning to make ODE solvers in the notebook activities. 
 2. What libraries did you use in your submission? Were any of them remarkable? Great to use, super annoying to use, etc?

    I used the Numpy library and solve_ivp from the scipy library to numerically solve the Simple harmonic oscillator ODE. Once the ODE was solved, I used the Pylab library to generate plots of the solutions and their features. I also used pylab to turn those plots into saved images. After creating the images, I removed those lines of code to limit the continual creation of images every time the code was run. At first, I had a lot of trouble using the RK integrators from scipy because I didn't understand how to properly set up and send a second order ODE to the "solve_ivp." I also didn't understand that RK45 and RK23 were settings in the "solve_ivp" function rather than their functions [5]. A Google search "AI Overview" gave me a better explanation of using the RK45 and RK23 integrators than the Scipy reference material. The Scipy reference material was very abstract and didn't give any real instruction on using the integrators (which was annoying).   

