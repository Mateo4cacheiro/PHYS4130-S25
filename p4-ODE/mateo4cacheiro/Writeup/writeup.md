

---
    Author: Mateo Cacheiro
    Topic: ODEs
    Course: TN Tech PHYS4130
    Term: Spring 2025
---


## The Writeup

In the previous python notebooks I created and implemented Euler and low order Runga Kutta numerical ODE solvers. While both of there integrators are easy to implement and understand, they are both low order and have large error. One source of error for these solvers is that they are both non-sympletic.

> [!NOTE]
> Sympletic integrators are numerical ODE solvers that conserve total energy.
>
> $$\Delta(T+U)=0$$

The program.py file contains a code that compares the accuracy of sympletic vs. non-sympletic integrators in the context of simple harmonic motion. The program compares the results of a verlet, RK4 , and a RK2 integrator. 

To begin the program defines the essential variables. These variables define the intial position, intial velocity, time range, mass of the object, dampening coeffeicent, restoring constant, and number of time steps. This block of code will also sets the second derivate of the funtion to the acceleration function. Once the variables are defined they are sent to the Verlet_solver function. This function uses verlet integration to find the position of a simple harmonic oscillator. Durring each iteration of the for loop the program uses the following equation to find the postion of the particle at the next time step. 

$$x_{n+1}=2x_n-x_{n-1}+a_{n}\Delta t^2$$

After the postion at each future time step is found, the velocity at the current time step is found using the following: 

$$v_{n}=\frac{x_{n+1}-x_{n-1}}{2dt}$$

The loop will run until the position array is filled. Unforutinatly, this means the velocity array does not have a value at the final time stamp. To accomidate this, the postion at the next time step is calculated and then used to fill the last entry in the velocity array. 

Once the velocity and postion array are complete, the function will return the position, velocity, and time array to the main program. The values of position and velocity will then be used to find the kinetic and potential energy as a funciton of time. Once these values are calculated the program outputs the following plots:

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


As expected both the postion vs. time and the velocity vs. time plots exhibit oscilatory behavior indicating that the verlet integrators are working properly. It is also worth noting that the total energy stays constant in the system which proves the verlet integrator is sympletic. Lastly the system's path in phase space is a circle.

After the Verlet plots are generated the program then uses the RK4(5) and RK2(3) integrators from the scipy library to again find the postion, velocity and energy of a simple harmonic oscilator. Using these new solutions and the previous verlet solution the following plots were created to compare the different integrators. 

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

Once again the first two plots display oscillatory motion which is expected and proves that all three integrators do a suffiecnt job approximating this system when 10000 time steps are used. The paths in phasespace are the first indication that these integrators produced different solutions. Both Runga Kutta paths slightly shrink while the verlet solver stays at a constant radius. This is an indication that the RK methods are not sympletic and are loosing energy (area in phasespace is shrinking). To further investigate this claim the hamiltion vs. time graph shows how the RK integrators do not have constant energy in time. The RK4 intgrator total energy is oscilatory and slowly lowers in comparision to the constant total energy found by the verlet integrator. Meanwhile, the RK2 integrator found the integrator to decrease quickly in comparision with the other to methods. These results indicate that over time the use of non-sympletic integrators will produce inaccurate results as they will slowly loose energy. 

Since Verlet integration is the only simpletic integrator of the three, the verlet integrator was then used to investigate the behavior of a SHO with a dampening force. The program investigates the behavior of four dampened oscillations with the following coeffiecents:

$$R_{1}=0 \hspace{1cm} R_{2}=\frac{1}{2} \hspace{1cm} R_{3}=1 \hspace{1cm} R_{4}=\frac{3}{2}$$

The position and velocity solutions are then found for each system using the same verlet integrator as before. Finally the flowing three plots were made to compare the the motion of SHOs with varying dampening coeffients.

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
I have spent between 10 and 20 hours on this assignment.

### Languages, Libraries, Lessons Learned
 1. What language did you use for your submission? Is it the same one you started using? If not, why'd you change?

    I used Python for this program The overall idea of the project was very approachable considering the support provided by the jupyter notebooks assigned prior to the project. After learning to make ODE solvers in the notebook activities I was able to quickly transfer into the project. 
 2. What libraries did you use in your submission? Were any of them remarkable? Great to use, super annoying to use, etc?

     I used the Numpy library and solve_ivp from the scipy library to numerically solve the Simple harmonic Oscilator ODE. Once the ODE was solved I used the pylab library to generate plots of the solutions and features about the solutions. I also used pylab to turn those plots into saved images. After creating the images I removed those lines of code to limit the continual creation of images every time the code is run. At first I had a lot of trouble using the RK integrators from scipy because I didn't understand how to properly set up and send a second order ODE to the "solve_ivp". I also didn't understand that RK45 and RK23 were settings in the "solve_ivp" function rather than their own functions [5]. Upon a google search "AI Overview" gave me a much better explaination on how to use the RK45 and RK23 integrators than the Scipy reference material. The Scipy reference material was very abstract and didn't give any real instruction on how to use the integrators (This was kinda annoying).   
