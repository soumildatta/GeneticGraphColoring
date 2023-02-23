from random import randint
import itertools
import numpy as np

n = 20
popSize = 100
graph = []
maxNumColors = 0

def createGraph():
    graph = np.random.randint(0, 2, size=(n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
                continue
            graph[i][j] = graph[j][i]

    return graph

def printGraph():
    print([row for row in graph])

def getMaxColors():
    global maxNumColors
    for row in graph:
        currMax = sum(row)
        if currMax > maxNumColors:
            maxNumColors = currMax

def createChromosome():
    return np.random.randint(1, maxNumColors + 1, size=(n))

def createPopulation():
    return np.array([createChromosome() for i in range(popSize)])

# First crossover function
def twoPointCrossover(parent1, parent2):
    firstPoint = randint(1, n - 3)
    secondPoint = randint(firstPoint + 1, n - 1)

    # Print parents
    # print(f'Parent 1:\t{parent1}\nParent 2:\t{parent2}')

    child1 = np.concatenate((parent1[:firstPoint], parent2[firstPoint:secondPoint], parent1[secondPoint:]))
    # child2 = np.concatenate((parent2[:firstPoint], parent1[firstPoint:secondPoint], parent2[secondPoint:]))

    # print(f'Child1:\t\t{child1}\nChild2:\t\t{child2}')
    # print(f'Child1:\t\t{child1}')

    return np.array(child1)

# TODO: Second crossover function

def mutation1(population, percent):
    # Random mutation 
    # Returns a new population

    # Soft copy - not creating new list, simply for more understandable code 
    newpop = population

    numMutations = int(len(population) * percent)

    for mutation in range(numMutations):
        # Select random index to mutate
        index = randint(0, len(population) - 1)

        # Mutate randomly selected chromosome
        randomGene = randint(0, len(population[index]) - 1)
        population[index][randomGene] = randint(1, maxNumColors)

    return newpop

def geneticAlgo():
    print('jhi')

if __name__ == '__main__':
    graph = createGraph()
    # printGraph()
    getMaxColors()
    print('Max colors:', maxNumColors)
    population = createPopulation()
    print(population)
    twoPointCrossover(createChromosome(), createChromosome())
    newPop = mutation1(population, 0.30)
    print(newPop)


    # Each solution is represented in a 1D array where the index of each item in that array maps to the index of a vertex in the graph
    # These vertices in the solution are assigned the lowest color number that they can be assigned