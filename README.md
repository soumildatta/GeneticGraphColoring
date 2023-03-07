# Genetic Graph Coloring Algorithm

The graph coloring algorithm is essential to several applications in multiple domains. However, its classification as an NP-complete problem means that there are no found efficient solutions to solve it. While most algorithms depend on the skills, and problem-solving power of the programmer, genetic algorithms have an opportunity to bypass all the human thinking and use randomization to find the closest solution to the problem. This project implements a genetic algorithm based graph coloring algorithm. The goal of this algorithm is to find the chromatic number. To do that, it must minimize its fitness (penalty) value.

The genetic algorithm is run on an graph with _n_ vertices. This graph is represented as an n x n adjacency matrix where each rows and columns represent vertices and 1s represent an edge to a vertex. A vertex cannot have an edge to itself, hence the diagonal of the adjacency matrix is forced to contain 0s.    

## Execution Instructions
Requirements: Python 3.7+, GCC Compiler (For CPP Version)   
This project contains both the Genetic Algorithm version, as well as the Non-Genetic Algorithm version. To run either program, simply run them as a normal Python program as such:

```python <program_name>```


## Algorithm Details
**Chromosome Representation** - One gene reprsenting the color for each vertex in the graph, generated with random colorings
**World Representation** - Contains several chromosomes generated randomly  
**Parent Selection** - Truncation selection, Tournament selection - Tournament selection performs better
**Crossover** - One point crossover, Two point crossover - One point crossover performs better   
**Mutation** - Checks if two vertices have the same color in a chromosome. If they do, and if the graph has an edge between those vertices, then the vertex is mutated with a random color. This idea was borrowed from a paper by Hindi et al. 
**Fitness Function** - Compares each gene to each other in the chromosome. If two genes have the same color in the chromosome, check if the vertices have an edge in the graph adjacency matrix. If they do, increment fitness.