from random import randint
import random
import numpy as np
from itertools import tee

n = 30
popSize = 50

graph = []
maxNumColors = 0

#! ============== GRAPH AND POPULATION CREATION FUNCTIONS
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
def calcFitness(graph, chromosome):
    penalty = 0
    for vertex1 in range(n):
        for vertex2 in range(vertex1, n):
            if graph[vertex1][vertex2] == 1 and chromosome[vertex1] == chromosome[vertex2]:
                penalty += 1
    return penalty


#! ============== SELECTION
def truncationSelection(population):
    print('hi')

def tournamentSelection(population):
    newPopulation = []
    for _ in range(2):
        random.shuffle(population)
        for i in range(0, popSize - 1, 2):
            if calcFitness(graph, population[i]) < calcFitness(graph, population[i + 1]):
                newPopulation.append(population[i])
            else:
                newPopulation.append(population[i + 1])
    return newPopulation


#! ============== CROSSOVER
def onePointCrossover(parent1, parent2):
    splitPoint = randint(2, n - 2)
    child1 = np.concatenate((parent1[:splitPoint], parent2[splitPoint:]))
    child2 = np.concatenate((parent2[:splitPoint], parent1[splitPoint:]))
    return child1, child2


#! ============== MUTATION
def mutation(chromosome, chance):    
    # Find invalid vertex to mutate
    possible = random.uniform(0, 1)
    if chance <= possible:
        for vertex1 in range(n):
            for vertex2 in range(vertex1, n):
                if graph[vertex1][vertex2] == 1 and chromosome[vertex1] == chromosome[vertex2]:
                    chromosome[vertex1] = randint(1, maxNumColors)
    return chromosome


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
    getMaxColors()

    checkCount = 0

    print(f'Trying to color with {maxNumColors} colors')
    while True:
        population = createPopulation()

        bestFitness = calcFitness(graph, population[0])
        fittest = population[0]

        # Generation Control
        generation = 0
        numGenerations = 1000

        if n >= 40:
            numGenerations = n * 15

        while bestFitness != 0 and generation != numGenerations:
            generation += 1
            population = tournamentSelection(population)

            #! CROSSOVER
            newPopulation = []
            random.shuffle(population)
            for i in range(0, len(population) - 1, 2):
                child1, child2 = onePointCrossover(population[i], population[i + 1])
                newPopulation.append(child1)
                newPopulation.append(child2)

            #! MUTATION
            for chromosome in newPopulation:
                if generation < 200:
                    chromosome = mutation(chromosome, 0.5)
                elif generation < 400:
                    chromosome = mutation(chromosome, 0.4)
                else:
                    chromosome = mutation(chromosome, 0.2)

            #! FITNESS
            population = newPopulation
            bestFitness = calcFitness(graph, population[0])
            fittest = population[0]
            for individual in population:
                if(calcFitness(graph, individual) < bestFitness):
                    bestFitness = calcFitness(graph, individual)
                    fittest = individual

            if bestFitness == 0:
                break

            # if generation % 10 == 0:
            #     print(f'generationeration: {generation}, Best Fitness: {bestFitness}, Individual: {fittest}')

        # print(f'Using {maxNumolorsx} colors')
        if bestFitness == 0:
            print(f'{maxNumColors} colors succeeded! Trying {maxNumColors - 1} colors')
            maxNumColors -= 1
            checkCount = 0
        else:
            if checkCount != 1:
                print(f'{maxNumColors} failed. For safety, checking for improvement with {maxNumColors - 1} colors')
                maxNumColors -= 1
                checkCount += 1
                continue

            print(f'Graph is {maxNumColors + 1} colorable')
            print('Test Solution:', testColoring())
            break