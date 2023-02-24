from random import randint
import numpy as np

n = 20
popSize = 20
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
    print(fitnessScores)

    parents = selectParent(population, fitnessScores, 0.5)
    print(parents)

    # Loop over parents and perform crossover and generate a child population
    twoPointCrossover(createChromosome(), createChromosome())
    newPop = mutation1(population, 0.30)




    # print(newPop)

    # Each solution is represented in a 1D array where the index of each item in that array maps to the index of a vertex in the graph
    # These vertices in the solution are assigned the lowest color number that they can be assigned