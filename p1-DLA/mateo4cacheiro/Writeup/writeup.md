
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
    
    
 3. Can you replicate Witten and Sander's published capacity dimension?
 4. How does the capacity dimension change as a function of *S*?

### Attribution
What resources did you use on this assignment? People, websites, books, etc.

### Timekeeping
How long did you spend on this assignment? If you didn't keep an accurate log, an estimate is fine.

### Languages, Libraries, Lessons Learned
 1. What language did you use for your submission? Is it the same one you started using? If not, why'd you change?
 2. What libraries did you use in your submission? Were any of them remarkable? Great to use, super annoying to use, etc?

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

