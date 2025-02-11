

---
meta:
    author: Mateo Cacheiro
    topic: Diffusion Limited Aggregation Project
    course: TN Tech PHYS4130
    term: Spring 2025
---


## The Writeup

### Address the following questions in your writeup
 1. What is the difference between capacity dimension[^1] and topological dimension?
    The Capacity Dimension is a value to represent how complicated a "self-similar" figure is. The fractile deminsion can tell us what how many points are in a set/how large a set is. [1]. From what I can find it is essentially a ratio between the log of the number of equal divisions of a particle and log of the factor need to return those divisions to their original size. While this makes a little bit of sense to me for things like a canton line, I have no idea how this can be applied to DLA simmulations. I think the capacity dimension is a dimension used for sets within a metric space but I don't really know what that means either. I have never taken a class or learned about sets or any spaces other than vector spaces so this is well beyond my abilites to fully understand.
    Using the sources I can find/have access to I can't seem to find a definition for a topological dimension in non "Mathemetian Language". I have tried interpreting all the set notation I have encountered but I haven't been successful at understanding anything. topological dimension seems to deal with how points are related to eachother in non spatial ways while the fractal dimension is a measure of how complex the points are in relation to eachother geometrically. 
    
 2. Can you replicate Witten and Sander's published capacity dimension?
    I think that for the most part the program I made creates the same type of structure that they did. Unforuntatly I don't really understand what is going on in EQ3 and beyond but overall they just seem to be finding differnt coefficents that charatarize the structure that is made. I also don't understand why determining values like the Hausdorff dimension is even a valueble thing to konw. 
 4. How does the capacity dimension change as a function of *S*?
    In concept, the Capacity dimension should increase. the structure should become more dense and complex. However, I can't seem to notice this with my current program. 

### Attribution
[1] https://math.bu.edu/DYSYS/chaos-game/node6.html
[2] https://en.wikipedia.org/wiki/Topological_space
[3] https://u.cs.biu.ac.il/~megereli/final_topology.pdf
[4] https://en.wikipedia.org/wiki/Metric_space
[5] https://www.quora.com/What-exactly-is-topological-dimension-and-how-does-it-relate-to-fractal-dimension
[6] https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.47.1400

### Timekeeping
I have spent between 25 and 30 hours on this assignment since Jan 28.

### Languages, Libraries, Lessons Learned
 1. What language did you use for your submission? Is it the same one you started using? If not, why'd you change?
    I used Python for this program. Its the language I used from the start and I used it because it seems to be the most approachable. While I know a limited amount of C++, python seems to make a lot of things much easier. Overall, the support for python I found on the internet was very helpful so it encouraged me to continue working with the language. 
 2. What libraries did you use in your submission? Were any of them remarkable? Great to use, super annoying to use, etc?
    I used Numpy, Random, Matplotlib, math, and PIL. I wouldn't call any of them remarkable though. If anything Random made my life terrible. I used a command on the internet from one of the links you provided me via email and found a way to determine that the randint() function was extremly slow. 
> [!NOTE]
> This section probably shouldn't more than a few sentences long. Record what you learned and move on!

# The Submission
> [!IMPORTANT]
> Your submissions for this project should be located within this project's directory. You'll have a lot of different "code" and "writeup" directories before all is said and done!

## Code directory
A directory titled "code" that contains your program files and makefile (if used), or a ReadMe.md file that gives sufficiently detailed instructions for me to build and execute your code.

> [!NOTE]
> If you test your code in a Jupyter Notebook, you will need to work to make sure your commit history is legible. I recommend a standalone code file.


## Writeup directory
A directory titled "writeup" containing 
 1. your writeup file: a well-structured markdown file OR a LaTeX document (and its resulting PDF) OR a well-structured Jupyter notebook
 2. Animation(s) of your DLA structures as they grow[^2]
 3. Figures (static, PNG or PDF) of the following
    1. Two noteworthy DLA structures of at least  1e5 particles, and a plot of their fractal dimension as a function of radius
    2. A plot of capacity dimension vs S
 4. Extensions (a.k.a. challenge)
    - Generate a 30 second long DLA animation for $N=1e6$ particles.
    - How does the behavior change with a 2D triangular lattice, where each point has six neighbors instead of four?
    - How does the behavior change in 3D, where each point has six nearest neighbors instead of four?

> [!NOTE]
> If you implement a 3D triangular lattice, each point has 12 neighbors.
> This is not required, or even suggested.

> [!NOTE]  
> This writeup will need to have figures. It's probably easiest to just add those files to your writeup directory and link them with relative markdown links.

> [!TIP]
> Your figures need to be captioned, which is probably easiest to accomplish with the [FigCaption](https://www.w3schools.com/tags/tag_figcaption.asp) attribute.

# Grading
 1. Explanation of undergirding theory
 2. Quality of workflow (including commit history)
 3. Documented implementation of relevant algorithms
 4. Clear and professional presentation of work

> [!TIP]
> You can access this markdown source file and learn from its formatting to improve your work



<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

[^1]: You'll also see this called the fractal or Hausdorff dimension
[^2]: These can be animated GIF files, HTML5 videos, mp4 files, or javascript animations
[^3]: This assignment draws heavily on [Daniel V. Schroeder's DLA module](https://physics.weber.edu/schroeder/javacourse/DLA.pdf)
