## The Goal

1) Define a square grid with a sticky aggregate in the middle.
2) Create a new particle at the edge (randomly, ideally).
3) Step one grid position (up, down, left, right)
4) Check for aggregate
 a) If yes, add to aggregate and start a new particle.
 b) If no, step again.

# Techniques

Start the particles sort-of in the middle, between the center and the edge.

Make a bigger circle around it called a "zone of death".
If a particle starts and crosses into the zone of death, restart that particle. 

The edge must grow as the aggregate grows.

# Initially

Define np.array that the aggregate will grow on. Find the midpoint.

- tree = np.array([w,h])
- tree[x0, y0] = 1

- tree = np.zeros([w,h]) # creates w * h array w/ values 1
- tree[4:6,4:7] # (rows 4 to 6, columns 4 to 7)
- np.sum(tree[3:6,4:7]) # adds everything in that square

In a grid-like fashion, the aggregate has a value of 1, and that is what is checked to stick.
Then, define a stickiness parameter (0 to 1). 

# By Thursday

Generate a 100-particle aggregate by Thursday (square grid, no sticky factor).



