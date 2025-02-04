Author: Adam Grice
Project: P1-DLA
Date: 02-04-2025


Questions:

1. Asking the difference between types of dimension is a weird question. From what I can tell, the main difference that is pertinent to this project is that capacity dimension provides a more precise measure of the space around a point. This would be useful for a simulation like this where the area around each "particle" determines its behavior. When I was reading the wikipedia page about Hausdorff dimension I saw a note stating that "Brownian motion in dimension 2 and above is conjectured to be Hausdorff dimension 2" which is relevant for DLA. I did not investigate this conjecture further as I do not have access to the paper which was referenced, and most of what I read about Hausdorff and topological dimensions made my eyes glaze over. I'm not a math major.

2. That depends on what is meant by "replicate." Currently my code cannot handle 3600 particles, so that's out the window. If it could, then I could only produce an approximate replica, an exact one would be so unlikely that I can consider it impossible. With a high voltage power supply I could produce a similar image on a wooden board, or I could buy a crystal growing kit and make some souveniers for the class.

3. I expect that capacity dimension increases with S. The more likely a particle is to stick to the aggregate, the more branches will appear. From what little I understand of capacity dimension I guess that it would increase with more branches.


Attribution: So far I have leaned heavily on Dr. Reid, wikipedia.org, numpy.org, and matplotlib.org. Other, less helpful resources include geeksforgeeks.org and stackoverflow.com. 


Timekeeping: Current estimate is 10-15 hours on the code itself, and another 1.5-2 hours on the writeup.


Languages, Libraries, Lessons Learned: 

1. Once again used python because it is more intuitive for me than other languages I have used in the past. I did not change language mid-project because that sounds like way more work.

2. I used numpy, matplotlib, and PLA. Dr. Reid used time for some troubleshooting. I found all of these to be useful and fairly easy to implement, with the only major problem being that I can't read and made an error in my use of numpy.random.randint()