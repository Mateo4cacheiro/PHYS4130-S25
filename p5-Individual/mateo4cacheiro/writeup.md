
---
    Author: Mateo Cacheiro
    Topic: Network Analysis
    Course: TN Tech PHYS4130
    Term: Spring 2025
---


# The Writeup
## Introduction

At their core, networks are collections of objects with connections between them that resemble some form of relationship. Admittiedly this is an extremly vague definintion; however, having an abstract definition allows networks to be used when studying a variety of different systems. For example, networks can be used to track the transmission of sexually transmitted deseises by connecting idividuals based on romantic relationships (Figure 1)[5]. In a more positive contexts networks can be used to track co-author colaborations within a field of research [6]. 

Networks can be used in non-human scenerios as well including how airlines can find flights options using the least amount of layovers. In each of these examples the common trait is the presence of objects and their connections. In the field of network analysis these are refered to as "nodes" and "edges". Specfically, a network is any collection of nodes that are connected by any number of edges.  

Beyond their visual appeal (see Figure 1), the statistical properties of networks can be studied in order to draw conclusions about the system. In this coding project the only property that will be studied is the average path length between nodes. A common example used to explain the interest of average path length is the six degrees of seperation. Esseintally this is the idea that by asssuming there exists some small amount of random connections that act as "short-cuts" within the population, all humans are on average 6 connections from one another.

<figure>
  <img src=Networks/images/boys_and_girls.png>
  <figcaption align="center">Network of romantic relationships over an 18 month period in a large midwestern highschool [5].</figcaption>
</figure>
<p>&nbsp;</p>


Unfortunatly, the code discussed here has only been used to study networks of up to a few thousand nodes as the computation time required to investigate eight billion node networks is beyond the scope of this project. Nevertheless, these networks can succesfully show how few random connections are needed to decrease the average path length. The project uses Sethna's textbook [3] and Chris Myers' coding activity [1-2] as motivation however most of the algorithms in SmallWorlds.py and Networks.py were written by the author of this markdown file. 

## Methods and code
The core program uses three python files: NetGraphics.py, Networks.py, and SmallWorlds.py. While the first two files can be used for any general networking alogrithm, the third file was specfically written to create the small world networks discussed here. 

### NetGraphics.py
This file was written by Chris Myers at Cornell and completes all the visual tasks of the program. A new network graphing library could have been written; however, completing this task would a lot more effort with very little educational benifits. The file contains many functions but in this project only the GenerateCircleGraphImage function was used. As the name suggests this function receives a network dicitonary as an imput and produces a figure containing an image of that network. 

<figure>
  <img src=Networks/images/Other/circle8.png>
  <figcaption align="center">Example figure that was generated for a network with 8 nodes where each node is connected to its' two neighbors.</figcaption>
</figure>
<p>&nbsp;</p>

### Networks.py
This is the primary file of the project. The purpose of this file is complete all tasks that alter, create, and analyse a network. Within the file, the most import feature is the network class. The network class contains a dictionary of all the connections between nodes and list of functions used to edit and read information from this dictionary. The keys of the dictionary represent the starting node while the values in the dictionary represent the ending node of a connection. All networks created using Networks.py are undirected menaing that the connections between edges have no direction. 

#### HasNode(self, node)
The HasNode function will return a boolian after searching the dictionary for the key it receives as an input. If that key is found the function returns true. If the key is not found then the key is returned false. The function exists as a safety step to prevent previously defined nodes from being re-defined. 

#### AddNode(self, node)
This function will call the HasNode function. If HasNode returns true then this function does nothing. On the other hand if HasNode returns false, then this function will create a new key in the network's dictionary. The value associated with this key will be empty. 

#### AddEdge(self, node1, node2)
The function will attempt to add both imputed nodes to the dictionary using the AddNode function. This ensures both nodes will exist before the program tried to add values to that key. Once the nodes are created (or the program verifies that the nodes were created on a previous occasion), the function will add each node as a value to the other's key. The code adds the connection for both keys as this method verifies the network will remain undirected. 

#### GetNodes and GetNeighbors
GetNodes returns the list of keys that the connections dictionary contains. Meanwhile, GetNeighbors will return a copy of the list of contections a specfic node has. 

#### Path Length functions
##### FindAveragePathLength(graph)
After receiving the dictionary of an entire graph the function sends the graph to the FindAllPathLengths function which will return a dictionary of all the path lengths between nodes. The function then finds the sum of all the path lengths and the length of the dictionary to find the average length between all nodes in the network.

##### FindAllPathLengths
The FindAllPathLengths function starts by creating a new dictionary that will store a subdictionary of lengths to each node. To find the lengths the function will call FindPathLegthsFromNode for each node in the network. This method results in the creation of an $L * L$ symmetric dictionary. Because the diagonal of this dictionary is meaningless and it is symmetric, the PathLengths dictionary is defined to store only lower triangle of this matrix. 

##### FindPathLengthsFromNode
As one of the more complicated functions in this project, the FindPathLengthsFromNode function implements a breadth-first seach technique. The program will find all the nodes directly connected to input and record their distance from the node as one. Then the code will determine all nodes connected to this shell and add these nodes to the next shell if they are not already found in the lengths dictionary. This process repeats until all nodes have been connected to inputed node. While this process is effective for finding the lengths between a given node and all other nodes it will fail if there are nodes that do no connect to the cluster the imputed node is in. 

## SmallWorlds.py
The SmallWorlds.py file uses the functions from the Networks.py file to generate specfic kind of network. A small world network can be thought of similarly to that of a small community. All the nodes in the network are assigned to be connected to their closest neighbors and there is a random number of connections between nodes that are not neighbors. The code also has some simple parameters that can be adjusted to changes the amount of nodes in the network ($L$), the number of neighbors each node is connected to ($Z =$ even number), and the probability coeffeicent ($0<p<1$) which defines the number of random connections. 

###SmallWorldSimple
This is the call fucntion that will activate the process for creating a small world network. This function will also call the DisplayCircleGraph function from NetGraphics to make a png of the network.

###MakeSmallWorldSimpleNetwork
When this is called in the SmallWorldSimple function it receives values for $L$, $Z$ and $p$. The function starts be generating a simple ring network containing all the nodes and $Z$ connections with their closest neighbors (Figure 3). Once the ring is formed the function uses the probabilty coeffeicent to find the number of random edges the network will attempt to form. The equation used to find this value is shown below.

$$NUM_{shortcuts}=\frac{pLZ}{2}$$

Once this value is calculated the network and this number are sent to AddRandomEdges function that returns a new networks with additional connections. 

<figure>
  <img src=Networks/images/20N/20N_10E_0.0p.png>
  <figcaption align="center">Example of a ring network. Z=10, L=20</figcaption>
</figure>
<p>&nbsp;</p>

### MakeRingGraph
The function begins by creating a network class. Once this class is made it uses a series of for loops to create each node and then connects all noded to predetermined number of neighbors set by $Z$. A primary stuggle that was faced when developing this function was making sure the end points would properly connect and ensuring the method would continue to work when $Z>\frac{L}{2}$. Addmittingly there is probably a more clear and effective method for accoplishing this task; however, this method is successful. 

### AddRandomEdges
This function is very simple. It runs a while loop until the code has attempted to add $NUM_{shortcuts}$. For each loop the code selects two random nodes and as long as the two randomly selected nodes are not the same node, an edge is created between them. This method works because the AddEdge function already checks if the connection exists. Using this method it is possible that fewer than $NUM_{shortcuts}$ are added if the random nodes had a connection before being selected. An example of a network with random shortcuts is shown in Figure 4.

<figure>
  <img src=Networks/images/20N/20N_10E_0.2p.png>
  <figcaption align="center">Example of a ring network with random shortcuts. Z=10, L=20, p=0.2</figcaption>
</figure>
<p>&nbsp;</p>

## Data and findings

Once all the functions were written and tested to ensure they work properly a for loop was used to calculate the average path length between nodes with different probability coefficients. The networks used had 50 nodes and each were connected to its two closest neighbors. The base ring is shown in figure 5. 

<figure>
  <img src=Networks/images/50N_2E/50N_2E_0.0p.png>
  <figcaption align="center">Image of base ring used when studying the average path length<figcaption>
</figure>
<p>&nbsp;</p>

The for loop found the average distance between nodes for 10K different probability coefficients. Images were not created for all 10K networks however the most notatable 1K networks have been uploaded to the github in the Networks/images/50N_2E directory. Once these values were found, the following plot was formed. 

<figure>
  <img src=Networks/images/Average_Length_vs_Probability.png>
  <figcaption align="center">Plot of average distance between nodes vs. the probability coefficient</figcaption>
</figure>
<p>&nbsp;</p>

As expected the plot shows a large amount of random variation but it clearly follows an exponentail decay. Considering this plot contains 10K points, these data points were bined into bins of size 10. Doing this helps to identify the effect the probability has on the average length between nodes and helps to reduce the random variations. 

<figure>
  <img src=Networks/images/Average_Length_vs_Probability_with_size_10_bins.png>
  <figcaption align="center">Plot of average distance between nodes vs. the probability coefficient  (size 10 bins)</figcaption>
</figure>
<p>&nbsp;</p>

After seeing the success of size 10 bins this process was repeated for bin containing 100 data points.

<figure>
  <img src=Networks/images/Average_Length_vs_Probability_with_size_100_bins.png>
  <figcaption align="center">Plot of average distance between nodes vs. the probability coefficient (size 100 bins)</figcaption>
</figure>
<p>&nbsp;</p>

By observing the above plots it is clear that the behavior follows an exponentail decay pattern. It is also worth noting that some clustering seems to be appearing for low p values. It is unknown why this behavior is occurring however it is possible that this is a result of flaw in the creation of random shortcuts discussed earlier or an odd feature of the bining method. Overall the project successfully created networks and demonstrated how quickly random shortcuts and decrease the average distance between nodes in a network.

### Attribution
[1] https://cac.cornell.edu/myers/teaching/ComputationalMethods/ComputerExercises/Networks/NetworksExercise.html

[2] https://cac.cornell.edu/myers/teaching/ComputationalMethods/ComputerExercises/SmallWorld/SmallWorld.html

[3] https://sethna.lassp.cornell.edu/StatMech/

[4] https://cac.cornell.edu/myers/teaching/ComputationalMethods/ComputerExercises/Networks/kleinberg_graph_handout.pdf

[5] Peter Bearman, James Moody, and Katherine Stovel. Chains of affection: The structure

of adolescent romantic and sexual networks. American Journal of Sociology, 110(1):44–
99, 2004.

[6] Meagan Sundstrom: Collaborations near and far, old and new: Co-authorship networks in Physical Review Physics Education Research


### Timekeeping
I have spent between 15 and 20 hours on this assignment.

### Languages, Libraries, Lessons Learned
 1. What language did you use for your submission? Is it the same one you started using? If not, why'd you change?

All of the code for this project was writen in python. I started in python becuase the sethna guides suggested using python and all the support materials for the project used python as well. Because the project was already set up for python it made the process easier to stick with the suggested language. 


 2. What libraries did you use in your submission? Were any of them remarkable? Great to use, super annoying to use, etc?

This project pulled from many different libraries in order to work correctly. Like previous projects, numpy, matplotlib, and scipy were used to accopmlish basic tasks with math, ploting, and other routine methods. Beyond the normal 3, random, importlib and the NetGraphics libraries were used. NetGraphics is a networks graphics library created by Chris Myers at cornell. This library gave me lots of issues. For starters my computer can't properly access temporary files, so the method NetGraphics used to properly save and display images would not function properly. To account for this the temporary file location was changed to a known address so the image could be found. Within the NetGraphics file there are 3 new libraries I had not used before (os, PIL, and tempfile). All three of these libraries are used to help generate figures onto a computer. The other issue I ran into with  Myers's files was the use of scipy. Scipy was used in countless locations were I have normally used numpy. Examples of this include square roots, trig fuctions, etc. Unforntuatly Scipy no longer supports these functions so I had to troubleshoot the source file to correct for the issues that the file was running into.  
