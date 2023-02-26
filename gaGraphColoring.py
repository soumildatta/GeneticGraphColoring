from random import randint
import random
import numpy as np
from itertools import tee

n = 35
popSize = 50
graph = []
maxNumColors = 0

#! UTILITY
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#! ============== CREATION FUNCTIONS
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
    # Each solution is represented in a 1D array where the index of each item in that array maps to the index of a vertex in the graph
    return np.random.randint(1, maxNumColors + 1, size=(n))

def createPopulation():
    return np.array([createChromosome() for i in range(popSize)])


#! ============== FITNESS FUNCTION
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


#! ============== SELECTION FUNCTIONS
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

def tournamentSelection(population, fitnessScores, ratio):
    # RETURN: DICT: (index: parent chromosome)

    parentsToSelect = int(len(population) * ratio)

    parentDict = {}
    for index in range(0, parentsToSelect, 2):
        if fitnessScores[index] > fitnessScores[index + 1]:
            parentDict[index] = population[index]
        else:
            parentDict[index + 1] = population[index + 1]

    return parentDict


#! ============== ELITISM
def getEliteChromosomes(population, fitnessScores, ratio):
    numItems = int(len(population) * ratio)
    result = []
    for index in np.argsort(fitnessScores)[-numItems:]:
        result.append(population[index])
    return result


#! ============== CROSSOVER FUNCTIONS
# First crossover function
def twoPointCrossover(parent1, parent2):
    firstPoint = randint(1, n - 3)
    secondPoint = randint(firstPoint + 1, n - 1)
    child1 = np.concatenate((parent1[:firstPoint], parent2[firstPoint:secondPoint], parent1[secondPoint:]))

    return np.array(child1)

def twoPointCrossover2(parent1, parent2):
    firstPoint = randint(1, n - 3)
    secondPoint = randint(firstPoint + 1, n - 1)
    child1 = np.concatenate((parent1[:firstPoint], parent2[firstPoint:secondPoint], parent1[secondPoint:]))
    child2 = np.concatenate((parent2[:firstPoint], parent1[firstPoint:secondPoint], parent2[secondPoint:]))

    return np.array(child1), np.array(child2)

def onePointCrossover(parent1, parent2):
    splitPoint = randint(1, n - 2)
    child1 = np.concatenate((parent1[0:splitPoint], parent2[splitPoint:]))

    return np.array(child1)

#! ============== MUTATION FUNCTIONS
def mutation1(population, percent):
    # Random mutation 
    # Returns a new population
    numMutations = int(len(population) * percent)

    for mutation in range(numMutations):
        # Select random index to mutate
        index = randint(0, len(population) - 1)

        # Mutate randomly selected chromosome
        randomGene = randint(0, len(population[index]) - 1)
        population[index][randomGene] = randint(1, maxNumColors)

    return population

def newMutation(population, percent):
    numMutations = int(len(population) * percent)

    for mutation in range(numMutations):
        index = randint(0, len(population) - 1)
        chromosome = population[index]

        for vertex in range(len(chromosome)):
            adjacentColors = []
            for otherVertex in range(vertex + 1, len(chromosome)):
                if chromosome[vertex] == chromosome[otherVertex] and graph[vertex][otherVertex] == 1:
                    adjacentColors.append(chromosome[vertex])
            validColors = [color for color in range(maxNumColors + 1) if color not in adjacentColors]
            population[index][vertex] == random.choice(validColors)
                    
        # adjacentColors = [chromosome[vertex] for vertex in range(len(chromosome)) if graph[index][vertex] == 1]
        # validColors = [color for color in range(maxNumColors + 1) if color not in adjacentColors]

    return population

def mutation2(population, percent):
    numMutations = int(len(population) * percent)

    for mutation in range(numMutations):
        # Select chromosome
        index = randint(0, len(population) - 1)

        chromosome = population[index]

        # Find invalid vertex to mutate
        for vertex1 in range(n):
            for vertex2 in range(vertex1, n):
                if graph[vertex1][vertex2] == 1 and chromosome[vertex1] == chromosome[vertex2]:
                    chromosome[vertex1] = randint(1, maxNumColors)
        population[index] = chromosome

    return population


def mutation12(individual):
    probability = 0.4
    check = random.uniform(0, 1)
    if(check <= probability):
        position = random.randint(0, n-1)
        individual[position] = random.randint(1, maxNumColors)
    return individual

def mutation22(individual):
    probability = 0.2
    check = random.uniform(0, 1)
    if(check <= probability):
        position = random.randint(0, n-1)
        individual[position] = random.randint(1, maxNumColors)
    return individual



#! --------- TEST METHODS
def generateTestGraph():
    global graph
    result = {}

    for i in range(n):
        result[i] = []
        for j in range(n):
            if graph[i][j] == 1:
                result[i].append(j)

    return result

def maxColoring(colorDict):
    maxColors = max(colorDict.values())
    return maxColors

def testColoring():
  graph = generateTestGraph()
  vertices = sorted((list(graph.keys())))
  colour_graph = {}

  for vertex in vertices:
    unused_colours = len(vertices) * [True]

    for neighbor in graph[vertex]:
      if neighbor in colour_graph:
        colour = colour_graph[neighbor]
        unused_colours[colour] = False
    for colour, unused in enumerate(unused_colours):
        if unused:
            colour_graph[vertex] = colour
            break

  return maxColoring(colour_graph)

#! ------------- END TEST METHODS 


if __name__ == '__main__':
    graph = createGraph()
    # printGraph()
    getMaxColors()

    checkCount = 0

    while True:
        print('Max colors:', maxNumColors)

        population = createPopulation()
        # print(population)

        fitnessScores = fitnessFunc(population)
        # print(fitnessScores)

        generations = 0
        numGenerations = 3500
        
        # Dynamically increase number of generations based on n
        if n  >= 30:
            numGenerations *= 200

        while 0 not in fitnessScores and generations < numGenerations:
            generations += 1
            # tournamentSelection(population, fitnessScores, 0.4)

            #! ====== PARENT SELECTION
            parents = {}
            if generations <= 1000:
                parents = tournamentSelection(population, fitnessScores, 1.0)
            else:
                parents = selectParent(population, fitnessScores, 0.9)

            #! ====== CROSSOVER
            population = []
            # Loop over parents and perform crossover and generate a child population
            for (index1, chromosome1), (index2, chromosome2) in pairwise(parents.items()):
                if generations <= 800:
                    child = twoPointCrossover(chromosome1, chromosome2)
                    population.append(child)
                elif generations <= 2000:
                    child1, child2 = twoPointCrossover2(chromosome1, chromosome2)
                    population.append(child1)
                    population.append(child2)
                else:
                    child = onePointCrossover(chromosome1, chromosome2)
                    population.append(child)

            #! ======= MUTATION
            # Do mutation here only on the new children
            # population = newMutation(population, 0.7)

            if generations <= 300:
                population = mutation1(population, 0.5)
            elif generations <= 1000:
                population = newMutation(population, 0.7)
            elif generations <= 3000:
                population = mutation2(population, 0.7)
            else:
                population = mutation2(population, 0.8)

            # for individual in range(len(population)):
            #     if generations < 1000:
            #         population[individual] = mutation12(population[individual])
            #     else:
            #         population[individual] = mutation22(population[individual])

            #! RANDOMLY ADD A PARENT TO THE POPULATION
            parent = list(parents.values())
            parent = random.sample(parent, k=2)
            population.append(parent[0])
            
            #! Fill up the rest of the population with random values
            for i in range(len(population), popSize):
                population.append(createChromosome())
        
            # TODO: Shuffle population

            np.random.shuffle(population)
            fitnessScores = fitnessFunc(population)

            if 0 in fitnessScores:
                print(generations, population[fitnessScores.index(0)])
                break
        
        if 0 in fitnessScores:
            maxNumColors -= 1
            generations = 0
        else:
            # print(generations, population[fitnessScores.index(1)])
            if checkCount != 1:
                print('Checking for improvement')
                maxNumColors -= 1
                checkCount += 1
                continue

            print('Solution found:', maxNumColors + 1)
            print('Test Solution:', testColoring())

            break
