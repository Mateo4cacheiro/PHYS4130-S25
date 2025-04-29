---
    Author: Zeke Vespie
    Topic: Integration Methods Project
    Course: TN Tech PHYS4130
    Term: Spring 2025
---

# WRITEUP

## MAIN ASSIGNMENT

This is the first part of my writeup, where I do all the main objectives. I do the first extension to the project later on.

### SIMPLE HARMONIC OSCILLATOR NOT AT REST

The first part of this project was to display how a Simple Harmonic Oscillator (SHO) that is *not* at rest. I foolishly took this as meaning that the center of the oscillation moves at a constant speed at first, but changed it to what was expected instead. The equation of motion is below:

```math
\frac{\partial x}{\partial t} = v
```
```math
\frac{\partial v}{\partial t} = -\omega^2x
```

This is simple to do analytically, but it's also easy computationally. In iterative form, this becomes the following:

```math
x+\Delta x=x+v\Delta t\ \ \ \Rightarrow\ \ \ x[i+1]=x[i]+v[i]\ dt
```
```math
v+\Delta v=v-\omega^2x\ \Delta t\ \ \ \Rightarrow\ \ \ v[i+1]=v[i]-\omega^2x[i]\ dt 
```

I implemented this and it produced exactly what you would expect a SHO to produce in phase space: a ellipse. The image is below:

<figure>
  <img src=figures/f1.png>
    <figcaption>Plot of phase space for a simple harmonic oscillator. Note that the number of time steps is 100,000 in this case.</figcaption>
</figure>
<p>&nbsp;</p> 

This is exactly what I would expect, considering the analytic solution for this differential equation is a cosine function.

### DAMPED SIMPLE HARMONIC OSCILLATOR

Next I produced the code for the damped case of the SHO. This changes the second equation of motion to this:

```math
\frac{\partial v}{\partial t} = -\omega^2x-\beta v
```

This is a much more annoying solution to find analytically, but computationally this is as easy as adding a single term to my iterative process:

```math
v+\Delta v=v-(\omega^2x-\beta v)\Delta t\ \ \ \Rightarrow\ \ \ v[i+1]=v[i]-(\omega^2x[i]+\beta v[i])\ dt 
```

Implementing this also does exactly what I'd expect, that being the ellipse from before slowing dying toward the center. An image of this is below:

<figure>
  <img src=figures/f2.png>
    <figcaption>Plot of phase space for a simple harmonic oscillator with a damping coefficient of 0.1. Note that the number of time steps is 10,000 in this case.</figcaption>
</figure>
<p>&nbsp;</p> 

### 3 NEW INTEGRATION TYPES

Before, the method of integration was just euler-style. This is good, but isn't the best thing around. For the next part of the project, I am going to use 3 different kinds of integration.

1. Velocity Verlet Integration:
This method is one that conserves energy. The explanation for this is kind of strange to me, but in essence I see it as being analagous to regular energy conservation. This method requires the computational iterations listed below, in order of use. (Seems that some of them clearly resemble classic kinematics equations)

```math
x[i+1]=x[i]+v[i]dt + \frac{1}{2}a[i](dt)^2
```
```math
a[i+1] = -\omega^2x[i+1]
```
```math
v[i+1]=v[i]+\frac{1}{2}(a[i]+a[i+1])dt
```

2. 4th Order Runge-Kutta Integration [RK4(5)]:
This method is just a more complicated version of the Runge-Kutta that we used in the homework for this section. It esentially takes advantage of a Taylor Series expansion of a variable that is in a simple ordinary differential equation. The iteration for this would look like the expansion I described, but since this is already in the SciPy library I don't actually know the code iterations exactly.

3. Backwards Differentiation Formula Integration [BDF]:
This method is the weird one. It appears to be specifically designed to solve ordinary differential equations that are "stiff", meaning they often have rapid changes that require a larger number of time steps to accomplish. Their are different orders of BDF, but the one used in my program is ambiguous since it is taken from the SciPy library.

### ENERGY VERSUS TIME FOR SHO AND DAMPED SHO

The energy of a SHO is calculated using the equation below:

```math
E=K+U=\frac{1}{2}mv^2+\frac{1}{2}m\omega^2x^2
```

This is easily calculated with what I have already gathered in the previous parts, so it is as simple as implementing it as written. The plot of the total energy over time of the SHO is below, with the first image being the undamped case and the second being the damped case.

<figure>
  <img src=figures/f3.png>
    <figcaption>Plot of the energy of a simple harmonic oscillator over time. Note that the number of time steps is 10,000 in this case.</figcaption>
</figure>
<p>&nbsp;</p> 

The problem is that this plot is garbage. Firstly, the Verlet integrator does not conserve energy; on average it does, but the energy versus time plot shows a sine wave, which is not constant. The RK4(5) integrator does conserve energy, which I don't think it's supposed to do, but it's constant and equal to the average of the Verlet. Lastly, the BDF integrator is incredibly strange, as it seems to start where RK4(5) does but then instantly falls to a value less than what it started at, then stays constant from there. I played around with this some, but I didn't really get anywhere with it, so this is the best I can do.

Next, I will show the same thing but for the damped case. The changes made have already been outlined in previous sections, so I will just show you the results:

<figure>
  <img src=figures/f4.png>
    <figcaption>Plot of the energy of a simple harmonic oscillator over time, this time with damping coefficient of 0.1. Note that the number of time steps is 100 in this case.</figcaption>
</figure>
<p>&nbsp;</p> 

I left the number of time steps at only 100 to show the fact that the Verlet integrator is a bit less efficient, but overall this looks better than the previous image. Granted, I have no idea if any of these should oscillate, but still the are dropping in energy over time as they should, even the Verlet in this case. 


This is the full extent of the work I put into this project. I would have done one of the extensions, but I have too much work to do.