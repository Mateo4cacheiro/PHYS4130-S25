---
   Author: Ethan White
   Topic: Homework 1, ODE Solver
   Course: PHYS 4130
   Term: Spring 2025
---

# parts left
5
6

### Questions

1. Discretized equations of motion are given by:

$y(t_{i+1})=y(t_{i})+v(t_i)\cdot dt$
$v(t_{i+1})=v(t_{i})+(-g-\beta)\cdot dt$

2. A plot of y(t) with nts = 20, 40, 80, 160 is portrayed below (with the analytic solution):

<figure>
  <img src=Figure1.png>
  <figcaption>A line of y = 12 and y = 0 are displayed as well (just for reference). As step size increases, Euler's method approaches the analytic solution (kinematics equations) extremely well. </figure>
<p>&nbsp;</p>

3. A plot of the error at $t_{max}$ vs $\delta t$:

<figure>
  <img src=Figure2.png>
  <figcaption> A plot of the $t_{max}$ versus $\delta t$ graph. The resulting slope is 1.78, which means they are proportional to eachother.
<p>&nbsp;</p>

4. Plots of y(t) and v(t) with drag are below: 

<figure>
  <img src=Figure3.png>
  <figcaption> A plot of y(t) and v(t) with drag are below. In this case, I used nts = 400 since anything higher felt pointless. Note that the betas follow the Fibonnaci sequence since doubling it every iteration felt like too much.
<p>&nbsp;</p>

5. I think that the drag graphs make sense because beta essentially just amplifies the gravitational acceleration (like beta = 5 would make g = 15). Thus, the item will fall faster for higher beta values (clearly seen with position graph). The velocity graph makes sense because the delta t doesn't change, so the resulting graph being linear from 35 meters per second to -100 meters per second makes sense (no quadratic change from t^2 in kinematic equation).

6. The resolution I chose for the drag graphs is acceptable because the error at nts = 320 was 5%, and the purpose of plotting the drags was to get a 'good enough' idea of what beta does (I think), so a 3-4% error margin was good enough to visualize what the drag does to the velocity and position graphs.
