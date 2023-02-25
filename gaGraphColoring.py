from random import randint
import numpy as np
from itertools import tee

n = 20
popSize = 20
graph = []
maxNumColors = 0

#! UTILITY
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

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

# TODO: Fitness function
def fitnessFunc(population):
    # Goal is to minimize fitness
    fitnessArray = []

    for chromosome in population:
        penalty = 0

        for vertex1 in range(n):
            # It could be i+1, since when i == j, graph[i][j] guaranteed to be 0
            for vertex2 in range(vertex1, n):
                if graph[vertex1][vertex2] == 1 and chromosome[vertex1] == chromosome[vertex2]:
                    penalty += 1

        fitnessArray.append(penalty)
    
    return fitnessArray

def selectParent(population, fitnessScores, ratio):
    # RETURN: Dict: {index: parent chromosome}
    # Fitness scores map with each chromosome in population

    # Ratio is the percentages of chromosomes to be designated as parents
    parentsToSelect = int(len(population) * ratio)
    # Maybe need to handle odd or even numbers

    # Dictionary is more efficient than list - make a dictionary of top fitness parents
    parentDict = {}
    for index in np.argsort(fitnessScores)[-parentsToSelect:]:
        
        parentDict[index] = population[index]
    # print(topParents)
    return parentDict

def getEliteChromosomes(population, fitnessScores, ratio):
    numItems = int(len(population) * ratio)
    result = []
    for index in np.argsort(fitnessScores)[-numItems:]:
        result.append(population[index])
    return result

# First crossover function
def twoPointCrossover(parent1, parent2):
    firstPoint = randint(1, n - 3)
    secondPoint = randint(firstPoint + 1, n - 1)

    child1 = np.concatenate((parent1[:firstPoint], parent2[firstPoint:secondPoint], parent1[secondPoint:]))

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


# TODO: New mutation
def mutation2(population, percent):
    print('New mutation function')

    newpop = population 
    numMutations = int(len(population) * percent)
    for mutation in range(numMutations):
        # Do something
        continue

    return newpop

def geneticAlgo():
    print('jhi')

if __name__ == '__main__':
    graph = createGraph()
    # printGraph()
    getMaxColors()
    print('Max colors:', maxNumColors)


    population = createPopulation()
    # print(population)

    fitnessScores = fitnessFunc(population)
    # print(fitnessScores)

    count = 0
    while 0 not in fitnessScores:
        count += 1
        parents = selectParent(population, fitnessScores, 0.5)
        print(parents)
        # print(parents)
        # print(population)

        population = []
        # Loop over parents and perform crossover and generate a child population
        # for index, chromosome in parents.items():
        for (index1, chromosome1), (index2, chromosome2) in pairwise(parents.items()):
            child = twoPointCrossover(chromosome1, chromosome2)
            population.append(child)

        # Do mutation here on the new children
        population = mutation1(population, 0.05)

        # hello = 0
        # for items in elites:
        #     hello += 1
        #     population.append(items)
        # print(hello)
        
        for i in range(len(population), popSize):
            population.append(createChromosome())
        
        fitnessScores = fitnessFunc(population)

        print(fitnessScores)

        if 0 in fitnessScores:
            print(count, population[fitnessScores.index(0)])

        # Each solution is represented in a 1D array where the index of each item in that array maps to the index of a vertex in the graph
        # These vertices in the solution are assigned the lowest color number that they can be assigned
